#!/usr/bin/env python3
"""Regenerate the ledger-derived columns of the source manifest table.

Every identifier an author acts on used to exist twice: once in ``source-resolution.csv``
and once, retyped by hand, in ``source-manifest.md``. Nothing kept the two copies equal, so
a correction made in the ledger never reached the page the author reads, and a
mistranscription made on the page was never contradicted by the ledger. Wrong DOIs reached
an author that way and cost real library trips.

This script removes the duplicate. Seven columns of the manifest table are now *derived*:
the script rewrites them from the ledger every time it runs. The remaining columns are
manifest-only judgements that no ledger holds, and the script preserves them untouched.

``check_source_resolution.py`` runs the same derivation in memory and fails when a rendered
cell disagrees, so the page cannot drift again between runs.

The citation publisher may replace a catalog-backed bibliographic shorthand with its deterministic
keyed-link form. The renderer accepts that published form as equivalent while continuing to reject
any changed key, label, or trailing bibliographic text.

Usage:
    python3 render_source_manifest.py PROJECT_DIR [--check]

``--check`` reports what would change and exits non-zero instead of writing.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from pathlib import Path
from urllib.parse import quote

MANIFEST_NAME = "source-manifest.md"
LEDGER_NAME = "source-resolution.csv"
CATALOG_NAME = "references.csv"

# Column header -> how that cell is built from a ledger row. A column absent from this map
# is a manifest-only judgement and is never touched.
DERIVED_HEADERS = (
    "Source ID",
    "Citation key",
    "Bibliographic identity",
    "DOI/canonical URL",
    "Canonical repository location",
    "Source-resolution state/locator",
    "Claim-matched upgrade search / stronger source",
    "Author-access request surfaced date/locator",
)


def join_parts(*parts: str) -> str:
    """Join the non-empty parts of a composite cell with an em dash."""
    kept = [part.strip() for part in parts if part and part.strip()]
    return " — ".join(kept)


def linked_locator(value: str, project_dir: Path) -> str:
    """Make a real external URL or existing project-relative locator clickable."""
    value = (value or "").strip()
    if not value:
        return ""
    if value.startswith(("https://", "http://")):
        return f"[{value}](<{value}>)"
    path_part, separator, fragment = value.partition("#")
    if not path_part or Path(path_part).is_absolute():
        return value
    destination = project_dir / path_part
    if not destination.exists():
        return value
    target = quote(path_part, safe="/._~-")
    if separator:
        target += "#" + quote(fragment, safe="._~-")
    return f"[{value}](<{target}>)"


def derive(header: str, row: dict[str, str], project_dir: Path) -> str:
    """Return the ledger-derived text for one manifest cell."""
    if header == "Source ID":
        return row.get("source_id", "")
    if header == "Citation key":
        return row.get("citation_key", "")
    if header == "Bibliographic identity":
        return row.get("bibliographic_identity", "")
    if header == "DOI/canonical URL":
        return linked_locator(row.get("canonical_url", ""), project_dir)
    if header == "Canonical repository location":
        return linked_locator(row.get("full_copy_locator", ""), project_dir)
    if header == "Source-resolution state/locator":
        return join_parts(
            row.get("acquisition_state", ""),
            row.get("full_text_review_locator", ""),
        )
    if header == "Claim-matched upgrade search / stronger source":
        return join_parts(row.get("upgrade_search", ""), row.get("superseded_by", ""))
    if header == "Author-access request surfaced date/locator":
        return join_parts(
            row.get("request_surfaced_date", ""),
            row.get("request_surfaced_locator", ""),
        )
    raise KeyError(header)


def escape_cell(value: str) -> str:
    """Make a ledger value safe inside a Markdown table cell."""
    return value.replace("|", r"\|").replace("\n", " ").strip()


def split_row(line: str) -> list[str]:
    """Split a Markdown table row into cells, honouring escaped pipes."""
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in body:
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\":
            current.append(char)
            escaped = True
            continue
        if char == "|":
            cells.append("".join(current).strip())
            current = []
            continue
        current.append(char)
    cells.append("".join(current).strip())
    return cells


def build_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def is_separator(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and set(stripped) <= set("|-: ")


def locate_table(lines: list[str]) -> tuple[int, int, list[str]]:
    """Find the manifest's main source table.

    Returns the header index, the index one past the last body row, and the header cells.
    The table is identified by its ``Source ID`` first column, never by position, so
    editing the prose around it cannot move the target.
    """
    for index, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cells = split_row(line)
        if not cells or cells[0] != "Source ID":
            continue
        if index + 1 >= len(lines) or not is_separator(lines[index + 1]):
            continue
        end = index + 2
        while end < len(lines) and lines[end].strip().startswith("|"):
            end += 1
        return index, end, cells
    raise SystemExit(
        f"{MANIFEST_NAME}: no source table found. The table's first column header must be "
        "'Source ID'."
    )


def render(project_dir: Path) -> tuple[str, list[str]]:
    """Return the rewritten manifest text and a list of human-readable changes."""
    manifest_path = project_dir / MANIFEST_NAME
    ledger_path = project_dir / LEDGER_NAME
    for required in (manifest_path, ledger_path):
        if not required.is_file():
            raise SystemExit(f"not found: {required}")

    with ledger_path.open(newline="", encoding="utf-8-sig") as handle:
        ledger = list(csv.DictReader(handle))

    published_identity = None
    if (project_dir / CATALOG_NAME).is_file():
        # The Markdown publisher deterministically turns catalog-backed bibliographic
        # shorthand into keyed links. Accept that published form as semantically equal to
        # the ledger-derived plain form, or generation and publication can never both pass.
        script_dir = str(Path(__file__).resolve().parent)
        if script_dir not in sys.path:
            sys.path.insert(0, script_dir)
        from render_phase1_reports import (  # noqa: PLC0415
            load_citation_catalog,
            transform_citations,
        )

        catalog = load_citation_catalog(project_dir)

        def published_identity(value: str) -> str:
            return transform_citations(value, catalog)[0]

    text = manifest_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    start, end, headers = locate_table(lines)
    width = len(headers)

    derived_index = {
        header: position
        for position, header in enumerate(headers)
        if header in DERIVED_HEADERS
    }
    if "Source ID" not in derived_index:
        raise SystemExit(f"{MANIFEST_NAME}: the source table has no 'Source ID' column.")
    key_position = derived_index["Source ID"]

    existing: dict[str, list[str]] = {}
    order: list[str] = []
    orphans: list[str] = []
    ledger_ids = {row.get("source_id", "") for row in ledger}
    for line in lines[start + 2 : end]:
        cells = split_row(line)
        if len(cells) < width:
            cells += [""] * (width - len(cells))
        source_id = cells[key_position]
        if not source_id or set(source_id) <= {"-", " "}:
            continue  # an empty template placeholder row
        if source_id not in ledger_ids:
            orphans.append(source_id)
        existing[source_id] = cells[:width]
        order.append(source_id)

    changes: list[str] = []
    body: list[str] = []
    for row in ledger:
        source_id = row.get("source_id", "")
        if not source_id:
            continue
        cells = existing.get(source_id)
        if cells is None:
            cells = [""] * width
            changes.append(f"{source_id}: row added from the ledger")
        for header, position in derived_index.items():
            wanted = escape_cell(derive(header, row, project_dir))
            accepted = {wanted}
            if header == "Bibliographic identity" and published_identity is not None:
                accepted.add(
                    escape_cell(published_identity(derive(header, row, project_dir)))
                )
            if cells[position] not in accepted:
                changes.append(
                    f"{source_id}: {header!r} was {cells[position]!r}, now {wanted!r}"
                )
                cells[position] = wanted
        body.append(build_row(cells))

    for source_id in order:
        if source_id not in ledger_ids:
            changes.append(
                f"{source_id}: printed on the manifest but absent from {LEDGER_NAME}; the "
                "row was dropped. Add the ledger row, or delete it from the page on purpose."
            )

    rebuilt = lines[: start + 2] + body + lines[end:]
    output = "\n".join(rebuilt)
    if text.endswith("\n"):
        output += "\n"
    return output, changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", help="directory holding source-manifest.md")
    parser.add_argument(
        "--check",
        action="store_true",
        help="report drift and exit non-zero instead of writing",
    )
    args = parser.parse_args()

    project_dir = Path(args.project_dir).expanduser().resolve()
    output, changes = render(project_dir)
    manifest_path = project_dir / MANIFEST_NAME

    if args.check:
        if changes:
            print(f"FAIL: {MANIFEST_NAME} disagrees with {LEDGER_NAME}:")
            for change in changes:
                print(f"  - {change}")
            print("Run render_source_manifest.py without --check to regenerate it.")
            return 1
        print(f"PASS: {MANIFEST_NAME} matches {LEDGER_NAME}.")
        return 0

    if not changes:
        print(f"PASS: {MANIFEST_NAME} already matches {LEDGER_NAME}. Nothing written.")
        return 0

    # Write through a temporary file and re-read it, so a failed write cannot leave a
    # truncated manifest where a correct one used to be.
    temporary = manifest_path.with_suffix(".md.tmp")
    temporary.write_text(output, encoding="utf-8")
    if temporary.read_text(encoding="utf-8") != output:
        temporary.unlink(missing_ok=True)
        raise SystemExit(f"refused to replace {MANIFEST_NAME}: the temporary copy differs.")
    os.replace(temporary, manifest_path)

    print(f"Rewrote {MANIFEST_NAME}: {len(changes)} change(s).")
    for change in changes:
        print(f"  - {change}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
