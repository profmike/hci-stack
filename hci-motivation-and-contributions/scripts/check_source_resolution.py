#!/usr/bin/env python3
"""Fail closed on unresolved sources and unstable retained-source identity."""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path


REQUIRED_COLUMNS = (
    "source_id",
    "citation_key",
    "bibliographic_identity",
    "canonical_url",
    "source_provenance",
    "candidate_role",
    "relevance",
    "acquisition_state",
    "full_copy_locator",
    "full_text_review_locator",
    "evidence_register_locator",
    "upgrade_search",
    "superseded_by",
    "attempted_routes",
    "exact_author_action",
    "request_surfaced_date",
    "request_surfaced_locator",
    "affected_claims",
    "fallback_or_narrowing",
    "reopen_trigger",
    "terminal_reason",
    "next_action",
    "identity_verified_against",
)

ALLOWED_RELEVANCE = {"retain", "exclude", "undecided"}
TRANSIENT_STATES = {"DISCOVERED", "ACQUIRING", "FULL_TEXT_OBTAINED"}
TERMINAL_STATES = {
    "FULL_TEXT_ASSESSED",
    "NEEDS_AUTHOR_SOURCE_ACCESS",
    "SCREENED_OUT",
    "SUPERSEDED",
}
ALLOWED_STATES = TRANSIENT_STATES | TERMINAL_STATES
CLAIM_ID_DELIMITER = "||"
PLACEHOLDER_VALUES = {
    "",
    "-",
    "n/a",
    "na",
    "no",
    "none",
    "not yet",
    "pending",
    "tbd",
    "todo",
    "unknown",
}


def require_fields(
    row: dict[str, str],
    fields: tuple[str, ...],
    row_number: int,
    state: str,
) -> list[str]:
    return [
        f"row {row_number} ({row.get('source_id') or 'missing source_id'}): "
        f"{state} requires {field}"
        for field in fields
        if not row.get(field, "").strip()
    ]


def is_placeholder(value: str) -> bool:
    normalized = unicodedata.normalize("NFKC", value).strip().casefold()
    while normalized and (
        normalized[0].isspace()
        or unicodedata.category(normalized[0])[0] in {"P", "S"}
        or unicodedata.category(normalized[0]) == "Cf"
    ):
        normalized = normalized[1:]
    while normalized and (
        normalized[-1].isspace()
        or unicodedata.category(normalized[-1])[0] in {"P", "S"}
        or unicodedata.category(normalized[-1]) == "Cf"
    ):
        normalized = normalized[:-1]
    normalized = re.sub(r"[-_]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized in PLACEHOLDER_VALUES


def placeholder_locator_component(value: str) -> bool:
    """Detect placeholders hidden inside an otherwise plausible locator."""
    normalized = value.strip()
    if not normalized or is_placeholder(normalized):
        return True

    base, separator, anchor = normalized.rpartition("#")
    if separator:
        if not anchor or is_placeholder(anchor):
            return True
        normalized = base

    scheme_match = re.fullmatch(
        r"(?P<scheme>[A-Za-z][A-Za-z0-9+.-]*):(?P<payload>.*)",
        normalized,
    )
    if scheme_match:
        scheme = scheme_match.group("scheme").casefold()
        payload = scheme_match.group("payload").strip()
        if not payload or is_placeholder(payload):
            return True
        if scheme in {"http", "https"}:
            return False
        normalized = payload

    final_path_component = normalized.rstrip("/").rsplit("/", 1)[-1]
    return not final_path_component or is_placeholder(final_path_component)


def reject_placeholder_fields(
    row: dict[str, str],
    fields: tuple[str, ...],
    row_number: int,
    state: str,
    *,
    locator_fields: tuple[str, ...] = (),
) -> list[str]:
    errors: list[str] = []
    for field in fields:
        value = row.get(field, "")
        if not value:
            continue
        invalid = (
            placeholder_locator_component(value)
            if field in locator_fields
            else is_placeholder(value)
        )
        if invalid:
            errors.append(
                f"row {row_number} ({row.get('source_id') or 'missing source_id'}): "
                f"{state} cannot use placeholder value '{value}' for {field}"
            )
    return errors


def valid_surfaced_date(value: str) -> bool:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        surfaced = date.fromisoformat(value)
    except ValueError:
        return False
    return surfaced <= date.today()


def valid_surfaced_locator(value: str) -> bool:
    normalized = value.strip()
    if is_placeholder(normalized) or placeholder_locator_component(normalized):
        return False
    return bool(
        re.fullmatch(
            r"(?:session|conversation|thread|chat|governed):\S+",
            normalized,
            flags=re.IGNORECASE,
        )
        or re.fullmatch(r"\S+\.md#[^\s#]+", normalized, flags=re.IGNORECASE)
    )


def load_claim_ids(path: Path) -> tuple[set[str], list[str]]:
    if not path.is_file():
        return set(), [f"claim-evidence ledger not found: {path}"]

    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if "claim_id" not in tuple(reader.fieldnames or ()):
            return set(), [f"claim-evidence ledger is missing claim_id column: {path}"]
        claim_ids: set[str] = set()
        errors: list[str] = []
        for index, row in enumerate(reader, start=2):
            claim_id = (row.get("claim_id") or "").strip()
            if not claim_id:
                continue
            if claim_id in claim_ids:
                errors.append(
                    f"claim-evidence ledger has duplicate claim_id '{claim_id}' "
                    f"at row {index}"
                )
                continue
            claim_ids.add(claim_id)
    return claim_ids, errors


def parse_affected_claim_ids(value: str) -> tuple[list[str], list[str]]:
    parts = [part.strip() for part in value.split(CLAIM_ID_DELIMITER)]
    errors: list[str] = []
    if any(not part for part in parts):
        errors.append(
            f"affected_claims must be nonempty stable IDs separated by "
            f"'{CLAIM_ID_DELIMITER}'"
        )
    for claim_id in parts:
        if claim_id and not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]*", claim_id):
            errors.append(
                f"affected_claims entry '{claim_id}' is not a stable claim ID; "
                f"separate IDs with '{CLAIM_ID_DELIMITER}'"
            )
    return [part for part in parts if part], errors


def load_reference_registry(path: Path) -> tuple[dict[str, str], list[str]]:
    if not path.is_file():
        return {}, [f"phase-ready citation registry not found: {path}"]

    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        missing = [
            column
            for column in ("citation_key", "url")
            if column not in tuple(reader.fieldnames or ())
        ]
        if missing:
            return {}, [
                "phase-ready citation registry is missing column(s): "
                + ", ".join(missing)
                + f": {path}"
            ]
        registry: dict[str, str] = {}
        errors: list[str] = []
        for index, row in enumerate(reader, start=2):
            key = (row.get("citation_key") or "").strip()
            if not key:
                continue
            url = (row.get("url") or "").strip()
            if key in registry:
                errors.append(
                    f"phase-ready citation registry has duplicate citation_key "
                    f"'{key}' at row {index}"
                )
                continue
            if not url.startswith(("http://", "https://", "internal:")):
                errors.append(
                    f"phase-ready citation registry row {index} ({key}) cannot be "
                    "classified: url must be HTTP(S) external evidence or internal: "
                    "project evidence"
                )
            registry[key] = url
    return registry, errors


DOI_PATTERN = re.compile(r"10\.\d{4,9}/[^\s|,;\"'<>)\]]+")


def extract_doi(text: str) -> str:
    """Return the first DOI in ``text``, normalized for comparison."""
    match = DOI_PATTERN.search(text or "")
    if not match:
        return ""
    return match.group(0).rstrip(".").lower()


def check_imported_identifier_agreement(
    path: Path,
    rows: list[dict[str, str]],
) -> list[str]:
    """Fail when an imported bibliography row and its resolution row disagree on the DOI.

    A supplied bibliography is a discovery seed, so neither side is authoritative on its
    own. A disagreement means one of the two was transcribed wrong, and a wrong DOI sends
    the author to the wrong paper. Resolve it against the obtained full copy, then make
    both records say the same thing.
    """
    imported_path = path.parent / "imported-bibliography-accountability.csv"
    if not imported_path.is_file():
        return []

    by_source_id = {row["source_id"]: row for row in rows if row.get("source_id")}
    by_citation_key: dict[str, dict[str, str]] = {}
    for row in rows:
        key = row.get("citation_key") or ""
        if key and key not in by_citation_key:
            by_citation_key[key] = row

    errors: list[str] = []
    with imported_path.open(newline="", encoding="utf-8-sig") as handle:
        for index, raw in enumerate(csv.DictReader(handle), start=2):
            record = {
                column: (value or "").strip() for column, value in raw.items() if column
            }
            imported_doi = extract_doi(record.get("bibliographic_identity", ""))
            if not imported_doi:
                continue
            resolution = by_source_id.get(record.get("source_resolution_id", ""))
            if resolution is None:
                resolution = by_citation_key.get(record.get("citation_key", ""))
            if resolution is None:
                continue
            resolved_doi = extract_doi(resolution.get("canonical_url", ""))
            if not resolved_doi or resolved_doi == imported_doi:
                continue
            if resolved_doi.startswith(imported_doi) or imported_doi.startswith(
                resolved_doi
            ):
                # A book DOI against one of its chapter DOIs is a granularity choice,
                # not a transcription error. Record which artifact is held; do not fail.
                continue
            label = record.get("accountability_id") or f"row {index}"
            errors.append(
                f"imported bibliography {label} and source-resolution row "
                f"{resolution['source_id']} ({resolution.get('citation_key', '')}) "
                f"disagree on the DOI: imported '{imported_doi}' against resolved "
                f"'{resolved_doi}'. One of them is a transcription error and it will "
                "send the author to the wrong paper. Resolve it against the obtained "
                "full copy or a registry lookup, then correct both records"
            )
    return errors


SOURCE_ID_PATTERN = re.compile(r"\bSR-\d{2,4}\b")


def check_access_queue_agreement(
    path: Path,
    rows: list[dict[str, str]],
) -> list[str]:
    """Fail when the author-facing access queue still asks for an obtained source.

    ``missing-full-copies.md`` is the page an author actually works from. When a row
    resolves in the ledger but its prose section is never updated, the queue keeps asking
    for a paper that is already in the corpus, and the author spends a library trip on it.
    """
    queue_path = path.parent / "missing-full-copies.md"
    if not queue_path.is_file():
        return []

    state_by_id = {
        row["source_id"]: row["acquisition_state"].upper()
        for row in rows
        if row.get("source_id")
    }
    text = queue_path.read_text(encoding="utf-8")
    errors: list[str] = []
    for line in text.splitlines():
        if not line.lstrip().startswith("#"):
            continue
        for source_id in SOURCE_ID_PATTERN.findall(line):
            state = state_by_id.get(source_id)
            if state and state != "NEEDS_AUTHOR_SOURCE_ACCESS":
                errors.append(
                    f"missing-full-copies.md still carries a section for {source_id}, "
                    f"but its source-resolution state is {state}. An author reading this "
                    "queue would be sent after a source that is already resolved: close "
                    "the section and record how it resolved"
                )
    return errors


BROADCAST_PAGES = ("source-manifest.md", "missing-full-copies.md")


def check_identifier_broadcast_agreement(
    path: Path,
    rows: list[dict[str, str]],
) -> list[str]:
    """Fail when an author-facing page prints a different DOI than the ledger holds.

    Every DOI an author acts on is copied out of the ledger into prose: a manifest row, an
    access-request table, a reading list. Those copies do not update themselves. A stale or
    mistyped copy sends the author to the wrong article and the error is invisible until
    the wrong PDF arrives, so each printed DOI is checked back against its source row.

    A line may quote a superseded identifier on purpose when it is recording the correction.
    Such a line must say so, using the word ``CORRECTION``, and it is then exempt.
    """
    def normalize(doi: str) -> str:
        """A DOI is case-insensitive, and prose wraps it in punctuation."""
        return doi.strip().rstrip(".,;:)]}`'\"").casefold()

    doi_by_id: dict[str, str] = {}
    doi_by_key: dict[str, str] = {}
    for row in rows:
        doi = normalize(extract_doi(row.get("canonical_url", "")))
        if not doi:
            continue
        if row.get("source_id"):
            doi_by_id[row["source_id"]] = doi
        if row.get("citation_key"):
            doi_by_key[row["citation_key"]] = doi

    errors: list[str] = []
    for page in BROADCAST_PAGES:
        page_path = path.parent / page
        if not page_path.is_file():
            continue
        for number, line in enumerate(page_path.read_text(encoding="utf-8").splitlines(), 1):
            if "CORRECTION" in line:
                continue
            if line.lstrip().startswith("|"):
                # A generated table row already agrees with the ledger by construction, and
                # check_source_manifest_generated is what proves it. Such a row also carries
                # long ledger prose that legitimately names OTHER works' identifiers — an
                # upgrade search that cites the stronger source it compared against, for
                # instance — which this line-scoped check would misread as the row's own.
                continue
            printed = {normalize(doi) for doi in DOI_PATTERN.findall(line)}
            if not printed:
                continue
            expected = {
                doi_by_id[source_id]
                for source_id in SOURCE_ID_PATTERN.findall(line)
                if source_id in doi_by_id
            }
            expected |= {
                doi for key, doi in doi_by_key.items() if key and key in line
            }
            if not expected:
                continue
            stray = printed - expected
            if stray:
                errors.append(
                    f"{page}:line {number}: prints DOI(s) {', '.join(sorted(stray))} for a "
                    f"source whose ledger DOI is {', '.join(sorted(expected))}. An author "
                    "acting on this page would fetch the wrong article: correct the page, or "
                    "mark the line as a recorded CORRECTION"
                )
    return errors


# A recorded identity check has to name where in the held copy it was read. These tokens are
# what a real locator looks like; a bare date or a bare "yes" is not one.
IDENTITY_LOCATOR_PATTERN = re.compile(
    r"\b(p{1,2}\.?\s*\d|page\s*\d|pp\b|title page|first page|front matter|cover sheet|"
    r"masthead|byline|colophon|§|section\s|abstract page|running head)",
    re.IGNORECASE,
)


def check_identity_verification(rows: list[dict[str, str]]) -> list[str]:
    """Fail when a held full copy's identity was never read off the copy itself.

    Wrong authors, wrong titles, and wrong page ranges enter a project the same way every
    time: someone types the identity out of a bibliography, a database record, or another
    paper's reference list, and nobody ever opens the held PDF's own front matter to
    contradict it. Those errors survive every consistency check, because every copy of the
    identity descends from the same bad transcription.

    A row that holds a full copy therefore has to record where in that copy the identity was
    read: a page, a title page, a masthead. The DOI checks compare copies of a value against
    each other; this one is the only check that reaches the paper.

    A source whose copy is an unsearchable scan is not exempt. Record that it was read
    visually and name the page.
    """
    errors: list[str] = []
    for index, row in enumerate(rows, start=2):
        if not row.get("full_copy_locator", "").strip():
            continue
        source_id = row.get("source_id") or f"row {index}"
        recorded = row.get("identity_verified_against", "").strip()
        if is_placeholder(recorded):
            errors.append(
                f"{source_id}: a full copy is held but identity_verified_against is empty. "
                "Open the copy, read its own front matter, and record where the authors, "
                "title, year, venue, and pages were read, for example "
                "'held copy p.1 title page, 2026-08-05'. Never copy an identity out of "
                "another work's bibliography"
            )
        elif not IDENTITY_LOCATOR_PATTERN.search(recorded):
            errors.append(
                f"{source_id}: identity_verified_against is {recorded!r}, which names no "
                "place in the held copy. Record the page or front-matter element the "
                "identity was read from, for example 'held copy p.1 byline'"
            )
    return errors


def check_source_manifest_generated(path: Path) -> list[str]:
    """Fail when the manifest's ledger-derived columns disagree with the ledger.

    The manifest used to hold a hand-typed second copy of every identifier. Those columns
    are generated now, by ``render_source_manifest.py``. This check runs the same derivation
    and reports any cell that has drifted, so the duplicate cannot come back.
    """
    manifest = path.parent / "source-manifest.md"
    if not manifest.is_file():
        return []
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from render_source_manifest import render  # noqa: PLC0415
    except Exception as error:  # pragma: no cover - defensive
        return [f"could not load render_source_manifest.py: {error}"]
    try:
        _, changes = render(path.parent)
    except SystemExit as error:
        return [f"source-manifest.md could not be rendered: {error}"]
    if not changes:
        return []
    return [
        "source-manifest.md disagrees with source-resolution.csv in "
        f"{len(changes)} place(s); the manifest's ledger-derived columns are generated. "
        "Run render_source_manifest.py to regenerate them. First disagreement: "
        + changes[0]
    ]


def validate(
    path: Path,
    *,
    end_of_round: bool = False,
    phase_ready: bool = False,
) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.is_file():
        return [f"source-resolution queue not found: {path}"], warnings, 0

    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        fieldnames = tuple(reader.fieldnames or ())
        missing = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
        if missing:
            detail = ""
            if "identity_verified_against" in missing:
                detail = (
                    " Add the 'identity_verified_against' column and, for every row that "
                    "holds a full copy, record where in that copy the identity was read, "
                    "for example 'held copy p.1 title page, 2026-08-05'. An identity typed "
                    "out of another work's bibliography is how wrong authors, titles, and "
                    "page ranges enter a project unchallenged."
                )
            return [
                "source-resolution queue is missing required column(s): "
                + ", ".join(missing)
                + detail
            ], warnings, 0
        rows = [
            {column: (value or "").strip() for column, value in row.items()}
            for row in reader
            if any((value or "").strip() for value in row.values())
        ]

    reference_registry: dict[str, str] = {}
    if phase_ready:
        reference_registry, reference_errors = load_reference_registry(
            path.parent / "references.csv"
        )
        errors.extend(reference_errors)

    claim_ids: set[str] = set()
    if (end_of_round or phase_ready) and any(
        row["acquisition_state"].upper() == "NEEDS_AUTHOR_SOURCE_ACCESS"
        for row in rows
    ):
        claim_ids, claim_errors = load_claim_ids(
            path.parent / "claim-evidence-ledger.csv"
        )
        errors.extend(claim_errors)

    seen_ids: set[str] = set()
    seen_citation_keys: set[str] = set()
    for index, row in enumerate(rows, start=2):
        source_id = row["source_id"]
        if not source_id:
            errors.append(f"row {index}: source_id is required")
        elif source_id in seen_ids:
            errors.append(f"row {index}: duplicate source_id '{source_id}'")
        else:
            seen_ids.add(source_id)

        citation_key = row["citation_key"]
        if citation_key:
            if citation_key in seen_citation_keys:
                errors.append(
                    f"row {index} ({source_id or 'missing source_id'}): duplicate "
                    f"citation_key '{citation_key}'"
                )
            else:
                seen_citation_keys.add(citation_key)

        errors.extend(
            require_fields(
                row,
                (
                    "bibliographic_identity",
                    "canonical_url",
                    "source_provenance",
                    "candidate_role",
                    "relevance",
                    "acquisition_state",
                ),
                index,
                row["acquisition_state"] or "source record",
            )
        )

        relevance = row["relevance"].lower()
        if relevance and relevance not in ALLOWED_RELEVANCE:
            errors.append(
                f"row {index} ({source_id}): invalid relevance '{row['relevance']}'"
            )

        state = row["acquisition_state"].upper()
        if state == "UNASSESSED":
            errors.append(
                f"row {index} ({source_id}): UNASSESSED is not a source-resolution state; "
                "acquire and review the full text or surface an exact author-access request"
            )
            continue
        if state and state not in ALLOWED_STATES:
            errors.append(
                f"row {index} ({source_id}): invalid acquisition_state "
                f"'{row['acquisition_state']}'"
            )
            continue

        if state in TRANSIENT_STATES:
            errors.extend(require_fields(row, ("next_action",), index, state))
            if end_of_round or phase_ready:
                errors.append(
                    f"row {index} ({source_id}): cannot end the round with transient "
                    f"state {state}"
                )
        elif state == "FULL_TEXT_ASSESSED":
            locator_fields = (
                "full_copy_locator",
                "full_text_review_locator",
                "evidence_register_locator",
            )
            errors.extend(
                require_fields(
                    row,
                    locator_fields,
                    index,
                    state,
                )
            )
            errors.extend(
                reject_placeholder_fields(
                    row,
                    locator_fields,
                    index,
                    state,
                    locator_fields=locator_fields,
                )
            )
            if relevance == "undecided":
                errors.append(
                    f"row {index} ({source_id}): FULL_TEXT_ASSESSED requires a retain "
                    "or exclude relevance decision"
                )
            if relevance == "retain":
                errors.extend(
                    require_fields(
                        row,
                        ("citation_key", "upgrade_search"),
                        index,
                        state,
                    )
                )
                errors.extend(
                    reject_placeholder_fields(
                        row,
                        ("citation_key", "upgrade_search"),
                        index,
                        state,
                    )
                )
                citation_key = row["citation_key"]
                if (
                    phase_ready
                    and citation_key
                    and citation_key not in reference_registry
                ):
                    errors.append(
                        f"row {index} ({source_id}): retained citation_key "
                        f"'{citation_key}' is absent from references.csv"
                    )
        elif state == "NEEDS_AUTHOR_SOURCE_ACCESS":
            errors.extend(
                require_fields(
                    row,
                    (
                        "attempted_routes",
                        "exact_author_action",
                        "request_surfaced_date",
                        "request_surfaced_locator",
                        "affected_claims",
                        "fallback_or_narrowing",
                        "reopen_trigger",
                        "next_action",
                    ),
                    index,
                    state,
                )
            )
            if not valid_surfaced_date(row["request_surfaced_date"]):
                errors.append(
                    f"row {index} ({source_id}): NEEDS_AUTHOR_SOURCE_ACCESS requires "
                    "request_surfaced_date as an actual, non-future YYYY-MM-DD date"
                )
            if not valid_surfaced_locator(row["request_surfaced_locator"]):
                errors.append(
                    f"row {index} ({source_id}): NEEDS_AUTHOR_SOURCE_ACCESS requires "
                    "request_surfaced_locator as a session/conversation/thread/chat/governed "
                    "locator or a Markdown heading locator"
                )
            errors.extend(
                reject_placeholder_fields(
                    row,
                    (
                        "attempted_routes",
                        "exact_author_action",
                        "affected_claims",
                        "fallback_or_narrowing",
                        "reopen_trigger",
                        "next_action",
                    ),
                    index,
                    state,
                )
            )
            if (end_of_round or phase_ready) and row["affected_claims"]:
                affected_ids, affected_errors = parse_affected_claim_ids(
                    row["affected_claims"]
                )
                errors.extend(
                    f"row {index} ({source_id}): {error}"
                    for error in affected_errors
                )
                for claim_id in affected_ids:
                    if claim_id not in claim_ids:
                        errors.append(
                            f"row {index} ({source_id}): affected claim ID "
                            f"'{claim_id}' is absent from claim-evidence-ledger.csv"
                        )
            if phase_ready:
                errors.append(
                    f"row {index} ({source_id}): phase-ready status cannot retain "
                    "NEEDS_AUTHOR_SOURCE_ACCESS"
                )
        elif state == "SCREENED_OUT":
            errors.extend(require_fields(row, ("terminal_reason",), index, state))
            errors.extend(
                reject_placeholder_fields(
                    row,
                    ("terminal_reason",),
                    index,
                    state,
                )
            )
            if relevance != "exclude":
                errors.append(
                    f"row {index} ({source_id}): SCREENED_OUT requires relevance=exclude"
                )
        elif state == "SUPERSEDED":
            errors.extend(
                require_fields(
                    row,
                    ("terminal_reason", "superseded_by"),
                    index,
                    state,
                )
            )
            errors.extend(
                reject_placeholder_fields(
                    row,
                    ("terminal_reason", "superseded_by"),
                    index,
                    state,
                )
            )
            if relevance != "exclude":
                errors.append(
                    f"row {index} ({source_id}): SUPERSEDED requires relevance=exclude"
                )

    identifier_rows: dict[str, list[tuple[int, dict[str, str]]]] = {}
    for index, row in enumerate(rows, start=2):
        for identifier in (row["source_id"], row["citation_key"]):
            if identifier:
                matches = identifier_rows.setdefault(identifier, [])
                if not any(existing_index == index for existing_index, _ in matches):
                    matches.append((index, row))

    for index, row in enumerate(rows, start=2):
        if row["acquisition_state"].upper() != "SUPERSEDED":
            continue
        source_id = row["source_id"]
        replacement = row["superseded_by"]
        if not replacement:
            continue
        matches = identifier_rows.get(replacement, [])
        if not matches:
            errors.append(
                f"row {index} ({source_id}): superseded_by '{replacement}' does not "
                "resolve to a source_id or citation_key in source-resolution.csv"
            )
            continue
        if len(matches) > 1:
            errors.append(
                f"row {index} ({source_id}): superseded_by '{replacement}' is ambiguous "
                "in source-resolution.csv"
            )
            continue
        replacement_index, replacement_row = matches[0]
        if replacement_index == index:
            errors.append(
                f"row {index} ({source_id}): SUPERSEDED cannot point superseded_by "
                "to itself"
            )
            continue
        replacement_state = replacement_row["acquisition_state"].upper()
        replacement_relevance = replacement_row["relevance"].lower()
        if replacement_state != "FULL_TEXT_ASSESSED" or replacement_relevance != "retain":
            errors.append(
                f"row {index} ({source_id}): superseded_by '{replacement}' must resolve "
                "to a retained FULL_TEXT_ASSESSED source, not "
                f"{replacement_state or 'missing state'}/{replacement_relevance or 'missing relevance'}"
            )
        if not replacement_row["citation_key"]:
            errors.append(
                f"row {index} ({source_id}): superseded_by '{replacement}' must resolve "
                "to a source with a stable citation_key"
            )

    errors.extend(check_imported_identifier_agreement(path, rows))
    errors.extend(check_access_queue_agreement(path, rows))
    errors.extend(check_identifier_broadcast_agreement(path, rows))
    errors.extend(check_identity_verification(rows))
    errors.extend(check_source_manifest_generated(path))

    if phase_ready and not rows:
        errors.append("phase-ready source-resolution queue has no source records")
    if phase_ready:
        external_keys = {
            key
            for key, url in reference_registry.items()
            if url.startswith(("http://", "https://"))
        }
        ledger_keys = {row["citation_key"] for row in rows if row["citation_key"]}
        for citation_key in sorted(external_keys - ledger_keys):
            errors.append(
                "phase-ready external citation_key "
                f"'{citation_key}' is absent from source-resolution.csv; every external "
                "research reference needs an explicit acquisition/disposition row"
            )

    return errors, warnings, len(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate Phase 1 source resolution and retained-source identity."
    )
    parser.add_argument(
        "project_dir",
        type=Path,
        help="Research-framing directory containing source-resolution.csv",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--end-of-round",
        action="store_true",
        help=(
            "Reject transient states before a declared bounded audit or research-round closure; "
            "not for an in-progress status update."
        ),
    )
    mode.add_argument(
        "--phase-ready",
        action="store_true",
        help="Also reject unresolved author-access requests before Phase 1 readiness.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = args.project_dir / "source-resolution.csv"
    errors, warnings, count = validate(
        path,
        end_of_round=args.end_of_round or args.phase_ready,
        phase_ready=args.phase_ready,
    )
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print(f"PASS: {count} source-resolution record(s) validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
