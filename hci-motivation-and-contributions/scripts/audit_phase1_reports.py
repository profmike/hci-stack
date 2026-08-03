#!/usr/bin/env python3
"""Audit generated Phase 1 HTML reports for structural and citation defects."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


CORE_REPORT_NAMES = (
    "phase-1-progress.html",
    "literature-and-evidence.html",
    "phase-1-final.html",
)
ARTIFACT_INDEX_NAME = "artifact-index.html"
ARTIFACT_REPORT_NAMES = (
    "phase-1-collaboration-workboard.html",
    "ranked-related-work-positioning.html",
    "acm-sigchi-related-work-audit.html",
    "related-work-search-recall-audit.html",
    "related-work-matrix.html",
    "related-work-contribution-tier-audit.html",
    "prior-work-contribution-boundary.html",
    "prior-work-evidence-accounting.html",
    "idea-provenance-ledger.html",
    "imported-bibliography-accountability.html",
    "late-found-work-postmortem.html",
    "novelty-regression-sentinels.html",
    "evidence-strength-register.html",
    "authoritative-source-map.html",
    "consequence-severity-ranking.html",
    "current-practice-audit.html",
    "motivation-claim-research-queue.html",
    "source-manifest.html",
    "source-resolution.html",
    "missing-full-copies.html",
)
REPORT_NAMES = CORE_REPORT_NAMES + (ARTIFACT_INDEX_NAME,) + ARTIFACT_REPORT_NAMES
NAVIGATION_NAMES = CORE_REPORT_NAMES + (ARTIFACT_INDEX_NAME,)
SOURCE_MIRROR_REPORTS = {
    "prior-work-contribution-boundary.html": "prior-work-contribution-boundary.md",
    "prior-work-evidence-accounting.html": "prior-work-evidence-accounting.csv",
    "idea-provenance-ledger.html": "idea-provenance-ledger.csv",
    "imported-bibliography-accountability.html": "imported-bibliography-accountability.csv",
    "late-found-work-postmortem.html": "late-found-work-postmortem.csv",
    "novelty-regression-sentinels.html": "novelty-regression-sentinels.yaml",
    "source-resolution.html": "source-resolution.csv",
}
REFERENCE_FIELDS = (
    "citation_key",
    "author_year",
    "short_title",
    "venue_abbrev",
    "full_title",
    "full_authors",
    "full_venue",
    "url",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit Phase 1 report HTML and citation metadata."
    )
    parser.add_argument("project_dir", type=Path, help="Research-framing directory")
    parser.add_argument(
        "--report-dir",
        type=Path,
        help="Report directory (default: PROJECT_DIR/reports)",
    )
    return parser.parse_args()


class ReportParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[dict[str, str]] = []
        self.citations: list[dict[str, str]] = []
        self.remote_resources: list[str] = []
        self.table_rows: list[list[str]] = []
        self.current_row: list[str] | None = None
        self.current_cell: list[str] | None = None
        self.citation_depth = 0
        self.reference_depth = 0
        self.code_depth = 0
        self.unlinked_text: list[str] = []

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]):
        attrs = {key: value or "" for key, value in attrs_list}
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        classes = set(attrs.get("class", "").split())
        if tag == "a":
            self.links.append(attrs)
            if "citation" in classes:
                self.citations.append({**attrs, "_text": ""})
                self.citation_depth += 1
        if tag == "article" and "reference-card" in classes:
            self.reference_depth += 1
        if tag in {"code", "pre"}:
            self.code_depth += 1
        if tag in {"script", "img", "link", "iframe", "source", "video", "audio"}:
            location = attrs.get("src") or attrs.get("href") or ""
            if location.startswith(("http://", "https://", "//")):
                self.remote_resources.append(f"{tag}: {location}")
        if tag == "tr":
            self.current_row = []
        if tag in {"th", "td"} and self.current_row is not None:
            self.current_cell = []

    def handle_endtag(self, tag: str):
        if tag == "a" and self.citation_depth:
            self.citation_depth -= 1
        if tag in {"code", "pre"} and self.code_depth:
            self.code_depth -= 1
        if tag in {"th", "td"} and self.current_cell is not None:
            assert self.current_row is not None
            self.current_row.append("".join(self.current_cell).strip())
            self.current_cell = None
        if tag == "tr" and self.current_row is not None:
            self.table_rows.append(self.current_row)
            self.current_row = None
        if tag == "article" and self.reference_depth:
            self.reference_depth -= 1

    def handle_data(self, data: str):
        if self.current_cell is not None:
            self.current_cell.append(data)
        if self.citation_depth and self.citations:
            self.citations[-1]["_text"] += data
        elif not self.reference_depth and not self.code_depth:
            self.unlinked_text.append(data)


def load_references(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    issues: list[str] = []
    if not path.is_file():
        return [], [f"missing citation catalog: {path}"]
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        missing_columns = [field for field in (*REFERENCE_FIELDS, "aliases") if field not in columns]
        if missing_columns:
            issues.append(
                "references.csv missing columns: " + ", ".join(missing_columns)
            )
            return [], issues
        references = [
            {key: (value or "").strip() for key, value in row.items()}
            for row in reader
        ]
    seen: set[str] = set()
    for row_number, reference in enumerate(references, start=2):
        for field in REFERENCE_FIELDS:
            if not reference[field]:
                issues.append(f"references.csv row {row_number}: empty {field}")
        key = reference["citation_key"]
        if key in seen:
            issues.append(f"references.csv row {row_number}: duplicate citation_key {key}")
        seen.add(key)
        if reference["author_year"] and not re.fullmatch(
            r".+,\s*\d{4}[a-z]?", reference["author_year"]
        ):
            issues.append(
                f"references.csv row {row_number}: author_year must end with ', YYYY'"
            )
        url = reference["url"]
        if url and not url.startswith(("http://", "https://", "internal:")):
            issues.append(
                f"references.csv row {row_number}: url must be HTTP(S) or internal:"
            )
    alias_owners: dict[str, set[str]] = {}
    for reference in references:
        for alias in alias_set(reference):
            alias_owners.setdefault(alias, set()).add(reference["citation_key"])
    for alias, keys in sorted(alias_owners.items()):
        if len(keys) > 1:
            issues.append(
                "references.csv ambiguous alias "
                f"'{alias}' maps to {', '.join(sorted(keys))}; "
                "use explicit [@CitationKey] tokens"
            )
    return references, issues


def alias_set(reference: dict[str, str]) -> set[str]:
    author_year = reference["author_year"]
    aliases = {
        reference["citation_key"],
        author_year,
        author_year.replace(",", ""),
        author_year.replace(", ", " "),
        reference["short_title"],
    }
    aliases.update(
        alias.strip()
        for alias in reference.get("aliases", "").split("||")
        if alias.strip()
    )
    match = re.fullmatch(r"(.+),\s*(\d{4}[a-z]?)", author_year)
    if match:
        author, year = match.groups()
        venue = reference["venue_abbrev"]
        aliases.update(
            {
                f"{author} ({year})",
                f"{author} ({venue} {year})",
                f"{author} ({year} {venue})",
                f"{author} ({venue}, {year})",
                f"{author}, {venue} {year}",
                f"{author} {venue} {year}",
            }
        )
    return {re.sub(r"\s+", " ", alias).strip() for alias in aliases if alias.strip()}


def first_author_surname(reference: dict[str, str]) -> str | None:
    match = re.fullmatch(r"(.+),\s*(\d{4}[a-z]?)", reference["author_year"])
    if not match:
        return None
    multiple_authors = re.fullmatch(r"(.+?)\s+et al\.", match.group(1))
    if not multiple_authors:
        return None
    return multiple_authors.group(1).split()[-1]


def unique_surname_aliases(
    references: list[dict[str, str]],
) -> dict[str, set[str]]:
    owners: dict[str, set[str]] = {}
    for reference in references:
        surname = first_author_surname(reference)
        if surname:
            owners.setdefault(surname, set()).add(reference["citation_key"])
    return {
        key: {surname}
        for surname, keys in owners.items()
        if len(keys) == 1
        for key in keys
    }


def normalize_shorthand(value: str) -> str:
    words = re.findall(r"[^\W_]+(?:[’'-][^\W_]+)*", value, flags=re.UNICODE)
    return " ".join(words).casefold()


def unresolved_parenthetical_shorthands(
    references: list[dict[str, str]], segments: list[str]
) -> set[str]:
    candidates: dict[str, set[str]] = {}
    for reference in references:
        surname = first_author_surname(reference)
        if surname:
            candidates.setdefault(normalize_shorthand(surname), set()).add(
                reference["citation_key"]
            )
        title_words = re.findall(
            r"[^\W_]+(?:[’'-][^\W_]+)*",
            reference["short_title"],
            flags=re.UNICODE,
        )
        for length in range(2, len(title_words)):
            prefix = normalize_shorthand(" ".join(title_words[:length]))
            if len(prefix) >= 8:
                candidates.setdefault(prefix, set()).add(reference["citation_key"])

    issues: set[str] = set()
    for segment in segments:
        for parenthetical in re.findall(r"\(([^()]*)\)", segment):
            parts = re.split(r"\s*(?:/|;|\band\b)\s*", parenthetical)
            for part in parts:
                normalized = normalize_shorthand(part)
                keys = candidates.get(normalized)
                if keys:
                    issues.add(
                        f"'{part.strip()}' could mean {', '.join(sorted(keys))}; "
                        "use one explicit [@CitationKey] token per work"
                    )
    return issues


def citation_label(reference: dict[str, str]) -> str:
    match = re.fullmatch(r"(.+),\s*(\d{4}[a-z]?)", reference["author_year"])
    if not match:
        return (
            f"{reference['author_year']} ({reference['venue_abbrev']}): "
            f"{reference['short_title']}"
        )
    author, year = match.groups()
    return f"{author} ({year} {reference['venue_abbrev']}): {reference['short_title']}"


def citation_tooltip(reference: dict[str, str]) -> str:
    return " ".join(
        part.strip().rstrip(".") + "."
        for part in (
            reference["full_authors"],
            reference["full_title"],
            reference["full_venue"],
        )
        if part.strip()
    )


def citation_destination(reference: dict[str, str]) -> str:
    if reference["url"].startswith(("http://", "https://")):
        return reference["url"]
    anchor = "ref-" + re.sub(
        r"[^a-z0-9]+", "-", reference["citation_key"].lower()
    ).strip("-")
    return f"literature-and-evidence.html#{anchor}"


def file_digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def audit(project_dir: Path, report_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    references, reference_issues = load_references(project_dir / "references.csv")
    errors.extend(reference_issues)
    expected_citations: dict[str, set[tuple[str, str]]] = {}
    for reference in references:
        expected_citations.setdefault(citation_label(reference), set()).add(
            (citation_destination(reference), citation_tooltip(reference))
        )
    parsed: dict[str, ReportParser] = {}

    for name in REPORT_NAMES:
        path = report_dir / name
        if not path.is_file():
            errors.append(f"missing report: {path}")
            continue
        source = path.read_text(encoding="utf-8", errors="replace")
        source_artifact_name = SOURCE_MIRROR_REPORTS.get(name)
        if source_artifact_name:
            source_artifact = project_dir / source_artifact_name
            if not source_artifact.is_file():
                errors.append(
                    f"{name}: missing required source artifact {source_artifact}"
                )
            else:
                if f"<code>{source_artifact_name}</code>" not in source:
                    errors.append(
                        f"{name}: does not identify source artifact {source_artifact_name}"
                    )
                expected_digest = file_digest(source_artifact)
                if expected_digest not in source:
                    errors.append(
                        f"{name}: does not match current SHA-256 for "
                        f"{source_artifact_name}; regenerate reports"
                    )
        if "<script" in source.lower():
            errors.append(f"{name}: script element found")
        parser = ReportParser()
        parser.feed(source)
        parser.close()
        parsed[name] = parser

        for resource in parser.remote_resources:
            errors.append(f"{name}: remote embedded resource {resource}")
        hrefs = {link.get("href", "") for link in parser.links}
        for required in NAVIGATION_NAMES:
            if required not in hrefs:
                errors.append(f"{name}: report navigation missing {required}")

        for row_index, row in enumerate(parser.table_rows, start=1):
            if not row:
                continue
            if any(cell == "\\" or cell.endswith("\\") for cell in row):
                errors.append(
                    f"{name}: table row {row_index} contains visible escape debris: {row}"
                )
            if len(row) == 1 and row[0]:
                warnings.append(f"{name}: table row {row_index} has only one cell")

        for citation in parser.citations:
            text = citation.get("_text", "").strip()
            candidates = expected_citations.get(text)
            if not candidates:
                errors.append(f"{name}: citation label does not match catalog format: {text}")
            for attribute in ("href", "title", "aria-label"):
                if not citation.get(attribute):
                    errors.append(f"{name}: citation '{text}' missing {attribute}")
            if citation.get("title") != citation.get("aria-label"):
                errors.append(f"{name}: citation '{text}' hover and accessible labels differ")
            if candidates:
                href = citation.get("href", "")
                destination_matches = {
                    tooltip
                    for destination, tooltip in candidates
                    if destination == href
                }
                if not destination_matches:
                    errors.append(
                        f"{name}: citation '{text}' does not use its canonical destination"
                    )
                elif citation.get("title", "") not in destination_matches:
                    errors.append(
                        f"{name}: citation '{text}' metadata does not match full catalog record"
                    )

    literature = parsed.get("literature-and-evidence.html")
    if literature is not None:
        for reference in references:
            anchor = "ref-" + re.sub(
                r"[^a-z0-9]+", "-", reference["citation_key"].lower()
            ).strip("-")
            if anchor not in literature.ids:
                errors.append(
                    f"literature-and-evidence.html: missing reference anchor #{anchor}"
                )

    all_ids = literature.ids if literature else set()
    surname_aliases = unique_surname_aliases(references)
    for name, parser in parsed.items():
        for link in parser.links:
            href = link.get("href", "")
            prefix = "literature-and-evidence.html#"
            if href.startswith(prefix) and href[len(prefix) :] not in all_ids:
                errors.append(f"{name}: broken internal citation link {href}")

        unlinked_segments = [
            re.sub(r"\s+", " ", segment).strip()
            for segment in parser.unlinked_text
            if segment.strip()
        ]
        for segment in unlinked_segments:
            for token in re.findall(r"\[@[^\[\]]+\]", segment):
                errors.append(f"{name}: unresolved explicit citation token '{token}'")
        for shorthand in sorted(
            unresolved_parenthetical_shorthands(references, unlinked_segments)
        ):
            errors.append(f"{name}: unresolved citation shorthand {shorthand}")
        for reference in references:
            aliases = alias_set(reference) | surname_aliases.get(
                reference["citation_key"], set()
            )
            for alias in aliases:
                if len(alias) < 5:
                    continue
                pattern = r"(?<![\w/:])" + re.escape(alias) + r"(?![\w/])"
                if any(re.search(pattern, segment) for segment in unlinked_segments):
                    errors.append(f"{name}: unlinked citation alias '{alias}'")
                    break

    return errors, warnings


def main() -> int:
    args = parse_args()
    project_dir = args.project_dir.resolve()
    report_dir = (args.report_dir or project_dir / "reports").resolve()
    errors, warnings = audit(project_dir, report_dir)
    for issue in warnings:
        print(f"WARNING: {issue}")
    for issue in errors:
        print(f"ERROR: {issue}")
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: {len(REPORT_NAMES)} reports, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
