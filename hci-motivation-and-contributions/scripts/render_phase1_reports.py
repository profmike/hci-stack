#!/usr/bin/env python3
"""Render self-contained Phase 1 HTML reports from durable research artifacts."""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import html
import re
import tempfile
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


REPORT_NAMES = (
    "phase-1-progress.html",
    "literature-and-evidence.html",
    "phase-1-final.html",
)

ARTIFACT_INDEX_NAME = "artifact-index.html"

ARTIFACT_REPORT_SPECS = (
    (
        "phase-1-collaboration-workboard.md",
        "phase-1-collaboration-workboard.html",
        "Phase 1 collaboration workboard",
        "Live phase coverage, constructive opposition, decision state, propagation, and reopen triggers.",
    ),
    (
        "ranked-related-work-positioning.md",
        "ranked-related-work-positioning.html",
        "Ranked related-work positioning",
        "Project-specific relevance ranking and paragraph-level comparisons with the closest work.",
    ),
    (
        "acm-sigchi-related-work-audit.md",
        "acm-sigchi-related-work-audit.html",
        "ACM DL and SIGCHI related-work audit",
        "Native ACM coverage, inclusion decisions, mechanism collisions, and broader-HCI situating.",
    ),
    (
        "related-work-search-recall-audit.md",
        "related-work-search-recall-audit.html",
        "Related-work search-recall audit",
        "Synonym coverage, sentinels, pagination rules, citation-title accountability, and late-find postmortems.",
    ),
    (
        "related-work-matrix.md",
        "related-work-matrix.html",
        "Related-work matrix",
        "Dimension-by-dimension comparison of the retained intervention landscape.",
    ),
    (
        "related-work-contribution-tier-audit.md",
        "related-work-contribution-tier-audit.html",
        "Related-work contribution-strength audit",
        "Prospective contribution boundaries and fallback tiers relative to prior work.",
    ),
    (
        "prior-work-contribution-boundary.md",
        "prior-work-contribution-boundary.html",
        "Prior-work contribution-boundary audit",
        "Human-readable synthesis of collision, attribution, channel, package, port, proposal, silence, and repair boundaries.",
    ),
    (
        "prior-work-evidence-accounting.csv",
        "prior-work-evidence-accounting.html",
        "Prior-work evidence accounting",
        "Six independent fields for claim, demonstration, operation, evaluation, capability collision, and contribution credit.",
    ),
    (
        "idea-provenance-ledger.csv",
        "idea-provenance-ledger.html",
        "Idea and provenance ledger",
        "Proposals, future work, interpretations, and unverified claims held at zero collision and contribution credit.",
    ),
    (
        "imported-bibliography-accountability.csv",
        "imported-bibliography-accountability.html",
        "Imported bibliography accountability",
        "Every supplied citation, independent discovery route, terminal source resolution, and evidence-accounting link.",
    ),
    (
        "late-found-work-postmortem.csv",
        "late-found-work-postmortem.html",
        "Late-found-work postmortems",
        "Missed routes, sibling sweeps, repairs, affected-claim reruns, and sentinel links.",
    ),
    (
        "novelty-regression-sentinels.yaml",
        "novelty-regression-sentinels.html",
        "Novelty regression sentinels",
        "Non-title retrieval tests that protect repaired literature-search routes.",
    ),
    (
        "evidence-strength-register.md",
        "evidence-strength-register.html",
        "Evidence-strength register",
        "Reusable claim-specific ingestion and evidence-strength assessments.",
    ),
    (
        "authoritative-source-map.md",
        "authoritative-source-map.html",
        "Authoritative domain-source map",
        "Claim-to-remit mapping for authoritative bodies, exact document roles, and evidence boundaries.",
    ),
    (
        "consequence-severity-ranking.md",
        "consequence-severity-ranking.html",
        "Consequence severity ranking",
        "Evidence-calibrated ranking of consequences with uncertainty and sensitivity.",
    ),
    (
        "current-practice-audit.md",
        "current-practice-audit.html",
        "Current-practice audit",
        "Dated product and research capabilities, bypasses, and collision boundaries.",
    ),
    (
        "motivation-claim-research-queue.md",
        "motivation-claim-research-queue.html",
        "Motivation-claim research queue",
        "Resolution state for active hypothesis and unsupported motivation claims.",
    ),
    (
        "source-manifest.md",
        "source-manifest.html",
        "Source manifest",
        "Full-copy, provenance, ingestion, and source-selection record.",
    ),
    (
        "source-resolution.csv",
        "source-resolution.html",
        "Source-resolution ledger",
        "Candidate acquisition, review, access, supersession, claim-impact, and reopen state.",
    ),
    (
        "missing-full-copies.md",
        "missing-full-copies.html",
        "Missing full copies",
        "Access barriers, attempted routes, requested author actions, and fallback boundaries.",
    ),
)

ARTIFACT_REPORT_NAMES = tuple(spec[1] for spec in ARTIFACT_REPORT_SPECS)
ALL_REPORT_NAMES = REPORT_NAMES + (ARTIFACT_INDEX_NAME,) + ARTIFACT_REPORT_NAMES

NAVIGATION_ITEMS = (
    ("phase-1-progress.html", "Progress"),
    ("literature-and-evidence.html", "Literature & evidence"),
    ("ranked-related-work-positioning.html", "Ranked related work"),
    ("phase-1-final.html", "Direction"),
    (ARTIFACT_INDEX_NAME, "Artifact shelf"),
)

PHASE1_COMPLETION_STATES = (
    "READY_FOR_PHASE_2",
    "READY_WITH_RISKS",
    "NEEDS_MOTIVATION_EVIDENCE",
    "NEEDS_LANDSCAPE_RESEARCH",
    "RECONSIDER_DIRECTION",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Phase 1 progress, literature/evidence, and final HTML reports."
    )
    parser.add_argument("project_dir", type=Path, help="Research-framing artifact directory")
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Report directory (default: PROJECT_DIR/reports)",
    )
    parser.add_argument("--project-title", help="Display title (default: project folder name)")
    parser.add_argument(
        "--generated-at",
        help="Fixed ISO timestamp for reproducible rendering and tests",
    )
    return parser.parse_args()


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


@dataclass(frozen=True)
class Reference:
    citation_key: str
    author_year: str
    short_title: str
    venue_abbrev: str
    full_title: str
    full_authors: str
    full_venue: str
    url: str
    explicit_aliases: tuple[str, ...]

    @property
    def label(self) -> str:
        match = re.fullmatch(r"(.+),\s*(\d{4}[a-z]?)", self.author_year)
        if not match:
            return f"{self.author_year} ({self.venue_abbrev}): {self.short_title}"
        author, year = match.groups()
        return f"{author} ({year} {self.venue_abbrev}): {self.short_title}"

    @property
    def tooltip(self) -> str:
        return " ".join(
            part.strip().rstrip(".") + "."
            for part in (self.full_authors, self.full_title, self.full_venue)
            if part.strip()
        )

    @property
    def anchor(self) -> str:
        return "ref-" + re.sub(r"[^a-z0-9]+", "-", self.citation_key.lower()).strip("-")

    def aliases(self) -> set[str]:
        aliases = {
            self.citation_key,
            self.author_year,
            self.author_year.replace(",", ""),
            self.author_year.replace(", ", " "),
            self.short_title,
            *self.explicit_aliases,
        }
        match = re.fullmatch(r"(.+),\s*(\d{4}[a-z]?)", self.author_year)
        if match:
            author, year = match.groups()
            aliases.update(
                {
                    f"{author} ({year})",
                    f"{author} ({self.venue_abbrev} {year})",
                    f"{author} ({year} {self.venue_abbrev})",
                    f"{author} ({self.venue_abbrev}, {year})",
                    f"{author}, {self.venue_abbrev} {year}",
                    f"{author} {self.venue_abbrev} {year}",
                }
            )
        return {re.sub(r"\s+", " ", alias).strip() for alias in aliases if alias.strip()}

    @property
    def first_author_surname(self) -> str | None:
        match = re.fullmatch(r"(.+),\s*(\d{4}[a-z]?)", self.author_year)
        if not match:
            return None
        author = match.group(1)
        multiple_authors = re.fullmatch(r"(.+?)\s+et al\.", author)
        if not multiple_authors:
            return None
        return multiple_authors.group(1).split()[-1]


class CitationCatalog:
    def __init__(self, references: list[Reference]):
        self.references = references
        key_map: dict[str, Reference] = {}
        for reference in references:
            existing = key_map.get(reference.citation_key)
            if existing is not None:
                raise ValueError(
                    f"Duplicate citation key '{reference.citation_key}' in references.csv"
                )
            key_map[reference.citation_key] = reference
        self.key_map = key_map

        surname_counts = Counter(
            reference.first_author_surname
            for reference in references
            if reference.first_author_surname
        )
        alias_map: dict[str, Reference] = {}
        for reference in references:
            aliases = set(reference.aliases())
            surname = reference.first_author_surname
            if surname and surname_counts[surname] == 1:
                aliases.add(surname)
            for alias in aliases:
                escaped_alias = html.escape(alias)
                existing = alias_map.get(escaped_alias)
                if existing is not None and existing.citation_key != reference.citation_key:
                    raise ValueError(
                        "Ambiguous citation alias "
                        f"'{alias}' maps to both '{existing.citation_key}' and "
                        f"'{reference.citation_key}'. Use explicit [@CitationKey] tokens."
                    )
                alias_map[escaped_alias] = reference
        self.alias_map = alias_map
        if alias_map:
            alternatives = sorted(alias_map, key=len, reverse=True)
            self.pattern = re.compile(
                r"(?<![\w/:])("
                + "|".join(re.escape(alias) for alias in alternatives)
                + r")(?![\w/])"
            )
        else:
            self.pattern = None
        self.token_pattern = re.compile(r"\[@([^\[\]]+)\]")

    def enrich(self, escaped: str) -> str:
        output: list[str] = []
        cursor = 0
        for token in self.token_pattern.finditer(escaped):
            output.append(self._enrich_aliases(escaped[cursor : token.start()]))
            key = html.unescape(token.group(1)).strip()
            reference = self.key_map.get(key)
            if reference is None:
                raise ValueError(
                    f"Unknown citation key '{key}' in explicit token [@{key}]"
                )
            output.append(self._link(reference))
            cursor = token.end()
        output.append(self._enrich_aliases(escaped[cursor:]))
        return "".join(output)

    def _enrich_aliases(self, escaped: str) -> str:
        if self.pattern is None:
            return escaped

        def replace(match: re.Match[str]) -> str:
            return self._link(self.alias_map[match.group(1)])

        return self.pattern.sub(replace, escaped)

    @staticmethod
    def _link(reference: Reference) -> str:
        external = reference.url.startswith(("http://", "https://"))
        href = reference.url if external else f"literature-and-evidence.html#{reference.anchor}"
        target = ' target="_blank" rel="noopener noreferrer"' if external else ""
        return (
            f'<a class="citation" href="{html.escape(href, quote=True)}"{target} '
            f'title="{html.escape(reference.tooltip, quote=True)}" '
            f'aria-label="{html.escape(reference.tooltip, quote=True)}">'
            f"{html.escape(reference.label)}</a>"
        )


def load_citation_catalog(root: Path) -> CitationCatalog:
    path = root / "references.csv"
    if not path.is_file():
        return CitationCatalog([])
    references: list[Reference] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            aliases = tuple(
                alias.strip()
                for alias in (row.get("aliases") or "").split("||")
                if alias.strip()
            )
            references.append(
                Reference(
                    citation_key=(row.get("citation_key") or "").strip(),
                    author_year=(row.get("author_year") or "").strip(),
                    short_title=(row.get("short_title") or "").strip(),
                    venue_abbrev=(row.get("venue_abbrev") or "").strip(),
                    full_title=(row.get("full_title") or "").strip(),
                    full_authors=(row.get("full_authors") or "").strip(),
                    full_venue=(row.get("full_venue") or "").strip(),
                    url=(row.get("url") or "").strip(),
                    explicit_aliases=aliases,
                )
            )
    return CitationCatalog([reference for reference in references if reference.citation_key])


def inline_format(value: str, catalog: CitationCatalog | None = None) -> str:
    escaped = html.escape(value.strip())
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    if catalog is not None:
        escaped = catalog.enrich(escaped)
    return escaped


def split_table_row(line: str) -> list[str]:
    content = line.strip()
    if content.startswith("|"):
        content = content[1:]
    if content.endswith("|") and not content.endswith(r"\|"):
        content = content[:-1]
    cells: list[str] = []
    current: list[str] = []
    index = 0
    while index < len(content):
        character = content[index]
        if character == "\\" and index + 1 < len(content):
            following = content[index + 1]
            if following in {"|", "\\"}:
                current.append(following)
                index += 2
                continue
        if character == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)
        index += 1
    cells.append("".join(current).strip())
    return cells


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def markdown_to_html(markdown: str, catalog: CitationCatalog | None = None) -> str:
    """Render a conservative Markdown subset after escaping all artifact content."""
    lines = markdown.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            index += 1
            continue

        if stripped.startswith("```"):
            language = stripped[3:].strip()
            code_lines: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(lines[index])
                index += 1
            index += 1
            class_name = f' class="language-{html.escape(language, quote=True)}"' if language else ""
            output.append(
                f"<pre><code{class_name}>{html.escape(chr(10).join(code_lines))}</code></pre>"
            )
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            level = len(heading.group(1))
            output.append(f"<h{level}>{inline_format(heading.group(2), catalog)}</h{level}>")
            index += 1
            continue

        if (
            stripped.startswith("|")
            and index + 1 < len(lines)
            and is_table_separator(lines[index + 1])
        ):
            table_line = index + 1
            headers = split_table_row(line)
            separators = split_table_row(lines[index + 1])
            if len(separators) != len(headers):
                raise ValueError(
                    f"Markdown table at line {table_line} has {len(headers)} header "
                    f"cell(s) but {len(separators)} separator cell(s). Escape literal pipes "
                    r"as \|."
                )
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                row = split_table_row(lines[index])
                if len(row) != len(headers):
                    raise ValueError(
                        f"Markdown table row at line {index + 1} has {len(row)} cell(s); "
                        f"expected {len(headers)}. Escape literal pipes as \\|."
                    )
                rows.append(row)
                index += 1
            output.append("<div class=\"table-wrap\"><table><thead><tr>")
            output.extend(f"<th>{inline_format(cell, catalog)}</th>" for cell in headers)
            output.append("</tr></thead><tbody>")
            for row in rows:
                output.append("<tr>")
                output.extend(
                    f"<td>{inline_format(cell, catalog)}</td>"
                    for cell in row
                )
                output.append("</tr>")
            output.append("</tbody></table></div>")
            continue

        list_match = re.match(r"^([-*+]|\d+\.)\s+(.+)$", stripped)
        if list_match:
            ordered = list_match.group(1).endswith(".")
            tag = "ol" if ordered else "ul"
            items: list[str] = []
            while index < len(lines):
                match = re.match(r"^([-*+]|\d+\.)\s+(.+)$", lines[index].strip())
                if not match or match.group(1).endswith(".") != ordered:
                    break
                item_parts = [match.group(2)]
                index += 1
                while index < len(lines):
                    continuation = lines[index]
                    if not continuation.strip():
                        break
                    if re.match(r"^([-*+]|\d+\.)\s+", continuation.strip()):
                        break
                    if continuation[:1].isspace():
                        item_parts.append(continuation.strip())
                        index += 1
                        continue
                    break
                items.append(" ".join(item_parts))
            output.append(f"<{tag}>")
            output.extend(f"<li>{inline_format(item, catalog)}</li>" for item in items)
            output.append(f"</{tag}>")
            continue

        if stripped.startswith(">"):
            quotes: list[str] = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quotes.append(lines[index].strip().lstrip(">").strip())
                index += 1
            output.append(
                f"<blockquote>{inline_format(' '.join(quotes), catalog)}</blockquote>"
            )
            continue

        paragraph = [stripped]
        index += 1
        while index < len(lines):
            candidate = lines[index].strip()
            if (
                not candidate
                or candidate.startswith(("#", "```", "|", ">"))
                or re.match(r"^([-*+]|\d+\.)\s+", candidate)
            ):
                break
            paragraph.append(candidate)
            index += 1
        output.append(f"<p>{inline_format(' '.join(paragraph), catalog)}</p>")

    return "\n".join(output)


def csv_to_html(path: Path, catalog: CitationCatalog | None = None) -> str:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return '<p class="missing">The CSV contains no rows.</p>'
    headers, body = rows[0], rows[1:]
    parts = ['<div class="table-wrap"><table><thead><tr>']
    parts.extend(f"<th>{inline_format(cell, catalog)}</th>" for cell in headers)
    parts.append("</tr></thead><tbody>")
    for row in body:
        padded = row + [""] * max(0, len(headers) - len(row))
        parts.append("<tr>")
        parts.extend(
            f"<td>{inline_format(cell, catalog)}</td>" for cell in padded[: len(headers)]
        )
        parts.append("</tr>")
    parts.append("</tbody></table></div>")
    return "".join(parts)


def artifact_card(
    path: Path,
    root: Path,
    catalog: CitationCatalog,
    *,
    open_by_default: bool = False,
) -> str:
    relative = path.relative_to(root).as_posix()
    if not path.is_file():
        return (
            '<article class="artifact missing-card">'
            f"<h3>{html.escape(relative)}</h3>"
            '<p class="missing">Artifact not available yet.</p></article>'
        )
    content = csv_to_html(path, catalog) if path.suffix.lower() == ".csv" else markdown_to_html(
        path.read_text(encoding="utf-8", errors="replace"), catalog
    )
    opened = " open" if open_by_default else ""
    return (
        '<article class="artifact">'
        f"<details{opened}><summary><span>{html.escape(relative)}</span>"
        f'<small>SHA-256 {digest(path)[:12]}</small></summary>'
        f'<div class="artifact-content">{content}</div></details></article>'
    )


def unique_paths(paths: list[Path]) -> list[Path]:
    seen: set[Path] = set()
    result: list[Path] = []
    for path in paths:
        normalized = path.resolve()
        if normalized not in seen:
            seen.add(normalized)
            result.append(path)
    return result


def phase1_completion_state(root: Path) -> str | None:
    """Return an explicit canonical readiness decision, never infer completion."""
    for path in (
        root / "STATUS.md",
        root / "research-framing-outline.md",
        root / "author-decisions.md",
    ):
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        for state in PHASE1_COMPLETION_STATES:
            if re.search(rf"(?<![A-Z0-9_]){re.escape(state)}(?![A-Z0-9_])", content, re.I):
                return state
    return None


def option_paths(root: Path) -> list[Path]:
    candidates: list[Path] = []
    packet_dir = root / "decision-packets"
    if packet_dir.is_dir():
        candidates.extend(sorted(packet_dir.rglob("*.md")))
    candidates.extend(sorted(root.glob("*-options.md")))
    candidates.extend(sorted(root.glob("*decision-packet*.md")))
    candidates.extend(sorted(root.glob("*proposal*.md")))
    candidates.extend(
        [
            root / "approach-options.md",
            root / "contribution-options.md",
            root / "related-work-quadrant-variations.md",
        ]
    )
    return unique_paths([path for path in candidates if path.is_file()])


def review_paths(root: Path) -> list[Path]:
    candidates = [
        root / "reviewer-audit.md",
        root / "reviewer-panel" / "synthesis.md",
    ]
    dated_reviews = root / "reviews"
    if dated_reviews.is_dir():
        candidates.extend(sorted(dated_reviews.rglob("synthesis.md")))
        candidates.extend(sorted(dated_reviews.rglob("*positioning*.md")))
        candidates.extend(sorted(dated_reviews.rglob("*terminology*.md")))
        candidates.extend(sorted(dated_reviews.rglob("*inference*.md")))
    return unique_paths([path for path in candidates if path.is_file()])


def artifact_section(
    title: str,
    paths: list[Path],
    root: Path,
    catalog: CitationCatalog,
    *,
    description: str = "",
    open_first: bool = False,
    empty_message: str = "No artifacts are available for this section yet.",
) -> tuple[str, list[Path]]:
    existing = [path for path in unique_paths(paths) if path.is_file()]
    intro = f"<p>{html.escape(description)}</p>" if description else ""
    if not existing:
        body = f'<p class="missing">{html.escape(empty_message)}</p>'
    else:
        body = "".join(
            artifact_card(
                path,
                root,
                catalog,
                open_by_default=open_first and index == 0,
            )
            for index, path in enumerate(existing)
        )
    return f"<section><h2>{html.escape(title)}</h2>{intro}{body}</section>", existing


def quadrant_gallery(root: Path) -> tuple[str, list[Path]]:
    svgs = sorted((root / "quadrants").glob("*.svg")) if (root / "quadrants").is_dir() else []
    if not svgs:
        return (
            '<section><h2>Positioning-chart variations</h2>'
            '<p class="missing">No rendered quadrant variations are available yet.</p></section>',
            [],
        )
    cards: list[str] = []
    for path in svgs:
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        cards.append(
            '<figure class="chart-card">'
            f'<img src="data:image/svg+xml;base64,{encoded}" '
            f'alt="{html.escape(path.stem, quote=True)}">'
            f"<figcaption>{html.escape(path.name)}</figcaption></figure>"
        )
    return (
        '<section><h2>Positioning-chart variations</h2>'
        f'<div class="chart-grid">{"".join(cards)}</div></section>',
        svgs,
    )


def ledger_metrics(root: Path) -> str:
    path = root / "claim-evidence-ledger.csv"
    if not path.is_file():
        return '<p class="missing">No claim-evidence ledger is available yet.</p>'
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        rows = list(reader)
    states = Counter(
        (row.get("evidence_state") or "unspecified").strip() for row in rows
    )
    statuses = Counter((row.get("status") or "unspecified").strip() for row in rows)
    metrics = [
        ("Claims", str(len(rows))),
        ("Verified", str(statuses.get("verified", 0))),
        ("Candidate", str(statuses.get("candidate", 0))),
        ("Unsupported", str(states.get("unsupported", 0))),
    ]
    cards = "".join(
        f'<div class="metric"><strong>{html.escape(value)}</strong>'
        f"<span>{html.escape(label)}</span></div>"
        for label, value in metrics
    )
    if "evidence_state" not in columns:
        return (
            f'<div class="metrics">{cards}</div>'
            '<p class="missing">This legacy claim ledger does not record '
            '<code>evidence_state</code>. Migrate it to the current template before treating '
            "the evidence-state summary as complete.</p>"
        )
    state_rows = "".join(
        f"<tr><td>{html.escape(state)}</td><td>{count}</td></tr>"
        for state, count in sorted(states.items())
    )
    return (
        f'<div class="metrics">{cards}</div>'
        '<div class="table-wrap"><table><thead><tr><th>Evidence state</th>'
        f"<th>Claims</th></tr></thead><tbody>{state_rows}</tbody></table></div>"
    )


def reference_catalog_html(catalog: CitationCatalog) -> str:
    if not catalog.references:
        return (
            '<section><h2>Reference catalog</h2>'
            '<p class="missing">No references.csv citation catalog is available yet. '
            "Citation links and hover metadata cannot be audited.</p></section>"
        )
    cards: list[str] = []
    for reference in catalog.references:
        external = reference.url.startswith(("http://", "https://"))
        title = html.escape(reference.full_title)
        if external:
            title = (
                f'<a href="{html.escape(reference.url, quote=True)}" target="_blank" '
                f'rel="noopener noreferrer">{title}</a>'
            )
        cards.append(
            f'<article class="reference-card" id="{reference.anchor}">'
            f"<h3>{html.escape(reference.label)}</h3>"
            f"<p><strong>{title}</strong></p>"
            f"<p>{html.escape(reference.full_authors)}</p>"
            f'<p class="venue">{html.escape(reference.full_venue)}</p>'
            f"<p><code>{html.escape(reference.citation_key)}</code></p></article>"
        )
    return (
        '<section><h2>Reference catalog</h2>'
        "<p>Hover any enriched citation elsewhere in the reports for the complete authors, "
        "title, and venue. Select it to open the canonical source when available.</p>"
        f'<div class="reference-grid">{"".join(cards)}</div></section>'
    )


def artifact_shelf_html(root: Path, *, compact: bool = False) -> str:
    cards: list[str] = []
    specs = ARTIFACT_REPORT_SPECS[:7] if compact else ARTIFACT_REPORT_SPECS
    for source_name, report_name, title, description in specs:
        source = root / source_name
        state = "Available" if source.is_file() else "Source artifact not available yet"
        state_class = "" if source.is_file() else ' class="missing"'
        cards.append(
            '<article class="reference-card">'
            f'<h3><a href="{html.escape(report_name, quote=True)}">'
            f"{html.escape(title)}</a></h3>"
            f"<p>{html.escape(description)}</p>"
            f"<p{state_class}>{html.escape(state)}</p></article>"
        )
    more = (
        f'<p><a href="{ARTIFACT_INDEX_NAME}">Open the complete artifact shelf</a>.</p>'
        if compact
        else ""
    )
    return (
        "<section><h2>Reader-facing artifact pages</h2>"
        "<p>Markdown and CSV remain the editable, diffable sources of truth. These generated "
        "HTML mirrors make the audits, registers, matrices, and positioning prose directly "
        "readable and shareable; edit the source artifact, then regenerate.</p>"
        f'<div class="reference-grid">{"".join(cards)}</div>{more}</section>'
    )


def inventory(paths: list[Path], root: Path) -> str:
    rows: list[str] = []
    for path in unique_paths([path for path in paths if path.is_file()]):
        stat = path.stat()
        modified = datetime.fromtimestamp(stat.st_mtime).astimezone().isoformat(
            timespec="seconds"
        )
        rows.append(
            "<tr>"
            f"<td><code>{html.escape(path.relative_to(root).as_posix())}</code></td>"
            f"<td>{html.escape(modified)}</td>"
            f"<td><code>{digest(path)}</code></td>"
            "</tr>"
        )
    if not rows:
        return '<p class="missing">No source artifacts were included.</p>'
    return (
        '<div class="table-wrap"><table><thead><tr><th>Artifact</th><th>Modified</th>'
        f"<th>SHA-256</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>"
    )


CSS = """
:root{--ink:#17202a;--muted:#5f6b76;--line:#d9e1e8;--paper:#fff;--wash:#f3f7fa;
--accent:#0b6e75;--accent2:#d97706;--danger:#a33a2b}
*{box-sizing:border-box}body{margin:0;background:var(--wash);color:var(--ink);
font:15px/1.55 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
a{color:var(--accent)}header.hero{padding:42px max(24px,calc((100vw - 1160px)/2));
background:linear-gradient(130deg,#073b4c,#0b6e75);color:#fff}
header.hero h1{margin:0 0 8px;font-size:clamp(28px,5vw,48px);line-height:1.08}
header.hero p{max-width:850px;margin:8px 0;color:#d9f1ef}.eyebrow{text-transform:uppercase;
letter-spacing:.13em;font-size:12px;font-weight:750}.meta{display:flex;gap:10px;flex-wrap:wrap;
margin-top:18px}.pill{border:1px solid #ffffff55;border-radius:99px;padding:5px 10px}
nav{position:sticky;top:0;z-index:3;background:#fffffff2;backdrop-filter:blur(10px);
border-bottom:1px solid var(--line);padding:10px max(24px,calc((100vw - 1160px)/2))}
nav a{display:inline-block;margin-right:18px;font-weight:700;text-decoration:none}
main{max-width:1160px;margin:0 auto;padding:24px}section{margin:0 0 26px;background:var(--paper);
border:1px solid var(--line);border-radius:16px;padding:22px;box-shadow:0 6px 24px #1b34420a}
h2{margin-top:0;font-size:23px}h3{margin:22px 0 8px}p{max-width:90ch}
.artifact{border-top:1px solid var(--line)}.artifact:first-of-type{border-top:0}
details summary{display:flex;justify-content:space-between;gap:12px;cursor:pointer;padding:14px 0;
font-weight:750}summary small{color:var(--muted);font-weight:500}.artifact-content{padding:0 0 18px}
.missing{color:var(--danger);font-weight:650}.missing-card{padding:12px 0}
.table-wrap{overflow:auto;margin:12px 0}table{border-collapse:collapse;width:100%;font-size:13px}
th,td{border:1px solid var(--line);padding:8px 9px;text-align:left;vertical-align:top}
th{background:#eaf2f4;position:sticky;top:0}code{background:#edf2f5;border-radius:4px;padding:1px 4px}
pre{overflow:auto;background:#101820;color:#eef7f7;padding:14px;border-radius:10px}
blockquote{border-left:4px solid var(--accent2);margin:14px 0;padding:5px 16px;color:var(--muted)}
.metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:14px 0}
.metric{border:1px solid var(--line);border-radius:12px;padding:14px;background:#f9fbfc}
.metric strong{display:block;font-size:28px;color:var(--accent)}.metric span{color:var(--muted)}
.chart-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
.chart-card{margin:0;border:1px solid var(--line);border-radius:12px;padding:10px}
.chart-card img{width:100%;height:auto}.chart-card figcaption{font-weight:700;padding:6px}
.citation{display:inline;border-bottom:1px dotted currentColor;text-decoration:none;font-weight:650}
.citation:hover,.citation:focus{background:#dff3f1;outline:2px solid transparent}
.reference-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
.reference-card{border:1px solid var(--line);border-radius:12px;padding:14px;background:#f9fbfc}
.reference-card h3{margin:0 0 8px;font-size:16px}.reference-card p{margin:6px 0}
.reference-card .venue{color:var(--muted)}
footer{max-width:1160px;margin:0 auto;padding:0 24px 40px;color:var(--muted)}
@media print{nav{display:none}body{background:#fff}section{break-inside:avoid;box-shadow:none}}
"""


def page(
    *,
    title: str,
    project_title: str,
    subtitle: str,
    generated_at: str,
    body: str,
    artifact_paths: list[Path],
    root: Path,
) -> str:
    navigation = " ".join(
        f'<a href="{name}">{label}</a>' for name, label in NAVIGATION_ITEMS
    )
    inventory_html = inventory(artifact_paths, root)
    return f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(project_title)} — {html.escape(title)}</title><style>{CSS}</style></head>
<body>
<header class="hero"><div class="eyebrow">HCI motivation and contributions · Phase 1</div>
<h1>{html.escape(title)}</h1><p>{html.escape(subtitle)}</p>
<div class="meta"><span class="pill">{html.escape(project_title)}</span>
<span class="pill">Generated {html.escape(generated_at)}</span></div></header>
<nav aria-label="Report navigation">{navigation}</nav>
<main>{body}<section><h2>Artifact inventory</h2>
<p>Paths are relative to the research-framing folder. Hashes make this report auditable.</p>
{inventory_html}</section></main>
<footer>Generated from durable project artifacts. The HTML report is a view, not the source of truth.</footer>
</body></html>"""


def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    temporary.replace(path)


def generate_reports(
    root: Path,
    output_dir: Path,
    *,
    project_title: str,
    generated_at: str,
) -> list[Path]:
    root = root.resolve()
    output_dir = output_dir.resolve()
    if not root.is_dir():
        raise ValueError(f"project directory not found: {root}")

    catalog = load_citation_catalog(root)
    completion_state = phase1_completion_state(root)
    catalog_path = root / "references.csv"
    options = option_paths(root)
    reviews = review_paths(root)
    workboard = [root / "phase-1-collaboration-workboard.md"]
    choices = [root / "author-decisions.md"]
    framing = [
        root / "starting-state.md",
        root / "terminology-contract.md",
        root / "prior-work-contribution-boundary.md",
        root / "motivation-claim-research-queue.md",
        root / "motivation-evidence-map.md",
        root / "authoritative-source-map.md",
        root / "current-practice-audit.md",
        root / "consequence-severity-ranking.md",
        root / "evidence-strength-register.md",
        root / "acm-sigchi-related-work-audit.md",
        root / "related-work-search-recall-audit.md",
        root / "related-work-matrix.md",
        root / "related-work-contribution-tier-audit.md",
        root / "ranked-related-work-positioning.md",
    ]
    risks = reviews + [root / "missing-full-copies.md"]
    exemplars = [
        root / "exemplar-analysis.md",
        root / "four-paper-exemplar-style-analysis.md",
        root / "exemplar-related-work-positioning-analysis.md",
    ]

    progress_sections: list[str] = []
    progress_paths: list[Path] = []
    for section_args in (
        (
            "Live collaboration workboard",
            workboard,
            "Current coverage, decision readiness, constructive opposition, blockers, and next author question.",
            True,
        ),
        (
            "Current framing",
            framing,
            "The current problem and evidence state; conclusions remain revisable.",
            True,
        ),
        (
            "Author choices",
            choices,
            "Selections, combinations, rejections, delegations, and decisions still pending.",
            True,
        ),
        (
            "Variations presented",
            options,
            "Complete option portfolios are retained even after a choice is made.",
            False,
        ),
        (
            "Review findings and open risks",
            risks,
            "Phase-aware critiques and unresolved evidence or access problems.",
            False,
        ),
        (
            "Exemplar transfer",
            exemplars,
            "Patterns learned from full exemplar papers, separated from project evidence.",
            False,
        ),
    ):
        rendered, included = artifact_section(
            section_args[0],
            section_args[1],
            root,
            catalog,
            description=section_args[2],
            open_first=section_args[3],
        )
        progress_sections.append(rendered)
        progress_paths.extend(included)
    gallery, gallery_paths = quadrant_gallery(root)
    progress_sections.append(gallery)
    progress_paths.extend(gallery_paths)
    if catalog_path.is_file():
        progress_paths.append(catalog_path)

    literature_paths = [
        root / "source-manifest.md",
        root / "source-resolution.csv",
        root / "search-log.md",
        root / "claim-evidence-ledger.csv",
        root / "claim-evidence-ledger-post-review.csv",
        root / "motivation-claim-research-queue.md",
        root / "motivation-evidence-map.md",
        root / "authoritative-source-map.md",
        root / "current-practice-audit.md",
        root / "consequence-severity-ranking.md",
        root / "evidence-strength-register.md",
        root / "acm-sigchi-related-work-audit.md",
        root / "related-work-search-recall-audit.md",
        root / "related-work-matrix.md",
        root / "related-work-contribution-tier-audit.md",
        root / "ranked-related-work-positioning.md",
        root / "prior-work-contribution-boundary.md",
        root / "citation-chain-log.md",
        root / "missing-full-copies.md",
        root / "reference-provenance-audit.md",
        root / "reference-provenance-audit.csv",
        root / "post-review-source-addendum.md",
        root / "exemplar-analysis.md",
        root / "four-paper-exemplar-style-analysis.md",
        root / "exemplar-related-work-positioning-analysis.md",
    ]
    literature_section, included_literature = artifact_section(
        "Reference and evidence record",
        literature_paths,
        root,
        catalog,
        description=(
            "Full-copy status, discovery provenance, cached claim-level evidence strength, "
            "methods, findings, uncertainty, limitations, related-work synthesis, and "
            "citation chains."
        ),
        open_first=True,
    )
    literature_body = (
        f"<section><h2>Evidence coverage</h2>{ledger_metrics(root)}</section>"
        + reference_catalog_html(catalog)
        + artifact_shelf_html(root, compact=True)
        + literature_section
    )
    if catalog_path.is_file():
        included_literature.append(catalog_path)

    outline_paths = [root / "research-framing-outline.md"]
    if not outline_paths[0].is_file():
        outline_paths.extend(
            [
                root / "STATUS.md",
                root / "outline-hourglass.md",
                root / "outline.md",
            ]
        )
    final_paths = (
        [root / "phase-1-collaboration-workboard.md"]
        + outline_paths
        + [
            root / "terminology-contract.md",
            root / "motivation-claim-research-queue.md",
            root / "authoritative-source-map.md",
            root / "current-practice-audit.md",
            root / "consequence-severity-ranking.md",
            root / "evidence-strength-register.md",
            root / "acm-sigchi-related-work-audit.md",
            root / "related-work-search-recall-audit.md",
            root / "ranked-related-work-positioning.md",
            root / "prior-work-contribution-boundary.md",
            root / "author-decisions.md",
        ]
        + reviews
        + [root / "phase-2-handoff.md"]
    )
    final_core_title = (
        "Selected research direction" if completion_state else "Working research direction"
    )
    final_core_description = (
        "The selected framing, evidence boundaries, review disposition, readiness, "
        "and optional Phase 2 handoff."
        if completion_state
        else
        "Candidate framing and evidence boundaries. Author gates and a Phase 1 readiness "
        "decision remain pending."
    )
    final_core, included_final = artifact_section(
        final_core_title,
        final_paths,
        root,
        catalog,
        description=final_core_description,
        open_first=True,
    )
    final_options, included_final_options = artifact_section(
        "Alternatives considered and user choices",
        options,
        root,
        catalog,
        description=(
            "Unselected and superseded alternatives remain visible so later phases can "
            "understand and, when evidence changes, reopen the decision."
        ),
    )
    final_gallery, final_gallery_paths = quadrant_gallery(root)
    final_body = final_core + final_options + final_gallery
    final_inventory = included_final + included_final_options + final_gallery_paths
    if catalog_path.is_file():
        final_inventory.append(catalog_path)

    final_title = (
        "Phase 1 final research direction"
        if completion_state
        else "Phase 1 research direction — working draft"
    )
    final_subtitle = (
        "Decision-complete outline with evidence boundaries, alternatives, and next-phase handoff."
        if completion_state
        else
        "Current candidate outline; this is not a completion or readiness decision."
    )
    reports = [
        (
            "phase-1-progress.html",
            "Phase 1 progress",
            "Live collaboration record: evidence, variations, author choices, and unresolved work.",
            "".join(progress_sections),
            progress_paths,
        ),
        (
            "literature-and-evidence.html",
            "Literature and evidence",
            "Auditable reference, search, provenance, full-copy, and claim-support record.",
            literature_body,
            included_literature,
        ),
        (
            "phase-1-final.html",
            final_title,
            final_subtitle,
            final_body,
            final_inventory,
        ),
    ]
    written: list[Path] = []
    for filename, title, subtitle, body, included in reports:
        destination = output_dir / filename
        write_atomic(
            destination,
            page(
                title=title,
                project_title=project_title,
                subtitle=subtitle,
                generated_at=generated_at,
                body=body,
                artifact_paths=included,
                root=root,
            ),
        )
        written.append(destination)

    artifact_index = output_dir / ARTIFACT_INDEX_NAME
    write_atomic(
        artifact_index,
        page(
            title="Research artifact shelf",
            project_title=project_title,
            subtitle=(
                "Standalone HTML mirrors of the working audits, registers, matrices, and "
                "positioning dossier."
            ),
            generated_at=generated_at,
            body=artifact_shelf_html(root),
            artifact_paths=[
                root / source_name
                for source_name, _, _, _ in ARTIFACT_REPORT_SPECS
                if (root / source_name).is_file()
            ]
            + ([catalog_path] if catalog_path.is_file() else []),
            root=root,
        ),
    )
    written.append(artifact_index)

    for source_name, report_name, title, subtitle in ARTIFACT_REPORT_SPECS:
        source = root / source_name
        if source.is_file():
            content = (
                csv_to_html(source, catalog)
                if source.suffix.lower() == ".csv"
                else markdown_to_html(
                    source.read_text(encoding="utf-8", errors="replace"),
                    catalog,
                )
            )
            body = (
                "<section><h2>Source artifact</h2>"
                f'<p><code>{html.escape(source_name)}</code> · '
                f"SHA-256 <code>{digest(source)}</code></p>{content}</section>"
            )
            included = [source]
        else:
            body = (
                "<section><h2>Source artifact</h2>"
                f'<p class="missing"><code>{html.escape(source_name)}</code> is not '
                "available yet. This page is retained so the report shelf does not silently "
                "hide missing work.</p></section>"
            )
            included = []
        if catalog_path.is_file():
            included.append(catalog_path)
        destination = output_dir / report_name
        write_atomic(
            destination,
            page(
                title=title,
                project_title=project_title,
                subtitle=subtitle,
                generated_at=generated_at,
                body=body,
                artifact_paths=included,
                root=root,
            ),
        )
        written.append(destination)
    return written


def main() -> int:
    args = parse_args()
    root = args.project_dir.resolve()
    output_dir = (args.output_dir or root / "reports").resolve()
    generated_at = args.generated_at or datetime.now().astimezone().isoformat(
        timespec="seconds"
    )
    project_title = args.project_title or root.name.replace("-", " ").title()
    try:
        written = generate_reports(
            root,
            output_dir,
            project_title=project_title,
            generated_at=generated_at,
        )
    except (OSError, ValueError, csv.Error) as exc:
        print(f"ERROR: {exc}")
        return 1
    for path in written:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
