#!/usr/bin/env python3
"""Render an evidence-grounded related-work quadrant CSV as accessible SVG."""

from __future__ import annotations

import argparse
import csv
import math
import re
import sys
import unicodedata
from dataclasses import dataclass
from html import escape
from pathlib import Path


REQUIRED_COLUMNS = (
    "record_type",
    "id",
    "label",
    "x",
    "y",
    "category",
    "is_current",
    "source",
    "x_locator",
    "x_evidence",
    "y_locator",
    "y_evidence",
    "uncertainty",
    "verification_status",
    "placement_status",
)
REQUIRED_META = (
    "variant_id",
    "title",
    "reader_question",
    "takeaway",
    "caveat",
    "recommendation",
    "x_axis_label",
    "x_low_label",
    "x_high_label",
    "y_axis_label",
    "y_low_label",
    "y_high_label",
    "quadrant_top_left",
    "quadrant_top_right",
    "quadrant_bottom_left",
    "quadrant_bottom_right",
    "source_note",
)
PLACEHOLDER = re.compile(
    r"(^|[\s:;/_-])(todo|tbd|replace|placeholder|unverified|unknown|n/?a)"
    r"($|[\s:;/_-])|<[^>]+>|\{[^}]+\}",
    re.IGNORECASE,
)
VALID_ID = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*$")
NOTEBOOK_SOURCE_ID = re.compile(
    r"^(?:notebooklm:)?[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-"
    r"[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
    re.IGNORECASE,
)
MAX_LABEL_COLUMNS = 36
MAX_QUADRANT_LABEL_COLUMNS = 42
PALETTE = (
    "#0072B2",
    "#D55E00",
    "#009E73",
    "#CC79A7",
    "#E69F00",
    "#56B4E9",
    "#6A3D9A",
    "#8C564B",
)
SHAPES = ("circle", "square", "diamond", "triangle", "hexagon", "cross")


@dataclass(frozen=True)
class Work:
    work_id: str
    label: str
    x: float
    y: float
    category: str
    is_current: bool
    source: str
    x_locator: str
    x_evidence: str
    y_locator: str
    y_evidence: str
    uncertainty: str
    placement_status: str


@dataclass(frozen=True)
class LabelPlacement:
    x: float
    y: float
    anchor: str
    bbox: tuple[float, float, float, float]
    needs_leader: bool


class ValidationError(Exception):
    """Raised when chart data cannot support a defensible rendering."""

    def __init__(self, issues: list[str]) -> None:
        super().__init__("\n".join(issues))
        self.issues = issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Render a 0–100 related-work quadrant CSV as a deterministic, "
            "accessible SVG. Every work must be verified against saved full text."
        )
    )
    parser.add_argument("input_csv", type=Path, help="filled quadrant CSV")
    parser.add_argument("output_svg", type=Path, help="SVG output path")
    parser.add_argument(
        "--strict",
        "--strict-audit",
        dest="strict",
        action="store_true",
        help=(
            "require audited placements and exact x/y source locators; default mode "
            "allows interpretive communication charts"
        ),
    )
    return parser.parse_args()


def row_issue(row_number: int | None, message: str) -> str:
    prefix = f"row {row_number}: " if row_number is not None else ""
    return f"{prefix}{message}"


def has_placeholder(value: str) -> bool:
    return bool(PLACEHOLDER.search(value))


def display_width(value: str) -> int:
    """Estimate terminal-style display columns, including wide CJK characters."""

    width = 0
    for character in value:
        if unicodedata.combining(character):
            continue
        width += 2 if unicodedata.east_asian_width(character) in {"W", "F"} else 1
    return width


def wrap_display(value: str, max_columns: int) -> list[str]:
    """Wrap text by display columns, preferring spaces without requiring them."""

    remaining = " ".join(value.split())
    if not remaining:
        return [value]

    lines: list[str] = []
    while display_width(remaining) > max_columns:
        columns = 0
        cut = 0
        for index, character in enumerate(remaining):
            character_width = display_width(character)
            if columns + character_width > max_columns:
                break
            columns += character_width
            cut = index + 1

        segment = remaining[:cut]
        space = segment.rfind(" ")
        if space > 0:
            lines.append(segment[:space].rstrip())
            remaining = remaining[space + 1 :].lstrip()
        else:
            lines.append(segment.rstrip())
            remaining = remaining[cut:].lstrip()

    if remaining:
        lines.append(remaining)
    return lines


def has_saved_source(value: str, csv_path: Path) -> bool:
    if NOTEBOOK_SOURCE_ID.fullmatch(value):
        return True
    try:
        candidate = Path(value).expanduser()
    except RuntimeError:
        return False
    if not candidate.is_absolute():
        candidate = csv_path.parent / candidate
    return candidate.is_file()


def parse_boolean(value: str, row_number: int, issues: list[str]) -> bool | None:
    normalized = value.casefold()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    issues.append(
        row_issue(row_number, "is_current must be exactly true or false")
    )
    return None


def parse_coordinate(
    value: str, field: str, row_number: int, issues: list[str]
) -> float | None:
    try:
        coordinate = float(value)
    except ValueError:
        issues.append(
            row_issue(row_number, f"{field} must be a number from 0 through 100")
        )
        return None
    if not math.isfinite(coordinate) or not 0 <= coordinate <= 100:
        issues.append(
            row_issue(row_number, f"{field} must be a finite number from 0 through 100")
        )
        return None
    if not coordinate.is_integer():
        issues.append(
            row_issue(
                row_number,
                f"{field} must be a whole-number anchor; decimal precision is unsupported",
            )
        )
        return None
    return coordinate


def load_chart(path: Path, *, strict: bool = False) -> tuple[dict[str, str], list[Work]]:
    issues: list[str] = []
    if not path.is_file():
        raise ValidationError([f"input file not found: {path}"])

    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            fieldnames = reader.fieldnames or []
            missing = [name for name in REQUIRED_COLUMNS if name not in fieldnames]
            unexpected = [name for name in fieldnames if name not in REQUIRED_COLUMNS]
            if missing:
                issues.append(f"missing required columns: {', '.join(missing)}")
            if unexpected:
                issues.append(f"unexpected columns: {', '.join(unexpected)}")
            if issues:
                raise ValidationError(issues)
            raw_rows = list(reader)
    except (OSError, csv.Error) as exc:
        raise ValidationError([f"could not read CSV: {exc}"]) from exc

    metadata: dict[str, str] = {}
    works: list[Work] = []
    seen_work_ids: set[str] = set()

    for row_number, raw in enumerate(raw_rows, start=2):
        if None in raw:
            issues.append(
                row_issue(row_number, "contains more values than the header defines")
            )
            continue
        row = {key: (value or "").strip() for key, value in raw.items()}
        if not any(row.values()):
            continue

        record_type = row["record_type"].casefold()
        record_id = row["id"]
        if record_type == "meta":
            if record_id not in REQUIRED_META:
                issues.append(
                    row_issue(
                        row_number,
                        f"unknown metadata id {record_id!r}; expected one of "
                        f"{', '.join(REQUIRED_META)}",
                    )
                )
                continue
            if record_id in metadata:
                issues.append(
                    row_issue(row_number, f"duplicate metadata id: {record_id}")
                )
            else:
                metadata[record_id] = row["label"]
            if not row["label"]:
                issues.append(
                    row_issue(row_number, f"metadata {record_id} has an empty label")
                )
            elif has_placeholder(row["label"]):
                issues.append(
                    row_issue(
                        row_number,
                        f"metadata {record_id} still contains a placeholder",
                    )
                )
            elif (
                record_id.startswith("quadrant_")
                and display_width(row["label"]) > MAX_QUADRANT_LABEL_COLUMNS
            ):
                issues.append(
                    row_issue(
                        row_number,
                        f"metadata {record_id} exceeds "
                        f"{MAX_QUADRANT_LABEL_COLUMNS} display columns",
                    )
                )
            continue

        if record_type != "work":
            issues.append(
                row_issue(row_number, "record_type must be exactly meta or work")
            )
            continue

        for field in (
            "id",
            "label",
            "category",
            "source",
            "x_evidence",
            "y_evidence",
            "uncertainty",
        ):
            if not row[field]:
                issues.append(row_issue(row_number, f"{field} is required for work rows"))
            elif has_placeholder(row[field]):
                issues.append(
                    row_issue(row_number, f"{field} still contains a placeholder")
                )

        placement_status = row["placement_status"].casefold()

        for field in ("x_locator", "y_locator"):
            if row[field] and has_placeholder(row[field]):
                issues.append(
                    row_issue(row_number, f"{field} still contains a placeholder")
                )
            if (strict or placement_status == "audited") and not row[field]:
                issues.append(
                    row_issue(
                        row_number,
                        f"{field} is required in --strict mode and whenever "
                        "placement_status=audited",
                    )
                )

        source_is_saved = False
        if row["source"] and not has_placeholder(row["source"]):
            source_is_saved = has_saved_source(row["source"], path)
            if not source_is_saved:
                issues.append(
                    row_issue(
                        row_number,
                        "source must be an existing saved file (absolute or relative "
                        "to the CSV) or a NotebookLM source UUID; a DOI or URL alone "
                        "does not establish a saved full copy",
                    )
                )

        if record_id in seen_work_ids:
            issues.append(row_issue(row_number, f"duplicate work id: {record_id}"))
        elif record_id:
            seen_work_ids.add(record_id)
        if record_id and not VALID_ID.fullmatch(record_id):
            issues.append(
                row_issue(
                    row_number,
                    "id must start with a letter and contain only letters, numbers, "
                    "periods, underscores, or hyphens",
                )
            )
        if display_width(row["label"]) > MAX_LABEL_COLUMNS:
            issues.append(
                row_issue(
                    row_number,
                    f"label exceeds {MAX_LABEL_COLUMNS} display columns; use a "
                    "short, unambiguous chart label such as a system name or "
                    "Author year",
                )
            )

        x = parse_coordinate(row["x"], "x", row_number, issues)
        y = parse_coordinate(row["y"], "y", row_number, issues)
        is_current = parse_boolean(row["is_current"], row_number, issues)

        verification = row["verification_status"].casefold()
        valid_verification = (
            verification == "verified_full_text"
            or (is_current is True and verification == "verified_project_artifacts")
        )
        if not valid_verification:
            issues.append(
                row_issue(
                    row_number,
                    "related works require verification_status=verified_full_text; "
                    "the current work may instead use verified_project_artifacts",
                )
            )

        if placement_status not in {"interpretive", "audited"}:
            issues.append(
                row_issue(
                    row_number,
                    "placement_status must be interpretive or audited",
                )
            )
        elif strict and placement_status != "audited":
            issues.append(
                row_issue(
                    row_number,
                    "placement_status must be audited in --strict mode",
                )
            )

        required_values = (
            record_id,
            row["label"],
            row["category"],
            row["source"],
            row["x_evidence"],
            row["y_evidence"],
            row["uncertainty"],
        )
        if (
            x is not None
            and y is not None
            and is_current is not None
            and all(required_values)
            and not any(has_placeholder(value) for value in required_values)
            and source_is_saved
            and valid_verification
            and placement_status in {"interpretive", "audited"}
        ):
            works.append(
                Work(
                    work_id=record_id,
                    label=row["label"],
                    x=x,
                    y=y,
                    category=row["category"],
                    is_current=is_current,
                    source=row["source"],
                    x_locator=row["x_locator"],
                    x_evidence=row["x_evidence"],
                    y_locator=row["y_locator"],
                    y_evidence=row["y_evidence"],
                    uncertainty=row["uncertainty"],
                    placement_status=placement_status,
                )
            )

    for key in REQUIRED_META:
        if key not in metadata:
            issues.append(f"missing required metadata row: {key}")
    if (
        "recommendation" in metadata
        and not has_placeholder(metadata["recommendation"])
        and metadata["recommendation"].casefold()
        not in {"primary", "secondary", "exploratory"}
    ):
        issues.append(
            "metadata recommendation must be primary, secondary, or exploratory"
        )

    if len(works) < 2:
        issues.append(
            "chart requires the current work and at least one related work with "
            "accepted full-source verification declarations"
        )
    current_count = sum(work.is_current for work in works)
    if current_count != 1:
        issues.append(
            f"chart requires exactly one is_current=true work; found {current_count}"
        )

    if issues:
        raise ValidationError(issues)
    return metadata, works


def overlap_area(
    first: tuple[float, float, float, float],
    second: tuple[float, float, float, float],
) -> float:
    left = max(first[0], second[0])
    top = max(first[1], second[1])
    right = min(first[2], second[2])
    bottom = min(first[3], second[3])
    return max(0.0, right - left) * max(0.0, bottom - top)


def label_bbox(
    text_x: float, text_y: float, anchor: str, width: float
) -> tuple[float, float, float, float]:
    if anchor == "start":
        left = text_x
    elif anchor == "end":
        left = text_x - width
    else:
        left = text_x - width / 2
    return (left - 3, text_y - 15, left + width + 3, text_y + 5)


def place_labels(
    works: list[Work],
    point_positions: dict[str, tuple[float, float]],
    plot_bounds: tuple[float, float, float, float],
    reserved: list[tuple[float, float, float, float]],
) -> dict[str, LabelPlacement]:
    plot_left, plot_top, plot_right, plot_bottom = plot_bounds
    marker_boxes = [
        (x - 13, y - 13, x + 13, y + 13) for x, y in point_positions.values()
    ]
    occupied = list(reserved)
    placements: dict[str, LabelPlacement] = {}
    candidates = (
        (15, -10, "start"),
        (15, 20, "start"),
        (-15, -10, "end"),
        (-15, 20, "end"),
        (0, -21, "middle"),
        (0, 32, "middle"),
        (28, -27, "start"),
        (-28, -27, "end"),
        (28, 35, "start"),
        (-28, 35, "end"),
    )

    ordered = sorted(
        works, key=lambda work: (not work.is_current, work.label.casefold(), work.work_id)
    )
    for work in ordered:
        point_x, point_y = point_positions[work.work_id]
        width = min(280.0, max(54.0, display_width(work.label) * 7.2))
        best: tuple[float, int, LabelPlacement] | None = None
        for order, (offset_x, offset_y, anchor) in enumerate(candidates):
            text_x = point_x + offset_x
            text_y = point_y + offset_y
            bbox = label_bbox(text_x, text_y, anchor, width)

            outside = (
                max(0.0, plot_left + 4 - bbox[0])
                + max(0.0, bbox[2] - plot_right + 4)
                + max(0.0, plot_top + 4 - bbox[1])
                + max(0.0, bbox[3] - plot_bottom + 4)
            )
            overlap = sum(overlap_area(bbox, other) for other in occupied)
            overlap += sum(overlap_area(bbox, marker) * 1.5 for marker in marker_boxes)
            score = outside * 10000 + overlap
            placement = LabelPlacement(
                x=text_x,
                y=text_y,
                anchor=anchor,
                bbox=bbox,
                needs_leader=abs(offset_x) > 20 or abs(offset_y) > 24,
            )
            candidate = (score, order, placement)
            if best is None or candidate[:2] < best[:2]:
                best = candidate

        assert best is not None
        placements[work.work_id] = best[2]
        occupied.append(best[2].bbox)
    return placements


def marker_svg(
    shape: str,
    x: float,
    y: float,
    color: str,
    *,
    size: float = 9,
    stroke_width: float = 2,
) -> str:
    common = (
        f'fill="{color}" stroke="#111111" stroke-width="{stroke_width:g}" '
        'vector-effect="non-scaling-stroke"'
    )
    if shape == "circle":
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size:.1f}" {common}/>'
    if shape == "square":
        return (
            f'<rect x="{x - size:.1f}" y="{y - size:.1f}" '
            f'width="{2 * size:.1f}" height="{2 * size:.1f}" rx="1.5" {common}/>'
        )
    if shape == "diamond":
        points = (
            f"{x:.1f},{y - size - 1:.1f} {x + size + 1:.1f},{y:.1f} "
            f"{x:.1f},{y + size + 1:.1f} {x - size - 1:.1f},{y:.1f}"
        )
        return f'<polygon points="{points}" {common}/>'
    if shape == "triangle":
        points = (
            f"{x:.1f},{y - size - 2:.1f} {x + size + 2:.1f},{y + size:.1f} "
            f"{x - size - 2:.1f},{y + size:.1f}"
        )
        return f'<polygon points="{points}" {common}/>'
    if shape == "hexagon":
        points = " ".join(
            f"{x + size * math.cos(math.radians(angle)):.1f},"
            f"{y + size * math.sin(math.radians(angle)):.1f}"
            for angle in (0, 60, 120, 180, 240, 300)
        )
        return f'<polygon points="{points}" {common}/>'
    points = (
        (x - size, y - size / 3),
        (x - size / 3, y - size / 3),
        (x - size / 3, y - size),
        (x + size / 3, y - size),
        (x + size / 3, y - size / 3),
        (x + size, y - size / 3),
        (x + size, y + size / 3),
        (x + size / 3, y + size / 3),
        (x + size / 3, y + size),
        (x - size / 3, y + size),
        (x - size / 3, y + size / 3),
        (x - size, y + size / 3),
    )
    encoded = " ".join(f"{px:.1f},{py:.1f}" for px, py in points)
    return f'<polygon points="{encoded}" {common}/>'


def category_styles(works: list[Work]) -> dict[str, tuple[str, str]]:
    categories = sorted(
        {work.category for work in works},
        key=lambda value: (value.casefold(), value),
    )
    return {
        category: (PALETTE[index % len(PALETTE)], SHAPES[index % len(SHAPES)])
        for index, category in enumerate(categories)
    }


def render_svg(metadata: dict[str, str], works: list[Work]) -> str:
    legend_categories = sorted(
        {work.category for work in works if not work.is_current},
        key=lambda value: (value.casefold(), value),
    )
    styles = category_styles(works)
    title_lines = wrap_display(metadata["title"], 76)
    reader_lines = wrap_display(metadata["reader_question"], 96)
    x_low_lines = wrap_display(metadata["x_low_label"], 42)
    x_high_lines = wrap_display(metadata["x_high_label"], 42)
    legend_layout: list[tuple[str, list[str], float]] = []
    legend_cursor_y = 36.0
    for category in legend_categories:
        category_lines = wrap_display(category, 34)
        legend_layout.append((category, category_lines, legend_cursor_y))
        legend_cursor_y += max(36.0, len(category_lines) * 16.0 + 10.0)
    current_y = legend_cursor_y + 8.0
    interpretation_limit = (
        "Positions are approximate interpretive judgments for communicating the "
        "landscape; distances are not measurements, and the chart does not establish "
        "overall research quality or novelty."
    )
    source_text = (
        f"Takeaway: {metadata['takeaway']} Caveat: {metadata['caveat']} "
        f"{metadata['source_note']} {interpretation_limit}"
    )
    source_lines = wrap_display(source_text, 145)

    width = 1280
    plot_left = 150.0
    plot_top = (
        112.0
        + 28.0 * (len(title_lines) - 1)
        + 18.0 * (len(reader_lines) - 1)
    )
    plot_width = 760.0
    plot_height = 590.0
    plot_right = plot_left + plot_width
    plot_bottom = plot_top + plot_height

    point_positions = {
        work.work_id: (
            plot_left + work.x / 100 * plot_width,
            plot_bottom - work.y / 100 * plot_height,
        )
        for work in works
    }
    coordinate_groups: dict[tuple[float, float], list[Work]] = {}
    for work in works:
        coordinate_groups.setdefault((work.x, work.y), []).append(work)
    overlapping_groups = [
        (coordinates, group)
        for coordinates, group in sorted(coordinate_groups.items())
        if len(group) > 1
    ]
    overlap_badges: list[tuple[float, float, list[Work]]] = []
    for _, group in overlapping_groups:
        point_x, point_y = point_positions[group[0].work_id]
        badge_x = point_x - 16 if point_x > plot_right - 28 else point_x + 16
        badge_y = point_y + 16 if point_y < plot_top + 28 else point_y - 16
        overlap_badges.append((badge_x, badge_y, group))

    x_axis_y = (
        plot_bottom
        + 78.0
        + 16.0 * (max(len(x_low_lines), len(x_high_lines)) - 1)
    )
    legend_y = plot_top + 14.0
    legend_final_note_y = current_y + 42.0 + (36.0 if overlap_badges else 0.0)
    legend_bottom = legend_y + legend_final_note_y + 18.0
    caption_top = max(x_axis_y + 38.0, legend_bottom + 24.0)
    height = int(max(850, caption_top + 26 * len(source_lines) + 32))

    quadrant_centers = (
        (
            plot_left + plot_width * 0.25,
            plot_top + 26,
            metadata["quadrant_top_left"],
        ),
        (
            plot_left + plot_width * 0.75,
            plot_top + 26,
            metadata["quadrant_top_right"],
        ),
        (
            plot_left + plot_width * 0.25,
            plot_bottom - 14,
            metadata["quadrant_bottom_left"],
        ),
        (
            plot_left + plot_width * 0.75,
            plot_bottom - 14,
            metadata["quadrant_bottom_right"],
        ),
    )
    reserved = [
        (
            center_x - min(170, max(50, display_width(label) * 3.4)),
            center_y - 16,
            center_x + min(170, max(50, display_width(label) * 3.4)),
            center_y + 5,
        )
        for center_x, center_y, label in quadrant_centers
    ]
    reserved.extend(
        (badge_x - 11, badge_y - 11, badge_x + 11, badge_y + 11)
        for badge_x, badge_y, _ in overlap_badges
    )
    placements = place_labels(
        works,
        point_positions,
        (plot_left, plot_top, plot_right, plot_bottom),
        reserved,
    )

    current = next(work for work in works if work.is_current)
    work_descriptions = "; ".join(
        (
            f"{work.label}, category {work.category}, x {work.x:g}, y {work.y:g}"
            f"{', current work' if work.is_current else ''}"
        )
        for work in works
    )
    interpretive_count = sum(
        work.placement_status == "interpretive" for work in works
    )
    audited_count = sum(work.placement_status == "audited" for work in works)
    description = (
        f"Related-work chart variant {metadata['variant_id']} "
        f"({metadata['recommendation']}) with {len(works)} works. "
        f"It asks: {metadata['reader_question']} "
        f"The x axis is {metadata['x_axis_label']}, from "
        f"{metadata['x_low_label']} to {metadata['x_high_label']}. "
        f"The y axis is {metadata['y_axis_label']}, from "
        f"{metadata['y_low_label']} to {metadata['y_high_label']}. "
        f"The highlighted current work is {current.label}, positioned at "
        f"x {current.x:g} and y {current.y:g}. "
        f"{interpretive_count} placements are marked interpretive and "
        f"{audited_count} are marked audited in the CSV. "
        f"Plotted works: {work_descriptions}. "
        f"{source_text}"
    )

    lines: list[str] = []
    append = lines.append
    append('<?xml version="1.0" encoding="UTF-8"?>')
    append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        'aria-labelledby="chart-title chart-desc">'
    )
    append(f'  <title id="chart-title">{escape(metadata["title"])}</title>')
    append(f'  <desc id="chart-desc">{escape(description)}</desc>')
    append("  <defs>")
    append(
        '    <filter id="label-bg" x="-10%" y="-30%" width="120%" height="160%">'
    )
    append(
        '      <feFlood flood-color="#FFFFFF" flood-opacity="0.88" result="bg"/>'
    )
    append(
        '      <feComposite in="bg" in2="SourceGraphic" operator="in" result="mask"/>'
    )
    append('      <feMerge><feMergeNode in="bg"/><feMergeNode in="SourceGraphic"/></feMerge>')
    append("    </filter>")
    append("  </defs>")
    append(
        '  <rect width="100%" height="100%" fill="#FFFFFF"/>'
    )
    append(
        '  <g font-family="system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" '
        'fill="#171717">'
    )

    for index, title_line in enumerate(title_lines):
        append(
            f'    <text x="{width / 2:.1f}" y="{38 + index * 28:.1f}" '
            'text-anchor="middle" font-size="24" font-weight="700">'
            f"{escape(title_line)}</text>"
        )
    reader_start_y = 70.0 + 28.0 * (len(title_lines) - 1)
    for index, reader_line in enumerate(reader_lines):
        append(
            f'    <text x="{width / 2:.1f}" '
            f'y="{reader_start_y + index * 18:.1f}" '
            'text-anchor="middle" font-size="14" fill="#4B4B4B">'
            f"{escape(reader_line)}</text>"
        )

    append(
        f'    <rect x="{plot_left:.1f}" y="{plot_top:.1f}" '
        f'width="{plot_width:.1f}" height="{plot_height:.1f}" '
        'fill="#FAFAFA" stroke="#333333" stroke-width="1.5"/>'
    )
    append(
        f'    <line x1="{plot_left + plot_width / 2:.1f}" y1="{plot_top:.1f}" '
        f'x2="{plot_left + plot_width / 2:.1f}" y2="{plot_bottom:.1f}" '
        'stroke="#8A8A8A" stroke-width="1.2" stroke-dasharray="6 6"/>'
    )
    append(
        f'    <line x1="{plot_left:.1f}" y1="{plot_top + plot_height / 2:.1f}" '
        f'x2="{plot_right:.1f}" y2="{plot_top + plot_height / 2:.1f}" '
        'stroke="#8A8A8A" stroke-width="1.2" stroke-dasharray="6 6"/>'
    )

    for center_x, center_y, label in quadrant_centers:
        append(
            f'    <text x="{center_x:.1f}" y="{center_y:.1f}" '
            'text-anchor="middle" font-size="13" font-weight="650" '
            'fill="#555555">'
            f"{escape(label)}</text>"
        )

    append(
        f'    <text x="{plot_left + plot_width / 2:.1f}" y="{x_axis_y:.1f}" '
        'text-anchor="middle" font-size="16" font-weight="650">'
        f'{escape(metadata["x_axis_label"])}</text>'
    )
    for endpoint_lines, endpoint_x, endpoint_anchor in (
        (x_low_lines, plot_left, "start"),
        (x_high_lines, plot_right, "end"),
    ):
        append(
            f'    <text x="{endpoint_x:.1f}" y="{plot_bottom + 46:.1f}" '
            f'text-anchor="{endpoint_anchor}" font-size="13">'
        )
        for line_index, endpoint_line in enumerate(endpoint_lines):
            append(
                f'      <tspan x="{endpoint_x:.1f}" '
                f'y="{plot_bottom + 46 + line_index * 16:.1f}">'
                f"{escape(endpoint_line)}</tspan>"
            )
        append("    </text>")
    append(
        f'    <text x="0" y="0" '
        f'transform="translate(44 {plot_top + plot_height / 2:.1f}) rotate(-90)" '
        'text-anchor="middle" font-size="16" font-weight="650">'
        f'{escape(metadata["y_axis_label"])}</text>'
    )
    for endpoint_label, endpoint_y in (
        (metadata["y_low_label"], plot_bottom),
        (metadata["y_high_label"], plot_top),
    ):
        endpoint_lines = wrap_display(endpoint_label, 18)
        first_line_y = endpoint_y - (len(endpoint_lines) - 1) * 8
        append(
            f'    <text x="{plot_left - 18:.1f}" y="{first_line_y:.1f}" '
            'text-anchor="end" font-size="13">'
        )
        for line_index, endpoint_line in enumerate(endpoint_lines):
            append(
                f'      <tspan x="{plot_left - 18:.1f}" '
                f'y="{first_line_y + line_index * 16:.1f}">'
                f"{escape(endpoint_line)}</tspan>"
            )
        append("    </text>")

    for work in works:
        point_x, point_y = point_positions[work.work_id]
        placement = placements[work.work_id]
        color, shape = styles[work.category]
        accessible_title = (
            f"{'Current work. ' if work.is_current else ''}{work.label}. "
            f"Category: {work.category}. X: {work.x:g}; Y: {work.y:g}."
        )
        append(
            f'    <g id="work-{escape(work.work_id, quote=True)}" '
            f'aria-label="{escape(accessible_title, quote=True)}">'
        )
        append(f"      <title>{escape(accessible_title)}</title>")
        if work.is_current:
            append(
                f'      <circle cx="{point_x:.1f}" cy="{point_y:.1f}" r="17" '
                'fill="#FFFFFF" stroke="#F4B400" stroke-width="5"/>'
            )
            append(
                f'      <circle cx="{point_x:.1f}" cy="{point_y:.1f}" r="13" '
                'fill="none" stroke="#111111" stroke-width="2.5"/>'
            )
        append(f"      {marker_svg(shape, point_x, point_y, color)}")
        if placement.needs_leader:
            line_end_x = placement.x
            if placement.anchor == "start":
                line_end_x -= 5
            elif placement.anchor == "end":
                line_end_x += 5
            append(
                f'      <line x1="{point_x:.1f}" y1="{point_y:.1f}" '
                f'x2="{line_end_x:.1f}" y2="{placement.y - 5:.1f}" '
                'stroke="#666666" stroke-width="0.9"/>'
            )
        append(
            f'      <text x="{placement.x:.1f}" y="{placement.y:.1f}" '
            f'text-anchor="{placement.anchor}" font-size="13" '
            f'font-weight="{"750" if work.is_current else "550"}" '
            'paint-order="stroke" stroke="#FFFFFF" stroke-width="4" '
            'stroke-linejoin="round">'
            f"{escape(work.label)}</text>"
        )
        append("    </g>")

    for badge_index, (badge_x, badge_y, group) in enumerate(overlap_badges, start=1):
        shared_labels = ", ".join(work.label for work in group)
        badge_title = (
            f"{len(group)} works share this coordinate: {shared_labels}."
        )
        append(
            f'    <g id="overlap-{badge_index}" '
            f'aria-label="{escape(badge_title, quote=True)}">'
        )
        append(f"      <title>{escape(badge_title)}</title>")
        append(
            f'      <circle cx="{badge_x:.1f}" cy="{badge_y:.1f}" r="10" '
            'fill="#FFFFFF" stroke="#111111" stroke-width="1.5"/>'
        )
        append(
            f'      <text x="{badge_x:.1f}" y="{badge_y + 4:.1f}" '
            'text-anchor="middle" font-size="11" font-weight="750">'
            f"{len(group)}</text>"
        )
        append("    </g>")

    legend_x = 958.0
    append(
        f'    <g id="legend" aria-label="Legend" transform="translate({legend_x:.1f} '
        f'{legend_y:.1f})">'
    )
    append(
        '      <text x="0" y="0" font-size="16" font-weight="700">'
        "Related-work categories</text>"
    )
    for category, category_lines, item_y in legend_layout:
        color, shape = styles[category]
        append(f"      {marker_svg(shape, 10, item_y - 5, color, size=7)}")
        append(
            f'      <text x="30" y="{item_y:.1f}" font-size="13">'
        )
        for line_index, category_line in enumerate(category_lines):
            append(
                f'        <tspan x="30" y="{item_y + line_index * 16:.1f}">'
                f"{escape(category_line)}</tspan>"
            )
        append("      </text>")
    append(
        f'      <circle cx="10" cy="{current_y - 5:.1f}" r="12" fill="#FFFFFF" '
        'stroke="#F4B400" stroke-width="4"/>'
    )
    append(
        f'      <circle cx="10" cy="{current_y - 5:.1f}" r="8" fill="none" '
        'stroke="#111111" stroke-width="2"/>'
    )
    append(
        f'      <text x="30" y="{current_y:.1f}" font-size="13" font-weight="700">'
        "Current work</text>"
    )
    legend_note_y = current_y + 42
    if overlap_badges:
        append(
            f'      <circle cx="10" cy="{legend_note_y - 5:.1f}" r="9" '
            'fill="#FFFFFF" stroke="#111111" stroke-width="1.5"/>'
        )
        append(
            f'      <text x="10" y="{legend_note_y - 1:.1f}" '
            'text-anchor="middle" font-size="10" font-weight="750">2</text>'
        )
        append(
            f'      <text x="30" y="{legend_note_y:.1f}" font-size="12">'
            "Numbered badge = shared coordinate</text>"
        )
        legend_note_y += 36
    append(
        f'      <text x="0" y="{legend_note_y:.1f}" font-size="12" fill="#555555">'
        "Color + shape encode category.</text>"
    )
    append("    </g>")

    append(
        f'    <line x1="80" y1="{caption_top - 22:.1f}" '
        f'x2="{width - 80}" y2="{caption_top - 22:.1f}" '
        'stroke="#D0D0D0" stroke-width="1"/>'
    )
    for index, source_line in enumerate(source_lines):
        prefix = "Chart note: " if index == 0 else ""
        append(
            f'    <text x="80" y="{caption_top + index * 20:.1f}" '
            'font-size="12" fill="#4B4B4B">'
            f"{escape(prefix + source_line)}</text>"
        )
    append("  </g>")
    append("</svg>")
    return "\n".join(lines) + "\n"


def aliases_input_file(input_path: Path, output_path: Path) -> bool:
    """Return whether output would overwrite input through a path or inode alias."""

    if input_path.resolve() == output_path.resolve():
        return True
    if not output_path.exists():
        return False
    try:
        return input_path.samefile(output_path)
    except OSError as exc:
        raise ValidationError(
            [f"could not verify that input and output are different files: {exc}"]
        ) from exc


def main() -> int:
    args = parse_args()
    try:
        metadata, works = load_chart(args.input_csv, strict=args.strict)
        if aliases_input_file(args.input_csv, args.output_svg):
            raise ValidationError(
                ["input CSV and output SVG must be different files"]
            )
        svg = render_svg(metadata, works)
        args.output_svg.parent.mkdir(parents=True, exist_ok=True)
        args.output_svg.write_text(svg, encoding="utf-8")
    except ValidationError as exc:
        for issue in exc.issues:
            print(f"ERROR: {issue}", file=sys.stderr)
        print(
            f"FAIL: chart data has {len(exc.issues)} validation error(s)",
            file=sys.stderr,
        )
        return 2
    except OSError as exc:
        print(f"ERROR: could not write SVG: {exc}", file=sys.stderr)
        return 1

    print(
        f"PASS: rendered {len(works)} full-text-declared work(s) "
        f"in {'strict audit' if args.strict else 'communication'} mode "
        f"to {args.output_svg}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
