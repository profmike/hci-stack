#!/usr/bin/env python3
"""Publish a GitHub-previewable Phase 1 Markdown shelf.

The publisher maintains only bounded navigation/citation blocks in canonical Markdown. Research
claims, decisions, evidence ratings, and statuses remain authored in their canonical artifacts.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import quote


CATALOG_FIELDS = (
    "citation_key",
    "author_year",
    "short_title",
    "venue_abbrev",
    "full_title",
    "full_authors",
    "full_venue",
    "url",
    "aliases",
)

NAV_START = "<!-- HCI-PHASE1-NAV:START -->"
NAV_END = "<!-- HCI-PHASE1-NAV:END -->"
CITATIONS_START = "<!-- HCI-CITATIONS:START -->"
CITATIONS_END = "<!-- HCI-CITATIONS:END -->"
HASH_START = "<!-- HCI-PHASE1-SOURCE-HASHES:START"
HASH_END = "HCI-PHASE1-SOURCE-HASHES:END -->"
GENERATED_MARKER = "<!-- GENERATED: hci-motivation-and-contributions Markdown publisher -->"

KEY_PATTERN = r"[A-Za-z0-9][A-Za-z0-9_.:-]*"
RAW_TOKEN_RE = re.compile(rf"(?<!\])\[@({KEY_PATTERN})\]")
INLINE_CODE_TOKEN_RE = re.compile(rf"`+\[@({KEY_PATTERN})\]`+")
KEYED_LINK_RE = re.compile(rf"\[([^\]\n]+)\]\[({KEY_PATTERN})\]")
WRAPPED_TOKEN_LINK_RE = re.compile(
    rf"\[[^\]\n]*`?\[@({KEY_PATTERN})\]`?[^\]\n]*\]\([^\n]+?\)"
)
MARKDOWN_LINK_RE = re.compile(
    r"!?\[[^\]\n]*\](?:\(<[^>\n]+>\)|\([^\n)]*\)|\[[^\]\n]+\])"
)
MANAGED_NAV_RE = re.compile(
    rf"\n?{re.escape(NAV_START)}.*?{re.escape(NAV_END)}\n?", re.DOTALL
)
MANAGED_CITATION_RE = re.compile(
    rf"\n?{re.escape(CITATIONS_START)}.*?{re.escape(CITATIONS_END)}\n?", re.DOTALL
)

CORE_REPORTS: dict[str, tuple[str, str, tuple[str, ...]]] = {
    "phase-1-progress.md": (
        "Phase 1 progress",
        "Decision-first current state, active collaboration, blockers, and next action.",
        (
            "phase-1-collaboration-workboard.md",
            "starting-state.md",
            "author-decisions.md",
            "decision-packets/README.md",
            "contribution-options.md",
            "terminology-contract.md",
            "motivation-claim-research-queue.md",
            "source-resolution.csv",
            "missing-full-copies.md",
            "reviewer-panel/README.md",
        ),
    ),
    "literature-and-evidence.md": (
        "Literature and evidence",
        "Full-copy, evidence-strength, search, related-work, and source-access record.",
        (
            "source-manifest.md",
            "notebooklm-maintenance.md",
            "authoritative-source-map.md",
            "evidence-strength-register.md",
            "source-resolution.csv",
            "claim-evidence-ledger.csv",
            "current-practice-audit.md",
            "consequence-severity-ranking.md",
            "acm-sigchi-related-work-audit.md",
            "related-work-search-recall-audit.md",
            "related-work-matrix.md",
            "related-work-contribution-tier-audit.md",
            "ranked-related-work-positioning.md",
            "prior-work-contribution-boundary.md",
            "prior-work-evidence-accounting.csv",
            "idea-provenance-ledger.csv",
            "imported-bibliography-accountability.csv",
            "late-found-work-postmortem.csv",
            "novelty-regression-sentinels.yaml",
            "citation-chain-log.md",
            "missing-full-copies.md",
        ),
    ),
    "phase-1-final.md": (
        "Phase 1 research direction",
        "Selected framing, prospective contributions, evidence boundaries, and downstream handoff.",
        (
            "phase-1-collaboration-workboard.md",
            "research-framing-outline.md",
            "contribution-options.md",
            "ranked-related-work-positioning.md",
            "terminology-contract.md",
            "author-decisions.md",
            "decision-packets/README.md",
            "reviewer-panel/README.md",
            "phase-2-handoff.md",
        ),
    ),
}

DATA_MIRRORS: dict[str, str] = {
    "references.csv": "references.md",
    "source-resolution.csv": "source-resolution.md",
    "claim-evidence-ledger.csv": "claim-evidence-ledger.md",
    "prior-work-evidence-accounting.csv": "prior-work-evidence-accounting.md",
    "idea-provenance-ledger.csv": "idea-provenance-ledger.md",
    "imported-bibliography-accountability.csv": "imported-bibliography-accountability.md",
    "late-found-work-postmortem.csv": "late-found-work-postmortem.md",
    "novelty-regression-sentinels.yaml": "novelty-regression-sentinels.md",
    "agent-context.json": "agent-context.md",
}


@dataclass(frozen=True)
class Citation:
    key: str
    author_year: str
    short_title: str
    venue: str
    full_title: str
    full_authors: str
    full_venue: str
    url: str
    aliases: tuple[str, ...]

    @property
    def label(self) -> str:
        match = re.fullmatch(r"(.+?),\s*(\d{4}[a-z]?)", self.author_year.strip())
        if match:
            author, year = match.groups()
            return f"{author} ({year} {self.venue}): {self.short_title}"
        return f"{self.author_year} ({self.venue}): {self.short_title}"

    @property
    def metadata(self) -> str:
        return f"{self.full_authors}. {self.full_title}. {self.full_venue}."


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_citation_catalog(root: Path) -> dict[str, Citation]:
    path = root / "references.csv"
    if not path.is_file():
        raise ValueError(f"missing citation catalog: {path}")
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != CATALOG_FIELDS:
            raise ValueError(
                "references.csv must use exactly: " + ",".join(CATALOG_FIELDS)
            )
        catalog: dict[str, Citation] = {}
        folded_keys: dict[str, str] = {}
        aliases: dict[str, str] = {}
        for line_number, row in enumerate(reader, start=2):
            missing = [field for field in CATALOG_FIELDS[:-1] if not (row.get(field) or "").strip()]
            if missing:
                raise ValueError(
                    f"references.csv line {line_number} missing metadata: {', '.join(missing)}"
                )
            key = row["citation_key"].strip()
            if not re.fullmatch(KEY_PATTERN, key):
                raise ValueError(f"invalid citation key {key!r} on line {line_number}")
            folded = key.casefold()
            if folded in folded_keys:
                raise ValueError(
                    f"duplicate citation key after case-folding: {folded_keys[folded]!r} and {key!r}"
                )
            url = row["url"].strip()
            if not (url.startswith("https://") or url.startswith("http://") or url.startswith("internal:")):
                raise ValueError(f"citation {key!r} has unsupported canonical destination {url!r}")
            parsed_aliases = tuple(
                alias.strip() for alias in row["aliases"].split("||") if alias.strip()
            )
            citation = Citation(
                key=key,
                author_year=row["author_year"].strip(),
                short_title=row["short_title"].strip(),
                venue=row["venue_abbrev"].strip(),
                full_title=row["full_title"].strip(),
                full_authors=row["full_authors"].strip(),
                full_venue=row["full_venue"].strip(),
                url=url,
                aliases=parsed_aliases,
            )
            catalog[key] = citation
            folded_keys[folded] = key
            for alias in parsed_aliases:
                alias_folded = alias.casefold()
                prior = aliases.get(alias_folded)
                if prior and prior != key:
                    raise ValueError(
                        f"ambiguous citation alias {alias!r}: {prior!r} and {key!r}"
                    )
                aliases[alias_folded] = key
    return catalog


def relative_link(from_file: Path, target: Path) -> str:
    relative = Path(os.path.relpath(target, start=from_file.parent)).as_posix()
    return quote(relative, safe="/._~-")


def citation_destination(citation: Citation, file_path: Path, output_dir: Path) -> str:
    if citation.url.startswith("internal:"):
        catalog = output_dir / "references.md"
        return relative_link(file_path, catalog) + "#reference-" + quote(citation.key.lower())
    return citation.url


def navigation_block(file_path: Path, repo_root: Path, root: Path, output_dir: Path) -> str:
    links = (
        ("Project overview", repo_root / "README.md"),
        ("Phase 1 index", output_dir / "artifact-index.md"),
        ("Live workboard", root / "phase-1-collaboration-workboard.md"),
        ("Phase 2 handoff", root / "phase-2-handoff.md"),
    )
    rendered = " · ".join(
        f"[{label}]({relative_link(file_path, target)})" for label, target in links
    )
    return f"{NAV_START}\n{rendered}\n{NAV_END}"


def insert_after_title(text: str, block: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            content_index = index + 1
            while content_index < len(lines) and not lines[content_index].strip():
                content_index += 1
            normalized = lines[: index + 1] + ["", block, ""] + lines[content_index:]
            return "\n".join(normalized).rstrip() + "\n"
    return block + "\n\n" + text.lstrip()


def _link_catalog_shorthands(segment: str, catalog: dict[str, Citation]) -> str:
    """Link exact, unique catalog shorthands that include a parenthetical year.

    This is a migration aid, not fuzzy citation inference. Existing Markdown links and reference
    definitions are protected, and a surface form shared by multiple catalog records is left for
    the fail-closed auditor to report.
    """
    if re.match(r"^\s*\[[^\]\n]+\]:", segment):
        return segment

    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"\x00HCI_LINK_{len(protected) - 1}\x00"

    masked = MARKDOWN_LINK_RE.sub(protect, segment)
    candidates: dict[tuple[int, int], set[str]] = {}
    for key, citation in catalog.items():
        phrases: list[tuple[str, str]] = []
        author_match = re.fullmatch(
            r"(.+?),\s*((?:19|20)\d{2}[a-z]?)", citation.author_year.strip()
        )
        if author_match:
            author, year = author_match.groups()
            # A catalog suffix disambiguates its entry, but legacy prose often omitted it. If that
            # omission makes two records collide, the uniqueness check below deliberately declines.
            year_pattern = re.escape(year[:4])
            if len(year) > 4:
                year_pattern += rf"(?:{re.escape(year[4:])})?"
            phrases.append((author, year_pattern))
        phrases.extend(
            (title, r"(?:19|20)\d{2}[a-z]?")
            for title in (citation.short_title, citation.full_title)
            if title
        )
        for phrase, year_pattern in phrases:
            if len(phrase) < 4:
                continue
            pattern = re.compile(
                rf"(?<![\w]){re.escape(phrase)}(?![\w])\s*"
                rf"\([^()\n]*\b{year_pattern}\b[^()\n]*\)",
                re.IGNORECASE,
            )
            for match in pattern.finditer(masked):
                candidates.setdefault((match.start(), match.end()), set()).add(key)

    selected: list[tuple[int, int, str]] = []
    cursor = -1
    for (start, end), keys in sorted(
        candidates.items(), key=lambda item: (item[0][0], -(item[0][1] - item[0][0]))
    ):
        if len(keys) != 1 or start < cursor:
            continue
        selected.append((start, end, next(iter(keys))))
        cursor = end

    for start, end, key in reversed(selected):
        masked = masked[:start] + f"[{catalog[key].label}][{key}]" + masked[end:]
    for index, original in enumerate(protected):
        masked = masked.replace(f"\x00HCI_LINK_{index}\x00", original)
    return masked


def _transform_non_code_segment(segment: str, catalog: dict[str, Citation]) -> str:
    def replace_keyed(match: re.Match[str]) -> str:
        key = match.group(2)
        citation = catalog.get(key)
        if citation is None:
            return match.group(0)
        return f"[{citation.label}][{key}]"

    def replace_raw(match: re.Match[str]) -> str:
        key = match.group(1)
        citation = catalog.get(key)
        if citation is None:
            raise ValueError(f"unknown citation key {key!r}")
        return f"[{citation.label}][{key}]"

    segment = KEYED_LINK_RE.sub(replace_keyed, segment)
    segment = RAW_TOKEN_RE.sub(replace_raw, segment)
    return _link_catalog_shorthands(segment, catalog)


def transform_citations(text: str, catalog: dict[str, Citation]) -> tuple[str, tuple[str, ...]]:
    """Resolve draft tokens outside fenced code and return used keys.

    An exact inline-code token such as ``[@Key]`` is legacy citation authoring, not a code
    example. Publish it as a link so backticks cannot hide an unlinked scholarly citation.
    Fenced code remains literal for documentation examples.
    """
    output: list[str] = []
    in_fence = False
    fence_token = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        fence = re.match(r"(```+|~~~+)", stripped)
        if fence:
            token = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_token = token[0]
            elif token[0] == fence_token:
                in_fence = False
                fence_token = ""
            output.append(line)
            continue
        if in_fence:
            output.append(line)
            continue
        def replace_wrapped_token(match: re.Match[str]) -> str:
            key = match.group(1)
            citation = catalog.get(key)
            if citation is None:
                raise ValueError(f"unknown citation key {key!r}")
            return f"[{citation.label}][{key}]"

        line = WRAPPED_TOKEN_LINK_RE.sub(replace_wrapped_token, line)
        line = INLINE_CODE_TOKEN_RE.sub(replace_wrapped_token, line)
        parts = re.split(r"(`+[^`]*`+)", line)
        output.append(
            "".join(
                part if index % 2 else _transform_non_code_segment(part, catalog)
                for index, part in enumerate(parts)
            )
        )
    transformed = "\n".join(output).rstrip() + "\n"
    used = sorted(
        {
            match.group(2)
            for match in KEYED_LINK_RE.finditer(strip_code(transformed))
            if match.group(2) in catalog
        },
        key=str.casefold,
    )
    return transformed, tuple(used)


def strip_code(text: str) -> str:
    lines: list[str] = []
    in_fence = False
    fence_token = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        fence = re.match(r"(```+|~~~+)", stripped)
        if fence:
            token = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_token = token[0]
            elif token[0] == fence_token:
                in_fence = False
                fence_token = ""
            continue
        if not in_fence:
            lines.append(re.sub(r"`+[^`]*`+", "", line))
    return "\n".join(lines)


def citation_block(
    used_keys: Iterable[str],
    catalog: dict[str, Citation],
    file_path: Path,
    output_dir: Path,
) -> str:
    keys = tuple(used_keys)
    if not keys:
        return ""
    visible = [CITATIONS_START, "## References", ""]
    definitions: list[str] = []
    for key in keys:
        citation = catalog[key]
        destination = citation_destination(citation, file_path, output_dir)
        metadata = " ".join(citation.metadata.split()).replace('"', "'")
        visible.append(
            f'- <a id="reference-{key.lower()}"></a>'
            f'[{citation.label}](<{destination}>) — {citation.full_authors}. '
            f'*{citation.full_title}*. {citation.full_venue}. Stable key: `{key}`.'
        )
        definitions.append(f'[{key}]: <{destination}> "{metadata}"')
    return "\n".join(visible + [""] + definitions + [CITATIONS_END])


def synchronize_markdown(
    path: Path,
    repo_root: Path,
    root: Path,
    output_dir: Path,
    catalog: dict[str, Citation],
    *,
    add_navigation: bool,
) -> str:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    text = MANAGED_NAV_RE.sub("", text)
    text = MANAGED_CITATION_RE.sub("", text)
    text, used_keys = transform_citations(text, catalog)
    if add_navigation:
        text = insert_after_title(
            text,
            navigation_block(path, repo_root, root, output_dir),
        )
    block = citation_block(used_keys, catalog, path, output_dir)
    if block:
        text = text.rstrip() + "\n\n" + block + "\n"
    return text


def source_hash_block(root: Path, source_paths: Iterable[str]) -> str:
    lines = [HASH_START]
    for relative in sorted(set(source_paths)):
        source = root / relative
        value = sha256(source) if source.is_file() else "MISSING"
        lines.append(f"{relative}\t{value}")
    lines.append(HASH_END)
    return "\n".join(lines)


def markdown_link_for_source(report_path: Path, root: Path, relative: str) -> str:
    source = root / relative
    label = relative
    if source.is_file():
        return f"[{label}]({relative_link(report_path, source)})"
    return f"`{label}` — **MISSING**"


def build_core_report(
    filename: str,
    title: str,
    subtitle: str,
    sources: tuple[str, ...],
    root: Path,
    output_dir: Path,
    project_title: str,
) -> str:
    path = output_dir / filename
    lines = [
        f"# {project_title} — {title}",
        "",
        GENERATED_MARKER,
        "",
        subtitle,
        "",
        "This is a generated navigation and provenance view. Follow the links below to the canonical,",
        "editable research records; do not record decisions or evidence only in this file.",
        "",
    ]
    if filename == "phase-1-progress.md":
        lines.extend(
            [
                "## Current state — read this first",
                "",
                f"- {markdown_link_for_source(path, root, 'phase-1-collaboration-workboard.md')} — direction, evidence states, active decisions, blockers, recommendation, and next action/owner.",
                f"- {markdown_link_for_source(path, root, 'author-decisions.md')} — selected, combined, rejected, delegated, and superseded variants with rationale.",
                f"- {markdown_link_for_source(path, root, 'missing-full-copies.md')} — exact human-only source-access requests and reopen triggers.",
                "",
            ]
        )
    elif filename == "phase-1-final.md":
        lines.extend(
            [
                "## Research direction and contribution boundary",
                "",
                f"- {markdown_link_for_source(path, root, 'research-framing-outline.md')} — argument outline and evidence-state boundaries.",
                f"- {markdown_link_for_source(path, root, 'contribution-options.md')} — prospective contribution packages and evidence gates.",
                f"- {markdown_link_for_source(path, root, 'phase-2-handoff.md')} — downstream contract, blocked claims, and return conditions.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "## Evidence record",
                "",
                f"- {markdown_link_for_source(path, root, 'evidence-strength-register.md')} — claim-specific strength and re-review triggers.",
                f"- {markdown_link_for_source(path, root, 'ranked-related-work-positioning.md')} — same/similar-problem ranking and working comparisons.",
                f"- [Source-resolution Markdown view]({relative_link(path, output_dir / 'source-resolution.md')}) — acquisition and access state.",
                "",
            ]
        )
    lines.extend(["## Canonical records", ""])
    for relative in sources:
        lines.append(f"- {markdown_link_for_source(path, root, relative)}")
    lines.extend(["", source_hash_block(root, sources), ""])
    return "\n".join(lines)


def markdown_cell(value: str) -> str:
    return " ".join((value or "").split()).replace("|", "\\|")


def csv_markdown_value(field: str, value: str, source: Path, report_path: Path) -> str:
    """Render URL and resolvable locator fields as human-usable Markdown links."""
    value = " ".join((value or "").split())
    if not value:
        return ""
    destination = ""
    if field in {"canonical_url", "url", "full_copy_locator"} and value.startswith(
        ("https://", "http://")
    ):
        destination = value
    elif field == "full_copy_locator":
        path_part, separator, fragment = value.partition("#")
        candidate = source.parent / path_part
        if path_part and not Path(path_part).is_absolute() and candidate.exists():
            destination = relative_link(report_path, candidate)
            if separator:
                destination += "#" + quote(fragment, safe="._~-")
    escaped = markdown_cell(value)
    return f"[{escaped}](<{destination}>)" if destination else escaped


def csv_mirror(source: Path, report_path: Path) -> str:
    with source.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    if not fields:
        return "_The canonical CSV has no header._\n"
    if len(fields) <= 10:
        lines = [
            "| " + " | ".join(markdown_cell(field) for field in fields) + " |",
            "| " + " | ".join("---" for _ in fields) + " |",
        ]
        for row in rows:
            lines.append(
                "| "
                + " | ".join(
                    csv_markdown_value(field, row.get(field, ""), source, report_path)
                    for field in fields
                )
                + " |"
            )
        return "\n".join(lines) + "\n"
    lines = []
    preferred_ids = (
        "record_id",
        "source_id",
        "claim_id",
        "citation_key",
        "candidate_id",
    )
    for index, row in enumerate(rows, start=1):
        identity = next((row.get(field, "").strip() for field in preferred_ids if row.get(field, "").strip()), str(index))
        lines.extend([f"### Record {index} — `{identity}`", ""])
        for field in fields:
            value = csv_markdown_value(field, row.get(field, ""), source, report_path) or "—"
            lines.append(f"- **{field}:** {value}")
        lines.append("")
    if not rows:
        lines.append("_The canonical CSV currently has no data rows._\n")
    return "\n".join(lines)


def references_mirror(
    catalog: dict[str, Citation],
    mirror_path: Path,
    root: Path,
) -> str:
    lines = ["## Reference catalog", ""]
    for key in sorted(catalog, key=str.casefold):
        citation = catalog[key]
        destination = citation.url
        if destination.startswith("internal:"):
            internal = destination.removeprefix("internal:")
            path_part, separator, fragment = internal.partition("#")
            destination = relative_link(mirror_path, root / path_part)
            if separator:
                destination += "#" + quote(fragment, safe="._~-")
        lines.extend(
            [
                f'### <a id="reference-{key.lower()}"></a>{citation.label}',
                "",
                f"- **Stable key:** `{key}`",
                f"- **Full authors:** {citation.full_authors}",
                f"- **Full title:** {citation.full_title}",
                f"- **Full venue:** {citation.full_venue}",
                f"- **Canonical destination:** [{citation.url}](<{destination}>)",
                "",
            ]
        )
    return "\n".join(lines)


def build_data_mirror(
    source_relative: str,
    report_name: str,
    root: Path,
    output_dir: Path,
    catalog: dict[str, Citation],
    project_title: str,
) -> str:
    source = root / source_relative
    path = output_dir / report_name
    lines = [
        f"# {project_title} — {Path(source_relative).stem.replace('-', ' ').title()}",
        "",
        GENERATED_MARKER,
        "",
        f"Canonical source: {markdown_link_for_source(path, root, source_relative)}",
        "",
    ]
    if not source.is_file():
        lines.extend(["**MISSING:** the required canonical source does not exist.", ""])
    elif source_relative == "references.csv":
        lines.extend([references_mirror(catalog, path, root), ""])
    elif source.suffix.lower() == ".csv":
        lines.extend([csv_mirror(source, path), ""])
    else:
        language = "json" if source.suffix.lower() == ".json" else "yaml"
        lines.extend([f"```{language}", source.read_text(encoding="utf-8").rstrip(), "```", ""])
    lines.extend([source_hash_block(root, (source_relative,)), ""])
    return "\n".join(lines)


def reader_artifacts(root: Path, output_dir: Path) -> list[Path]:
    items: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or output_dir in path.parents:
            continue
        if "sources/full-text" in path.relative_to(root).as_posix():
            continue
        items.append(path)
    return sorted(items, key=lambda path: path.relative_to(root).as_posix().casefold())


def build_artifact_index(root: Path, output_dir: Path, project_title: str) -> str:
    path = output_dir / "artifact-index.md"
    items = reader_artifacts(root, output_dir)
    lines = [
        f"# {project_title} — Phase 1 artifact index",
        "",
        GENERATED_MARKER,
        "",
        "Canonical, editable research records are linked directly. Generated Markdown views are",
        "navigation and ledger-preview aids; they are not independent evidence or decision sources.",
        "",
        "## Canonical artifacts",
        "",
        "| Artifact | Type | SHA-256 |",
        "| --- | --- | --- |",
    ]
    relatives: list[str] = []
    for source in items:
        relative = source.relative_to(root).as_posix()
        relatives.append(relative)
        link = relative_link(path, source)
        lines.append(
            f"| [{relative}]({link}) | `{source.suffix.lstrip('.') or 'file'}` | `{sha256(source)}` |"
        )
    lines.extend(["", "## Generated Markdown views", ""])
    for report in (*CORE_REPORTS, *DATA_MIRRORS.values()):
        lines.append(f"- [{report}]({report})")
    lines.extend(["- [Report shelf](README.md)", "", source_hash_block(root, relatives), ""])
    return "\n".join(lines)


def build_report_readme(project_title: str) -> str:
    lines = [
        f"# {project_title} — Phase 1 Markdown reports",
        "",
        GENERATED_MARKER,
        "",
        "These GitHub-previewable Markdown files link back to the canonical research records. Fix",
        "claims, decisions, or evidence in those records, then rerun the publisher.",
        "",
        "## Start here",
        "",
        "- [Phase 1 progress](phase-1-progress.md)",
        "- [Literature and evidence](literature-and-evidence.md)",
        "- [Phase 1 research direction](phase-1-final.md)",
        "- [Complete artifact index](artifact-index.md)",
        "",
        "## Machine-ledger views",
        "",
    ]
    for report in DATA_MIRRORS.values():
        lines.append(f"- [{report}]({report})")
    return "\n".join(lines) + "\n"


def write_if_changed(path: Path, text: str) -> None:
    normalized = text.rstrip() + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == normalized:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalized, encoding="utf-8")


def generate_reports(
    root: Path,
    output_dir: Path | None = None,
    *,
    project_title: str | None = None,
) -> dict[str, str]:
    root = root.resolve()
    repo_root = root.parent
    output_dir = (output_dir or root / "reports").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    catalog = load_citation_catalog(root)
    title = project_title or repo_root.name

    # Maintain bounded navigation/citation blocks in every canonical Markdown file.
    markdown_sources = [
        path
        for path in root.rglob("*.md")
        if output_dir not in path.parents and path != output_dir
    ]
    root_readme = repo_root / "README.md"
    if root_readme.is_file():
        synchronized = synchronize_markdown(
            root_readme,
            repo_root,
            root,
            output_dir,
            catalog,
            add_navigation=False,
        )
        write_if_changed(root_readme, synchronized)
    for source in sorted(markdown_sources):
        synchronized = synchronize_markdown(
            source,
            repo_root,
            root,
            output_dir,
            catalog,
            add_navigation=True,
        )
        write_if_changed(source, synchronized)

    documents: dict[str, str] = {}
    for filename, (report_title, subtitle, sources) in CORE_REPORTS.items():
        documents[filename] = build_core_report(
            filename,
            report_title,
            subtitle,
            sources,
            root,
            output_dir,
            title,
        )
    for source_relative, report_name in DATA_MIRRORS.items():
        documents[report_name] = build_data_mirror(
            source_relative,
            report_name,
            root,
            output_dir,
            catalog,
            title,
        )
    documents["artifact-index.md"] = build_artifact_index(root, output_dir, title)
    documents["README.md"] = build_report_readme(title)

    for filename, document in list(documents.items()):
        path = output_dir / filename
        write_if_changed(path, document)
        synchronized = synchronize_markdown(
            path,
            repo_root,
            root,
            output_dir,
            catalog,
            add_navigation=True,
        )
        write_if_changed(path, synchronized)
        documents[filename] = synchronized
    return documents


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Publish GitHub-previewable Phase 1 Markdown reports and link blocks."
    )
    parser.add_argument("project_dir", type=Path, help="research-framing directory")
    parser.add_argument("--output-dir", type=Path, help="output directory (default: PROJECT/reports)")
    parser.add_argument("--project-title", help="display title (default: repository directory name)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.project_dir.expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"project directory does not exist: {root}")
    documents = generate_reports(
        root,
        args.output_dir.expanduser().resolve() if args.output_dir else None,
        project_title=args.project_title,
    )
    print(f"PASS: published {len(documents)} Markdown files in {root / 'reports'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
