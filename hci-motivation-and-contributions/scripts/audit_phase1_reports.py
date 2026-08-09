#!/usr/bin/env python3
"""Fail-closed audit for the Phase 1 GitHub Markdown publication shelf."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import render_phase1_reports as publisher


INLINE_LINK_RE = re.compile(
    r"(?<!!)\[[^\]\n]+\]\((<[^>\n]+>|[^)\s\n]+)"
    r"(?:\s+(?:\"[^\"\n]*\"|'[^'\n]*'|\([^\)\n]*\)))?\)"
)
GENERAL_REFERENCE_LINK_RE = re.compile(r"\[([^\]\n]+)\]\[([^\]\n]+)\]")
REFERENCE_DEF_RE = re.compile(
    rf"^\[({publisher.KEY_PATTERN})\]:\s+<([^>]+)>\s+\"([^\"]*)\"\s*$",
    re.MULTILINE,
)
GENERIC_REFERENCE_DEF_RE = re.compile(
    r'^\[([^\]\n]+)\]:\s*(<[^>\n]+>|[^\s\n]+)'
    r'(?:\s+(?:"[^"\n]*"|\'[^\'\n]*\'|\([^\)\n]*\)))?\s*$',
    re.MULTILINE,
)
HASH_BLOCK_RE = re.compile(
    rf"{re.escape(publisher.HASH_START)}\n(.*?){re.escape(publisher.HASH_END)}",
    re.DOTALL,
)
GENERIC_AUTHOR_YEAR_RE = re.compile(
    r"\b[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÖØ-öø-ÿ'’\-]+\s+et\s+al\.\s*"
    r"\([^()\n]*\b(?:19|20)\d{2}[a-z]?\b[^()\n]*\)"
)

REQUIRED_ROOT_LINKS = (
    "research-framing/phase-1-collaboration-workboard.md",
    "research-framing/research-framing-outline.md",
    "research-framing/ranked-related-work-positioning.md",
    "research-framing/evidence-strength-register.md",
    "research-framing/author-decisions.md",
    "research-framing/decision-packets/README.md",
    "research-framing/phase-2-handoff.md",
    "research-framing/reports/README.md",
    "research-framing/reports/phase-1-progress.md",
    "research-framing/reports/literature-and-evidence.md",
    "research-framing/reports/phase-1-final.md",
    "research-framing/reports/artifact-index.md",
)

PHASE_COMPLETION_GATES = (
    (
        "motivation-claim-research-queue.md",
        "MOTIVATION_CLAIM_AUDIT_COMPLETE",
        None,
        "Last sweep",
    ),
    (
        "acm-sigchi-related-work-audit.md",
        "ACM_SIGCHI_LANDSCAPE_AUDITED",
        "ACM_SIGCHI_LANDSCAPE_AUDITED",
        "Last checked",
    ),
    (
        "related-work-search-recall-audit.md",
        "RELATED_WORK_SEARCH_RECALL_AUDITED",
        "RELATED_WORK_SEARCH_RECALL_AUDITED",
        "Last checked",
    ),
)

OPEN_TABLE_VALUE_RE = re.compile(
    r"^(?:no|not reached|queued|needs_[a-z0-9_]+)$|\bpending\b",
    re.IGNORECASE,
)
TABLE_SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")


def expected_report_names() -> set[str]:
    return {
        *publisher.CORE_REPORTS,
        *publisher.DATA_MIRRORS.values(),
        "artifact-index.md",
        "README.md",
    }


def audit_completed_gate_body(path: Path, source: str, errors: list[str]) -> None:
    """Reject residue from the real gate templates, not just their headline markers."""
    for line_number, line in enumerate(source.splitlines(), start=1):
        if re.match(r"^-\s+\*\*[^*]+:\*\*\s*$", line):
            errors.append(f"{path}:{line_number}: completed research gate has a blank field")

        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        cells = [cell.strip() for cell in stripped[1:-1].split("|")]
        if cells and all(TABLE_SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells):
            continue
        for cell in cells:
            normalized = cell.strip().strip("`")
            if not normalized:
                errors.append(
                    f"{path}:{line_number}: completed research gate has a blank table cell"
                )
                break
            if OPEN_TABLE_VALUE_RE.search(normalized):
                errors.append(
                    f"{path}:{line_number}: completed research gate retains unfinished "
                    f"table value {cell!r}"
                )
                break


def audit_phase_completion(root: Path, errors: list[str]) -> None:
    """Reject a completed phase whose canonical research gates are visibly unfinished."""
    manifest_path = root / "agent-context.json"
    if not manifest_path.is_file():
        return
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"{manifest_path}: invalid project-context manifest: {exc}")
        return
    if manifest.get("phase", {}).get("status") != "complete":
        return

    for relative, terminal_status, terminal_gate, date_label in PHASE_COMPLETION_GATES:
        path = root / relative
        if not path.is_file():
            errors.append(f"phase.status=complete but required research gate is missing: {path}")
            continue
        source = path.read_text(encoding="utf-8")
        status = re.search(r"^Status:\s*`([^`]+)`\s*$", source, re.MULTILINE)
        if status is None or status.group(1) != terminal_status:
            actual = status.group(1) if status else "missing"
            errors.append(
                f"{path}: phase.status=complete requires Status `{terminal_status}`; found `{actual}`"
            )
        if terminal_gate is not None:
            gate = re.search(r"^Gate:\s*`([^`]+)`\s*$", source, re.MULTILINE)
            if gate is None or gate.group(1) != terminal_gate:
                actual = gate.group(1) if gate else "missing"
                errors.append(
                    f"{path}: phase.status=complete requires Gate `{terminal_gate}`; "
                    f"found `{actual}`"
                )
        date_match = re.search(
            rf"^{re.escape(date_label)}:\s*(\S+)\s*$", source, re.MULTILINE
        )
        date_value = date_match.group(1) if date_match else ""
        try:
            dt.date.fromisoformat(date_value)
        except ValueError:
            errors.append(
                f"{path}: phase.status=complete requires {date_label} as an ISO date; "
                f"found {date_value!r}"
            )
        unchecked = len(re.findall(r"(?m)^-\s*\[\s\]", source))
        if unchecked:
            errors.append(
                f"{path}: phase.status=complete but {unchecked} research gate item(s) remain unchecked"
            )
        for placeholder in ("YYYY-MM-DD", "| Pending |"):
            if placeholder in source:
                errors.append(
                    f"{path}: phase.status=complete but template placeholder {placeholder!r} remains"
                )
        audit_completed_gate_body(path, source, errors)


def strip_managed_citations(text: str) -> str:
    return publisher.MANAGED_CITATION_RE.sub("\n", text)


def inline_code_citation_tokens(text: str) -> list[str]:
    """Return exact inline-code citation keys while ignoring fenced examples."""
    tokens: list[str] = []
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
            tokens.extend(publisher.INLINE_CODE_TOKEN_RE.findall(line))
    return tokens


def mask_match(match: re.Match[str]) -> str:
    """Hide Markdown syntax while preserving line numbers for diagnostics."""
    return "".join("\n" if character == "\n" else " " for character in match.group(0))


def unlinked_citation_shorthands(
    text: str,
    catalog: dict[str, publisher.Citation],
) -> list[tuple[int, str, str | None]]:
    """Find catalog-backed or author-year scholarly shorthand outside actual links."""
    visible = publisher.strip_code(strip_managed_citations(text))
    visible = GENERIC_REFERENCE_DEF_RE.sub(mask_match, visible)
    visible = INLINE_LINK_RE.sub(mask_match, visible)
    visible = GENERAL_REFERENCE_LINK_RE.sub(mask_match, visible)
    matches: dict[tuple[int, int], tuple[str, set[str]]] = {}
    for key, citation in catalog.items():
        author_match = re.fullmatch(
            r"(.+?),\s*((?:19|20)\d{2}[a-z]?)", citation.author_year.strip()
        )
        candidates: list[tuple[str, str]] = []
        if author_match:
            author, year = author_match.groups()
            candidates.append((author, year))
        candidates.extend((title, "") for title in (citation.short_title, citation.full_title))
        for phrase, required_year in candidates:
            if not phrase or len(phrase) < 4:
                continue
            year_pattern = re.escape(required_year) if required_year else r"(?:19|20)\d{2}[a-z]?"
            pattern = re.compile(
                rf"(?<![\w]){re.escape(phrase)}\s*"
                rf"\([^()\n]*\b{year_pattern}\b[^()\n]*\)",
                re.IGNORECASE,
            )
            for match in pattern.finditer(visible):
                span = (match.start(), match.end())
                if span not in matches:
                    matches[span] = (match.group(0), set())
                matches[span][1].add(key)
    for match in GENERIC_AUTHOR_YEAR_RE.finditer(visible):
        matches.setdefault((match.start(), match.end()), (match.group(0), set()))
    return [
        (
            visible.count("\n", 0, start) + 1,
            mention,
            next(iter(keys)) if len(keys) == 1 else None,
        )
        for (start, _), (mention, keys) in sorted(matches.items())
    ]


def markdown_anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    anchors = set(re.findall(r'<a\s+id="([^"]+)"\s*></a>', text, re.IGNORECASE))
    seen: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", publisher.strip_code(text), re.MULTILINE):
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        slug = heading.strip().lower()
        slug = re.sub(r"[^\w\- ]", "", slug, flags=re.UNICODE)
        slug = re.sub(r"\s+", "-", slug)
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        anchors.add(slug if count == 0 else f"{slug}-{count}")
    return anchors


def parse_inline_target(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<"):
        end = raw.find(">")
        return raw[1:end] if end >= 0 else raw
    # A quoted title may follow a destination. Local repository paths may contain spaces, so only
    # strip a title when it is clearly introduced by whitespace plus a quote.
    match = re.match(r"(.+?)\s+[\"'].*[\"']\s*$", raw)
    return (match.group(1) if match else raw).strip()


def normalize_reference_label(label: str) -> str:
    return " ".join(label.split()).casefold()


def parse_reference_target(raw: str) -> str:
    raw = raw.strip()
    return raw[1:-1] if raw.startswith("<") and raw.endswith(">") else raw


def audit_link(
    source: Path,
    target: str,
    repo_root: Path,
    errors: list[str],
) -> None:
    target = unquote(target.strip())
    if not target or target.startswith("#"):
        if target.startswith("#") and target[1:] not in markdown_anchors(source):
            errors.append(f"{source}: broken local fragment {target!r}")
        return
    split = urlsplit(target)
    if split.scheme:
        if split.scheme in {"http", "https", "mailto"}:
            return
        errors.append(f"{source}: disallowed link scheme in {target!r}")
        return
    if target.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", target):
        errors.append(f"{source}: machine-local absolute link {target!r}")
        return
    relative_path = split.path
    destination = (source.parent / relative_path).resolve() if relative_path else source.resolve()
    try:
        destination.relative_to(repo_root)
    except ValueError:
        errors.append(f"{source}: link escapes project repository: {target!r}")
        return
    if not destination.exists():
        errors.append(f"{source}: broken relative link {target!r}")
        return
    if split.fragment and destination.is_file() and destination.suffix.lower() == ".md":
        if split.fragment not in markdown_anchors(destination):
            errors.append(f"{source}: broken fragment {split.fragment!r} in {target!r}")


def audit_citations(
    path: Path,
    text: str,
    catalog: dict[str, publisher.Citation],
    output_dir: Path,
    repo_root: Path,
    errors: list[str],
) -> None:
    unmanaged = strip_managed_citations(text)
    hidden_inline_tokens = sorted(set(inline_code_citation_tokens(unmanaged)))
    if hidden_inline_tokens:
        errors.append(
            f"{path}: inline-code citation token(s) must be published as links: "
            + ", ".join(hidden_inline_tokens)
        )
    outside_block = publisher.strip_code(unmanaged)
    raw_tokens = sorted(set(publisher.RAW_TOKEN_RE.findall(outside_block)))
    if raw_tokens:
        errors.append(f"{path}: unresolved raw citation token(s): {', '.join(raw_tokens)}")
    if output_dir not in path.parents:
        for line_number, mention, key in unlinked_citation_shorthands(text, catalog):
            resolution = f"; use [@{key}]" if key else ""
            errors.append(
                f"{path}:{line_number}: unlinked scholarly citation shorthand {mention!r}{resolution}"
            )

    all_uses = list(GENERAL_REFERENCE_LINK_RE.finditer(outside_block))
    uses: list[re.Match[str]] = []
    ordinary_uses: list[re.Match[str]] = []
    for match in all_uses:
        label, key = match.groups()
        if key in catalog or re.search(r"\(\d{4}[a-z]?(?:\s+[^)]*)?\):", label):
            uses.append(match)
        else:
            ordinary_uses.append(match)

    generic_definitions: dict[str, list[str]] = {}
    for match in GENERIC_REFERENCE_DEF_RE.finditer(text):
        label, destination = match.groups()
        generic_definitions.setdefault(normalize_reference_label(label), []).append(
            parse_reference_target(destination)
        )
    for match in ordinary_uses:
        label, key = match.groups()
        values = generic_definitions.get(normalize_reference_label(key), [])
        if len(values) != 1:
            errors.append(
                f"{path}: ordinary reference link {label!r} / {key!r} must have exactly one definition"
            )
            continue
        audit_link(path, values[0], repo_root, errors)

    used_keys: list[str] = []
    for match in uses:
        label, key = match.groups()
        citation = catalog.get(key)
        if citation is None:
            errors.append(f"{path}: unknown citation key {key!r}")
            continue
        used_keys.append(key)
        if label != citation.label:
            errors.append(
                f"{path}: citation {key!r} label {label!r} does not match {citation.label!r}"
            )

    citation_key_folds = {match.group(2).casefold() for match in uses}
    definitions = [
        match
        for match in REFERENCE_DEF_RE.finditer(text)
        if match.group(1).casefold() in citation_key_folds
    ]
    definition_map: dict[str, list[tuple[str, str]]] = {}
    for match in definitions:
        key, destination, metadata = match.groups()
        definition_map.setdefault(key, []).append((destination, metadata))
    if len({key.casefold() for key in definition_map}) != len(definition_map):
        errors.append(f"{path}: case-folded duplicate citation definitions")

    used_set = set(used_keys)
    if not used_set and definition_map:
        errors.append(f"{path}: unused citation definitions are not allowed")
    for key in sorted(used_set, key=str.casefold):
        citation = catalog[key]
        values = definition_map.get(key, [])
        if len(values) != 1:
            errors.append(f"{path}: citation {key!r} must have exactly one definition")
            continue
        destination, metadata = values[0]
        expected_destination = publisher.citation_destination(citation, path, output_dir)
        expected_metadata = " ".join(citation.metadata.split()).replace('"', "'")
        if destination != expected_destination:
            errors.append(
                f"{path}: citation {key!r} destination {destination!r} is not canonical"
            )
        if metadata != expected_metadata:
            errors.append(f"{path}: citation {key!r} metadata does not match references.csv")
        managed_match = publisher.MANAGED_CITATION_RE.search(text)
        managed = managed_match.group(0) if managed_match else ""
        for required in (
            f"Stable key: `{key}`",
            citation.full_authors,
            citation.full_title,
            citation.full_venue,
        ):
            if required not in managed:
                errors.append(f"{path}: citation {key!r} lacks visible full-reference metadata")
                break
    extras = set(definition_map) - used_set
    if extras:
        errors.append(f"{path}: unused citation definition(s): {', '.join(sorted(extras))}")


def audit_hashes(path: Path, text: str, root: Path, errors: list[str]) -> None:
    for match in HASH_BLOCK_RE.finditer(text):
        for line in match.group(1).splitlines():
            if not line.strip():
                continue
            try:
                relative, expected = line.split("\t", 1)
            except ValueError:
                errors.append(f"{path}: malformed source-hash row {line!r}")
                continue
            source = root / relative
            actual = publisher.sha256(source) if source.is_file() else "MISSING"
            if actual != expected:
                errors.append(
                    f"{path}: stale source hash for {relative}: expected {expected}, current {actual}"
                )


def audit_root_readme(repo_root: Path, errors: list[str]) -> None:
    path = repo_root / "README.md"
    if not path.is_file():
        errors.append("project root README.md is missing")
        return
    source = path.read_text(encoding="utf-8")
    for heading in (
        "## The user value",
        "## Introduction — structure and outline",
        "## At a glance",
        "## Closest prior work",
        "## Planned approach",
        "## Prospective contributions",
        "## Current status",
        "## Continue by task",
        "## Record boundary",
    ):
        if heading not in source:
            errors.append(f"README.md: missing required section {heading!r}")

    level_two_headings = re.findall(r"^##\s+.+$", source, re.MULTILINE)
    if level_two_headings and level_two_headings[0] != "## At a glance":
        errors.append("README.md: At a glance must be the first level-two section")

    for heading in ("At a glance", "The user value"):
        section = re.search(
            rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)",
            source,
            re.MULTILINE | re.DOTALL,
        )
        if section and re.search(
            r"\bshould\b", publisher.strip_code(section.group(1)), re.IGNORECASE
        ):
            errors.append(
                f"README.md: {heading} must state motivation and user value declaratively; "
                "author-voice 'should' belongs only in an attributed recommendation outside "
                "these sections"
            )

    introduction = re.search(
        r"^## Introduction — structure and outline\s*$\n(.*?)(?=^##\s+|\Z)",
        source,
        re.MULTILINE | re.DOTALL,
    )
    introduction_source = introduction.group(1) if introduction else ""
    for label in (
        "Approach invariant",
        "Essential interaction/control-policy dimensions",
        "Implementation substrate / empirical waist",
        "Platform-substitution result",
        "Adaptation-credit disposition",
    ):
        if label not in introduction_source:
            errors.append(f"README.md: Introduction outline lacks {label!r}")

    approach_position = introduction_source.find("Approach invariant")
    substrate_position = introduction_source.find("Implementation substrate / empirical waist")
    if (
        approach_position >= 0
        and substrate_position >= 0
        and approach_position > substrate_position
    ):
        errors.append(
            "README.md: Introduction outline must state the approach invariant before "
            "the implementation substrate / empirical waist"
        )

    profile = re.search(
        r"^<!-- HCI-PLAIN-LANGUAGE: ISO 24495-1:2023 \| "
        r"audience=(?P<audience>[^|\n]+) \| tasks=(?P<tasks>[^>\n]+) -->$",
        source,
        re.MULTILINE,
    )
    if not profile:
        errors.append(
            "README.md: missing ISO 24495-1 HCI-PLAIN-LANGUAGE audience/task profile"
        )
    else:
        audience = profile.group("audience").strip()
        tasks = [task.strip() for task in profile.group("tasks").split(";") if task.strip()]
        placeholders = {"audience", "everyone", "reader", "readers", "tbd", "todo", "unknown"}
        if audience.casefold() in placeholders:
            errors.append("README.md: plain-language audience must name intended readers")
        if len(tasks) < 2 or any(task.casefold() in placeholders for task in tasks):
            errors.append("README.md: plain-language profile must name at least two reader tasks")

    glance = re.search(
        r"^## At a glance\s*$\n(.*?)(?=^##\s+|\Z)",
        source,
        re.MULTILINE | re.DOTALL,
    )
    if glance and not re.search(
        r"\b(established-external|observed-project|planned|hypothesis|aspiration|unsupported)\b",
        glance.group(1),
    ):
        errors.append("README.md: At a glance lacks an explicit evidence-state label")

    onward = re.search(
        r"^## Continue by task\s*$\n(.*?)(?=^##\s+|\Z)",
        source,
        re.MULTILINE | re.DOTALL,
    )
    if onward:
        goals = re.findall(r"^###\s+\S.*$", onward.group(1), re.MULTILINE)
        if len(goals) < 2:
            errors.append("README.md: Continue by task must group links under at least two reader goals")
    if not re.search(
        r"\b(established-external|observed-project|planned|hypothesis|aspiration|unsupported)\b",
        source,
    ):
        errors.append("README.md: high-level framing lacks an explicit evidence-state label")
    for target in REQUIRED_ROOT_LINKS:
        if f"]({target})" not in source:
            errors.append(f"README.md: missing required reader link {target!r}")


def audit_readme_prior_work_context(
    repo_root: Path,
    catalog: dict[str, publisher.Citation],
    errors: list[str],
) -> None:
    path = repo_root / "README.md"
    if not path.is_file():
        return
    source = strip_managed_citations(path.read_text(encoding="utf-8"))
    framing_match = re.search(
        r"^## At a glance\s*$\n(.*?)(?=^##\s+|\Z)", source, re.MULTILINE | re.DOTALL
    )
    if not framing_match:
        return
    closest_match = re.search(
        r"^## Closest prior work\s*$\n(.*?)(?=^##\s+|\Z)",
        source,
        re.MULTILINE | re.DOTALL,
    )
    framing = framing_match.group(1)
    closest = closest_match.group(1) if closest_match else ""
    uses = [
        match.group(2)
        for match in GENERAL_REFERENCE_LINK_RE.finditer(framing + "\n" + closest)
        if match.group(2) in catalog
    ]
    if not uses:
        return
    if not closest_match:
        errors.append(
            "README.md: framing citations require a '## Closest prior work' comparison section"
        )
        return
    entries = [
        match.group(1)
        for match in re.finditer(
            r"(?ms)^-\s+(.*?)(?=^-\s+|^##\s+|\Z)", closest_match.group(1)
        )
    ]
    for key in sorted(set(uses), key=str.casefold):
        matching = [entry for entry in entries if f"][{key}]" in entry]
        if len(matching) != 1:
            errors.append(
                f"README.md: citation {key!r} must have exactly one closest-work comparison bullet"
            )
            continue
        entry = matching[0]
        for marker in ("**What it did:**", "**How this project differs:**"):
            if marker not in entry:
                errors.append(
                    f"README.md: citation {key!r} comparison lacks {marker}"
                )


def audit(
    root: Path,
    output_dir: Path | None = None,
) -> tuple[list[str], list[str]]:
    root = root.resolve()
    repo_root = root.parent
    output_dir = (output_dir or root / "reports").resolve()
    errors: list[str] = []
    warnings: list[str] = []
    try:
        catalog = publisher.load_citation_catalog(root)
    except ValueError as exc:
        return [str(exc)], warnings

    audit_root_readme(repo_root, errors)
    audit_readme_prior_work_context(repo_root, catalog, errors)
    audit_phase_completion(root, errors)

    legacy_html = sorted(output_dir.rglob("*.html")) if output_dir.is_dir() else []
    for path in legacy_html:
        errors.append(f"stale generated HTML must be removed: {path}")

    for name in sorted(expected_report_names()):
        path = output_dir / name
        if not path.is_file():
            errors.append(f"missing required Markdown report: {path}")
        elif publisher.GENERATED_MARKER not in path.read_text(encoding="utf-8"):
            errors.append(f"{path}: missing generated-publication marker")

    markdown_paths = []
    root_readme = repo_root / "README.md"
    if root_readme.is_file():
        markdown_paths.append(root_readme)
    markdown_paths.extend(sorted(root.rglob("*.md")))
    for path in markdown_paths:
        text = path.read_text(encoding="utf-8")
        if path != root_readme and not (
            publisher.NAV_START in text and publisher.NAV_END in text
        ):
            errors.append(f"{path}: missing managed Phase 1 navigation block")
        html_scan = re.sub(
            r"https?://[^\s)>]+",
            "",
            publisher.strip_code(text),
            flags=re.IGNORECASE,
        )
        # HTML files under a figures/ directory are canonical figure artifacts,
        # not legacy HTML report views; only non-figure HTML references are errors.
        html_scan = re.sub(r"[^\s|()\[\]]*figures/[^\s|()\[\]]*\.html", "", html_scan)
        if re.search(r"\.html(?:[#?)\s]|$)", html_scan, re.IGNORECASE):
            errors.append(f"{path}: contains a legacy HTML report reference")
        audit_citations(path, text, catalog, output_dir, repo_root, errors)
        audit_hashes(path, text, root, errors)
        for match in INLINE_LINK_RE.finditer(publisher.strip_code(text)):
            audit_link(path, parse_inline_target(match.group(1)), repo_root, errors)

    progress = output_dir / "phase-1-progress.md"
    if progress.is_file():
        source = progress.read_text(encoding="utf-8")
        first = source.find("## Current state — read this first")
        later = source.find("## Canonical records")
        if first < 0 or later < 0 or first > later:
            errors.append("phase-1-progress.md: current-state section is not first")
        for required in (
            "phase-1-collaboration-workboard.md",
            "author-decisions.md",
            "missing-full-copies.md",
        ):
            if required not in source:
                errors.append(f"phase-1-progress.md: missing decision-state link {required}")

    literature = output_dir / "literature-and-evidence.md"
    if literature.is_file():
        source = literature.read_text(encoding="utf-8")
        for required in (
            "source-resolution.md",
            "evidence-strength-register.md",
            "ranked-related-work-positioning.md",
            "prior-work-evidence-accounting.csv",
            "idea-provenance-ledger.csv",
            "missing-full-copies.md",
        ):
            if required not in source:
                errors.append(f"literature-and-evidence.md: missing evidence link {required}")

    return errors, warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit Phase 1 GitHub Markdown publication files.")
    parser.add_argument("project_dir", type=Path, help="research-framing directory")
    parser.add_argument("--output-dir", type=Path, help="output directory (default: PROJECT/reports)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.project_dir.expanduser().resolve()
    errors, warnings = audit(
        root,
        args.output_dir.expanduser().resolve() if args.output_dir else None,
    )
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: audited Phase 1 Markdown publication in {root / 'reports'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
