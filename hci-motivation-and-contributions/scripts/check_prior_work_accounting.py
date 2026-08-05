#!/usr/bin/env python3
"""Validate exclusion-first prior-work evidence and novelty accounting."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


ACCOUNTING_FILE = "prior-work-evidence-accounting.csv"
IDEA_FILE = "idea-provenance-ledger.csv"
IMPORTED_FILE = "imported-bibliography-accountability.csv"
LATE_FILE = "late-found-work-postmortem.csv"
SENTINEL_FILE = "novelty-regression-sentinels.yaml"
BOUNDARY_FILE = "prior-work-contribution-boundary.md"
SOURCE_RESOLUTION_FILE = "source-resolution.csv"

ACCOUNTING_COLUMNS = (
    "record_id",
    "work_id",
    "source_id",
    "citation_key",
    "proposition_type",
    "atomic_proposition",
    "unit_kind",
    "smallest_operated_unit",
    "channel_id",
    "input_or_signal",
    "mapped_command_or_effect",
    "generalization_boundary",
    "author_claim_status",
    "author_claim_evidence",
    "author_claim_locator",
    "demonstration_status",
    "demonstrated_artifact_or_study",
    "demonstration_evidence",
    "demonstration_locator",
    "operated_capability_status",
    "operated_capability",
    "operation_evidence",
    "operation_locator",
    "evaluated_result_status",
    "evaluated_result",
    "evaluation_design_or_measure",
    "evaluation_locator",
    "evidence_granularity",
    "causal_attribution_scope",
    "capability_collision",
    "collision_atom",
    "collision_scope",
    "collision_evidence_locator",
    "contribution_credit",
    "contribution_atom",
    "credit_basis",
    "credit_scope",
    "credit_evidence_locator",
    "attribution_status",
    "port_status",
    "port_credit_gate",
    "classification_scope",
    "required_channel_set",
    "qualified_channel_set",
    "source_silence_disposition",
    "search_priority_or_reopen_query",
    "reopen_trigger",
)

IDEA_COLUMNS = (
    "idea_id",
    "work_id",
    "source_id",
    "citation_key",
    "idea_type",
    "idea_text",
    "source_wording",
    "locator",
    "provenance_scope",
    "first_idea_language_consequence",
    "capability_collision",
    "contribution_credit",
    "prohibited_use",
    "reopen_trigger",
)

IMPORTED_COLUMNS = (
    "accountability_id",
    "supplied_artifact",
    "bibliographic_identity",
    "citation_key",
    "potential_relevance",
    "independent_discovery_route",
    "source_resolution_id",
    "terminal_disposition",
    "terminal_reason",
    "full_copy_locator",
    "evidence_accounting_ids",
    "upgrade_search",
    "stronger_or_counter_source",
    "superseded_by",
    "exact_author_access_action",
    "affected_claims",
    "reopen_trigger",
)

LATE_COLUMNS = (
    "incident_id",
    "late_found_source_id",
    "citation_key",
    "discovery_date",
    "material_boundary_changed",
    "affected_claim_ids",
    "route_that_should_have_found_it",
    "process_failure",
    "sibling_seed_ids",
    "sibling_records_screened",
    "query_or_graph_repair",
    "affected_claim_rerun",
    "regression_sentinel_id",
    "source_resolution_state",
    "completed_date",
    "status",
)

PROPOSITION_TYPES = {
    "ARTIFACT_CAPABILITY",
    "TECHNICAL_PERFORMANCE",
    "HUMAN_EXPERIENCE_OR_OUTCOME",
    "EMPIRICAL_KNOWLEDGE",
    "DESIGN_KNOWLEDGE",
    "METHODOLOGICAL_KNOWLEDGE",
    "THEORETICAL_KNOWLEDGE",
    "OPEN_RESOURCE",
}
UNIT_KINDS = {
    "COMMAND",
    "PARAMETER",
    "INPUT_CHANNEL",
    "REWARD_CHANNEL",
    "CONFIGURATION",
    "CONDITION",
    "EVALUATED_FINDING",
}
EVIDENCE_STATUSES = {"YES", "NO", "PARTIAL", "UNRESOLVED", "N/A"}
COLLISION_STATUSES = {"EXACT", "PARTIAL", "NONE", "UNRESOLVED"}
CREDIT_STATUSES = {"FULL", "PARTIAL", "NONE", "UNRESOLVED"}
ATTRIBUTION_STATUSES = {
    "CLAIMED_AND_DEMONSTRATED",
    "DEMONSTRATED_UNCLAIMED",
    "CLAIMED_UNDEMONSTRATED",
    "NEITHER",
    "UNRESOLVED",
}
EVIDENCE_GRANULARITIES = {
    "ATOMIC_OPERATION",
    "PACKAGE_CONDITION",
    "EMPIRICAL_FINDING",
    "DESIGN_KNOWLEDGE",
    "THEORETICAL_KNOWLEDGE",
    "RESOURCE",
}
CAUSAL_SCOPES = {"ATOMIC", "PACKAGE_ONLY", "NOT_APPLICABLE", "UNRESOLVED"}
PORT_STATUSES = {"NOT_A_PORT", "PORT_ONLY", "ADAPTATION_CANDIDATE"}
PORT_GATES = {
    "NONE",
    "DEMONSTRATED_NONTRIVIAL_ADAPTATION",
    "DEMONSTRATED_NEW_USE_CLASS",
    "DIRECTLY_VALIDATED_EMPIRICAL_FINDING",
}
CLASSIFICATION_SCOPES = {"ATOMIC_CHANNEL", "PACKAGE_ONLY", "WHOLE_SYSTEM"}
SILENCE_DISPOSITIONS = {"NOT_USED", "SEARCH_PRIORITY", "REOPEN_QUERY"}
IDEA_TYPES = {
    "IDEA",
    "PROPOSAL",
    "FUTURE_WORK",
    "HYPOTHETICAL_SCENARIO",
    "INTERPRETATION",
    "UNVERIFIED_IMPLEMENTATION_CLAIM",
}
RELEVANCE_STATUSES = {"MATERIAL", "NOT_MATERIAL", "UNRESOLVED"}
TERMINAL_DISPOSITIONS = {
    "FULL_TEXT_ASSESSED",
    "SCREENED_OUT",
    "SUPERSEDED",
    "NEEDS_AUTHOR_SOURCE_ACCESS",
}
LATE_STATUSES = {"OPEN", "COMPLETE"}
COMPLETION_MARKERS = (
    "IMPORTED_BIBLIOGRAPHY_ACCOUNTED",
    "CLAIM_DEMONSTRATION_OPERATION_EVALUATION_DECOMPOSED",
    "CAPABILITY_COLLISION_AND_CREDIT_SEPARATED",
    "HUMAN_ACTIVITY_PREDICATES_AND_COLLISION_LEVELS_CHECKED",
    "NO_COMPONENT_SUBTRACTION_FALLACY",
    "DEMONSTRATED_UNCLAIMED_OPERATIONS_REVIEWED",
    "MIXED_CHANNELS_DECOMPOSED",
    "PORT_CREDIT_GATES_APPLIED",
    "NO_PROPOSAL_GRANTED_CAPABILITY_CREDIT",
    "NO_SILENCE_DERIVED_CAPABILITY_OR_ABSENCE",
    "LATE_FOUND_WORK_REPAIR_COMPLETE",
    "NOVELTY_REGRESSION_SENTINELS_RECHECKED",
    "ZERO_YIELD_PROMOTION_WAVE_COMPLETE",
)

POSITIVE = {"YES", "PARTIAL"}
EQUIVALENCE_CLAIM = re.compile(
    r"\b(equivalent|equivalence|comparable|maintain(?:ed|s)?|"
    r"no (?:statistically significant )?difference|non[- ]?inferior)\b",
    re.IGNORECASE,
)
EQUIVALENCE_DESIGN = re.compile(
    r"\b(equivalence|non[- ]?inferiority|noninferiority)\b",
    re.IGNORECASE,
)
IMPORTED_PROVENANCE = re.compile(
    r"\b(imported|draft[_ -]?bibliograph|author[_ -]?(?:supplied|provided)|"
    r"reading[_ -]?list)\b",
    re.IGNORECASE,
)
LATE_PROVENANCE = re.compile(r"\blate[_ -]?found\b", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate prior-work evidence accounting, idea provenance, imported "
            "bibliography resolution, late-find repair, and novelty sentinels."
        )
    )
    parser.add_argument("project_dir", type=Path, help="Research-framing artifact directory")
    gate = parser.add_mutually_exclusive_group()
    gate.add_argument(
        "--end-of-round",
        action="store_true",
        help="Require complete ledgers and checked completion markers.",
    )
    gate.add_argument(
        "--phase-ready",
        action="store_true",
        help="Apply the same fail-closed gate before a readiness decision.",
    )
    return parser.parse_args()


def normalized(value: str) -> str:
    return value.strip().upper().replace("-", "_").replace(" ", "_")


def issue(path: Path, row: int | None, message: str) -> str:
    location = f"{path.name}"
    if row is not None:
        location += f":row {row}"
    return f"{location}: {message}"


def read_csv(
    path: Path, required_columns: tuple[str, ...]
) -> tuple[list[dict[str, str]], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.is_file():
        return [], [issue(path, None, "file not found")], warnings
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            columns = reader.fieldnames or []
            missing = [name for name in required_columns if name not in columns]
            extra = [name for name in columns if name not in required_columns]
            if missing:
                errors.append(
                    issue(path, None, "missing required columns: " + ", ".join(missing))
                )
                return [], errors, warnings
            if extra:
                warnings.append(
                    issue(path, None, "unrecognized columns: " + ", ".join(extra))
                )
            rows = [
                {key: (value or "").strip() for key, value in row.items()}
                for row in reader
            ]
    except (OSError, csv.Error) as exc:
        return [], [issue(path, None, f"could not read CSV: {exc}")], warnings
    return rows, errors, warnings


def require(
    row: dict[str, str],
    fields: tuple[str, ...],
    path: Path,
    row_number: int,
    errors: list[str],
    reason: str,
) -> None:
    for field in fields:
        if not row[field]:
            errors.append(issue(path, row_number, f"{reason}: missing {field}"))


def check_enum(
    value: str,
    allowed: set[str],
    field: str,
    path: Path,
    row_number: int,
    errors: list[str],
) -> str:
    status = normalized(value)
    if status not in allowed:
        errors.append(
            issue(
                path,
                row_number,
                f"{field} must be one of {sorted(allowed)}; got {value!r}",
            )
        )
    return status


def expected_attribution(claim: str, demonstration: str) -> str:
    if claim in POSITIVE and demonstration in POSITIVE:
        return "CLAIMED_AND_DEMONSTRATED"
    if claim == "NO" and demonstration in POSITIVE:
        return "DEMONSTRATED_UNCLAIMED"
    if claim in POSITIVE and demonstration in {"NO", "UNRESOLVED", "N/A"}:
        return "CLAIMED_UNDEMONSTRATED"
    if claim == "NO" and demonstration in {"NO", "N/A"}:
        return "NEITHER"
    return "UNRESOLVED"


def split_set(value: str) -> set[str]:
    return {item.strip() for item in value.split("||") if item.strip()}


def validate_accounting(
    path: Path, rows: list[dict[str, str]], strict: bool
) -> list[str]:
    errors: list[str] = []
    if strict and not rows:
        return [issue(path, None, "bounded closure requires at least one accounting row")]

    atomic_channel_rows: dict[str, list[dict[str, str]]] = {}
    for candidate in rows:
        if (
            normalized(candidate["classification_scope"]) == "ATOMIC_CHANNEL"
            and candidate["channel_id"].strip()
        ):
            atomic_channel_rows.setdefault(candidate["channel_id"].strip(), []).append(
                candidate
            )

    seen: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        require(
            row,
            (
                "record_id",
                "work_id",
                "source_id",
                "proposition_type",
                "atomic_proposition",
                "unit_kind",
                "author_claim_status",
                "demonstration_status",
                "operated_capability_status",
                "evaluated_result_status",
                "evidence_granularity",
                "causal_attribution_scope",
                "capability_collision",
                "contribution_credit",
                "attribution_status",
                "port_status",
                "port_credit_gate",
                "classification_scope",
                "source_silence_disposition",
                "reopen_trigger",
            ),
            path,
            row_number,
            errors,
            "accounting row",
        )
        record_id = row["record_id"]
        if record_id in seen:
            errors.append(issue(path, row_number, f"duplicate record_id {record_id}"))
        seen.add(record_id)

        proposition_type = check_enum(
            row["proposition_type"],
            PROPOSITION_TYPES,
            "proposition_type",
            path,
            row_number,
            errors,
        )
        unit_kind = check_enum(
            row["unit_kind"], UNIT_KINDS, "unit_kind", path, row_number, errors
        )
        claim = check_enum(
            row["author_claim_status"],
            EVIDENCE_STATUSES - {"N/A"},
            "author_claim_status",
            path,
            row_number,
            errors,
        )
        demonstration = check_enum(
            row["demonstration_status"],
            EVIDENCE_STATUSES,
            "demonstration_status",
            path,
            row_number,
            errors,
        )
        operation = check_enum(
            row["operated_capability_status"],
            EVIDENCE_STATUSES,
            "operated_capability_status",
            path,
            row_number,
            errors,
        )
        evaluated = check_enum(
            row["evaluated_result_status"],
            EVIDENCE_STATUSES,
            "evaluated_result_status",
            path,
            row_number,
            errors,
        )
        granularity = check_enum(
            row["evidence_granularity"],
            EVIDENCE_GRANULARITIES,
            "evidence_granularity",
            path,
            row_number,
            errors,
        )
        causal_scope = check_enum(
            row["causal_attribution_scope"],
            CAUSAL_SCOPES,
            "causal_attribution_scope",
            path,
            row_number,
            errors,
        )
        collision = check_enum(
            row["capability_collision"],
            COLLISION_STATUSES,
            "capability_collision",
            path,
            row_number,
            errors,
        )
        credit = check_enum(
            row["contribution_credit"],
            CREDIT_STATUSES,
            "contribution_credit",
            path,
            row_number,
            errors,
        )
        attribution = check_enum(
            row["attribution_status"],
            ATTRIBUTION_STATUSES,
            "attribution_status",
            path,
            row_number,
            errors,
        )
        port_status = check_enum(
            row["port_status"],
            PORT_STATUSES,
            "port_status",
            path,
            row_number,
            errors,
        )
        port_gate = check_enum(
            row["port_credit_gate"],
            PORT_GATES,
            "port_credit_gate",
            path,
            row_number,
            errors,
        )
        classification_scope = check_enum(
            row["classification_scope"],
            CLASSIFICATION_SCOPES,
            "classification_scope",
            path,
            row_number,
            errors,
        )
        silence = check_enum(
            row["source_silence_disposition"],
            SILENCE_DISPOSITIONS,
            "source_silence_disposition",
            path,
            row_number,
            errors,
        )

        if claim in POSITIVE:
            require(
                row,
                ("author_claim_evidence", "author_claim_locator"),
                path,
                row_number,
                errors,
                "positive author claim",
            )
        if demonstration in POSITIVE:
            require(
                row,
                (
                    "demonstrated_artifact_or_study",
                    "demonstration_evidence",
                    "demonstration_locator",
                ),
                path,
                row_number,
                errors,
                "positive demonstration",
            )
        if operation in POSITIVE:
            require(
                row,
                (
                    "smallest_operated_unit",
                    "operated_capability",
                    "operation_evidence",
                    "operation_locator",
                    "generalization_boundary",
                ),
                path,
                row_number,
                errors,
                "positive operated capability",
            )
        if operation == "NO":
            require(
                row,
                ("operation_evidence", "operation_locator", "generalization_boundary"),
                path,
                row_number,
                errors,
                "operated capability NO requires positive boundary evidence",
            )
        if evaluated in POSITIVE:
            require(
                row,
                ("evaluated_result", "evaluation_design_or_measure", "evaluation_locator"),
                path,
                row_number,
                errors,
                "positive evaluated result",
            )

        if proposition_type == "ARTIFACT_CAPABILITY":
            if demonstration in POSITIVE and operation not in POSITIVE:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "artifact-capability demonstration requires positive operated capability",
                    )
                )
            if operation == "N/A":
                errors.append(
                    issue(
                        path,
                        row_number,
                        "artifact-capability operated_capability_status cannot be N/A",
                    )
                )
        if operation in POSITIVE and demonstration not in POSITIVE:
            errors.append(
                issue(
                    path,
                    row_number,
                    "positive operated capability requires a matched positive demonstration",
                )
            )
        if evaluated in POSITIVE and demonstration not in POSITIVE:
            errors.append(
                issue(
                    path,
                    row_number,
                    "positive evaluated result requires a matched positive demonstrated study",
                )
            )

        if collision in {"EXACT", "PARTIAL"}:
            if operation not in POSITIVE:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "capability collision requires a positively operated capability",
                    )
                )
            require(
                row,
                ("collision_atom", "collision_scope", "collision_evidence_locator"),
                path,
                row_number,
                errors,
                "positive capability collision",
            )

        if credit in {"FULL", "PARTIAL"}:
            if claim not in POSITIVE or demonstration not in POSITIVE:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "contribution credit requires both a positive author claim and matched demonstration",
                    )
                )
            if proposition_type == "ARTIFACT_CAPABILITY" and operation not in POSITIVE:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "artifact contribution credit requires a positively operated capability",
                    )
                )
            if proposition_type not in {"ARTIFACT_CAPABILITY", "OPEN_RESOURCE"} and evaluated not in POSITIVE:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "knowledge/result contribution credit requires a positive evaluated result",
                    )
                )
            require(
                row,
                (
                    "contribution_atom",
                    "credit_basis",
                    "credit_scope",
                    "credit_evidence_locator",
                ),
                path,
                row_number,
                errors,
                "positive contribution credit",
            )

        expected = expected_attribution(claim, demonstration)
        if attribution != expected:
            errors.append(
                issue(
                    path,
                    row_number,
                    f"attribution_status must be {expected} for claim={claim} and demonstration={demonstration}",
                )
            )
        if attribution == "DEMONSTRATED_UNCLAIMED":
            if credit != "NONE":
                errors.append(
                    issue(
                        path,
                        row_number,
                        "DEMONSTRATED_UNCLAIMED operation must receive contribution_credit=NONE",
                    )
                )
            require(
                row,
                ("author_claim_evidence", "author_claim_locator"),
                path,
                row_number,
                errors,
                "DEMONSTRATED_UNCLAIMED claim audit",
            )
        if attribution == "CLAIMED_UNDEMONSTRATED" and credit != "NONE":
            errors.append(
                issue(
                    path,
                    row_number,
                    "CLAIMED_UNDEMONSTRATED atom must receive contribution_credit=NONE",
                )
            )

        if granularity == "PACKAGE_CONDITION":
            if causal_scope != "PACKAGE_ONLY":
                errors.append(
                    issue(
                        path,
                        row_number,
                        "PACKAGE_CONDITION requires causal_attribution_scope=PACKAGE_ONLY",
                    )
                )
            if classification_scope != "PACKAGE_ONLY":
                errors.append(
                    issue(
                        path,
                        row_number,
                        "PACKAGE_CONDITION requires classification_scope=PACKAGE_ONLY",
                    )
                )
            for field, status in (
                ("collision_scope", collision),
                ("credit_scope", credit),
            ):
                if status not in {"NONE", "UNRESOLVED"} and "PACKAGE" not in normalized(row[field]):
                    errors.append(
                        issue(
                            path,
                            row_number,
                            f"package evidence cannot support operator-specific {field}",
                        )
                    )

        if evaluated in POSITIVE and EQUIVALENCE_CLAIM.search(row["evaluated_result"]):
            if not EQUIVALENCE_DESIGN.search(row["evaluation_design_or_measure"]):
                errors.append(
                    issue(
                        path,
                        row_number,
                        "equivalent/comparable/maintained/no-difference wording requires an equivalence or non-inferiority design",
                    )
                )

        if port_status == "PORT_ONLY" and credit != "NONE":
            errors.append(
                issue(
                    path,
                    row_number,
                    "PORT_ONLY receives contribution_credit=NONE",
                )
            )
        if port_status == "PORT_ONLY" and port_gate != "NONE":
            errors.append(
                issue(
                    path,
                    row_number,
                    "PORT_ONLY must use port_credit_gate=NONE; demonstrated adaptation uses ADAPTATION_CANDIDATE",
                )
            )
        if port_status == "NOT_A_PORT" and port_gate != "NONE":
            errors.append(
                issue(
                    path,
                    row_number,
                    "NOT_A_PORT must use port_credit_gate=NONE",
                )
            )
        if port_status == "ADAPTATION_CANDIDATE" and credit in {"FULL", "PARTIAL"}:
            if port_gate == "NONE":
                errors.append(
                    issue(
                        path,
                        row_number,
                        "adaptation contribution credit requires a demonstrated port credit gate",
                    )
                )
            if demonstration not in POSITIVE:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "adaptation credit gate requires matched demonstration",
                    )
                )
            if port_gate == "DEMONSTRATED_NEW_USE_CLASS" and operation not in POSITIVE:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "demonstrated new use class requires a positively operated capability",
                    )
                )
            if port_gate == "DIRECTLY_VALIDATED_EMPIRICAL_FINDING" and evaluated not in POSITIVE:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "directly validated empirical finding requires a positive evaluated result",
                    )
                )

        if classification_scope == "ATOMIC_CHANNEL":
            if unit_kind in {"COMMAND", "INPUT_CHANNEL", "REWARD_CHANNEL"} and not row["channel_id"]:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "atomic command/input/reward channel requires channel_id",
                    )
                )
        if classification_scope == "WHOLE_SYSTEM":
            required_channels = split_set(row["required_channel_set"])
            qualified_channels = split_set(row["qualified_channel_set"])
            if not required_channels:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "WHOLE_SYSTEM classification requires a nonempty required_channel_set",
                    )
                )
            if required_channels != qualified_channels:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "WHOLE_SYSTEM classification requires every required channel to be positively qualified",
                    )
                )
            for channel_id in qualified_channels:
                candidates = atomic_channel_rows.get(channel_id, [])
                if not any(
                    normalized(candidate["demonstration_status"]) in POSITIVE
                    and normalized(candidate["operated_capability_status"]) in POSITIVE
                    for candidate in candidates
                ):
                    errors.append(
                        issue(
                            path,
                            row_number,
                            "WHOLE_SYSTEM qualified channel "
                            f"{channel_id!r} lacks a positively demonstrated operated "
                            "ATOMIC_CHANNEL row",
                        )
                    )

        if silence in {"SEARCH_PRIORITY", "REOPEN_QUERY"}:
            require(
                row,
                ("search_priority_or_reopen_query",),
                path,
                row_number,
                errors,
                "source silence disposition",
            )
            if operation != "UNRESOLVED":
                errors.append(
                    issue(
                        path,
                        row_number,
                        "source silence can only leave operated capability UNRESOLVED",
                    )
                )
            if collision != "UNRESOLVED":
                errors.append(
                    issue(
                        path,
                        row_number,
                        "source silence can only leave capability collision UNRESOLVED",
                    )
                )
            if credit != "NONE":
                errors.append(
                    issue(
                        path,
                        row_number,
                        "source silence cannot create contribution credit",
                    )
                )
        elif row["search_priority_or_reopen_query"]:
            errors.append(
                issue(
                    path,
                    row_number,
                    "search_priority_or_reopen_query requires SEARCH_PRIORITY or REOPEN_QUERY",
                )
            )

    return errors


def validate_ideas(path: Path, rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        require(
            row,
            (
                "idea_id",
                "work_id",
                "source_id",
                "idea_type",
                "idea_text",
                "source_wording",
                "locator",
                "provenance_scope",
                "first_idea_language_consequence",
                "capability_collision",
                "contribution_credit",
                "prohibited_use",
                "reopen_trigger",
            ),
            path,
            row_number,
            errors,
            "idea/provenance row",
        )
        idea_id = row["idea_id"]
        if idea_id in seen:
            errors.append(issue(path, row_number, f"duplicate idea_id {idea_id}"))
        seen.add(idea_id)
        check_enum(
            row["idea_type"], IDEA_TYPES, "idea_type", path, row_number, errors
        )
        if normalized(row["capability_collision"]) != "NONE":
            errors.append(
                issue(
                    path,
                    row_number,
                    "ideas/proposals/future work must use capability_collision=NONE",
                )
            )
        if normalized(row["contribution_credit"]) != "NONE":
            errors.append(
                issue(
                    path,
                    row_number,
                    "ideas/proposals/future work must use contribution_credit=NONE",
                )
            )
    return errors


def read_source_resolution(
    path: Path,
) -> tuple[dict[str, dict[str, str]], list[str]]:
    errors: list[str] = []
    if not path.is_file():
        return {}, [issue(path, None, "file not found")]
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            required = {"source_id", "source_provenance", "acquisition_state"}
            missing = required - set(reader.fieldnames or [])
            if missing:
                return {}, [
                    issue(
                        path,
                        None,
                        "missing columns needed for cross-check: "
                        + ", ".join(sorted(missing)),
                    )
                ]
            rows = [
                {key: (value or "").strip() for key, value in row.items()}
                for row in reader
            ]
    except (OSError, csv.Error) as exc:
        return {}, [issue(path, None, f"could not read CSV: {exc}")]

    by_id: dict[str, dict[str, str]] = {}
    for row_number, row in enumerate(rows, start=2):
        source_id = row["source_id"]
        if not source_id:
            continue
        if source_id in by_id:
            errors.append(issue(path, row_number, f"duplicate source_id {source_id}"))
        by_id[source_id] = row
    return by_id, errors


def validate_imported(
    path: Path,
    rows: list[dict[str, str]],
    source_rows: dict[str, dict[str, str]],
    strict: bool,
) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    accounted_sources: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        require(
            row,
            (
                "accountability_id",
                "supplied_artifact",
                "bibliographic_identity",
                "potential_relevance",
                "independent_discovery_route",
                "terminal_disposition",
                "terminal_reason",
                "upgrade_search",
                "affected_claims",
                "reopen_trigger",
            ),
            path,
            row_number,
            errors,
            "imported bibliography row",
        )
        accountability_id = row["accountability_id"]
        if accountability_id in seen_ids:
            errors.append(
                issue(path, row_number, f"duplicate accountability_id {accountability_id}")
            )
        seen_ids.add(accountability_id)

        relevance = check_enum(
            row["potential_relevance"],
            RELEVANCE_STATUSES,
            "potential_relevance",
            path,
            row_number,
            errors,
        )
        disposition = check_enum(
            row["terminal_disposition"],
            TERMINAL_DISPOSITIONS,
            "terminal_disposition",
            path,
            row_number,
            errors,
        )
        if strict and relevance == "UNRESOLVED":
            errors.append(
                issue(
                    path,
                    row_number,
                    "bounded closure cannot retain UNRESOLVED imported relevance",
                )
            )
        if relevance == "MATERIAL":
            require(
                row,
                ("source_resolution_id",),
                path,
                row_number,
                errors,
                "material imported item",
            )
        if disposition == "FULL_TEXT_ASSESSED":
            require(
                row,
                ("full_copy_locator", "evidence_accounting_ids"),
                path,
                row_number,
                errors,
                "FULL_TEXT_ASSESSED imported item",
            )
        elif disposition == "SUPERSEDED":
            require(
                row,
                ("superseded_by",),
                path,
                row_number,
                errors,
                "SUPERSEDED imported item",
            )
        elif disposition == "NEEDS_AUTHOR_SOURCE_ACCESS":
            require(
                row,
                ("exact_author_access_action",),
                path,
                row_number,
                errors,
                "NEEDS_AUTHOR_SOURCE_ACCESS imported item",
            )

        source_id = row["source_resolution_id"]
        if source_id:
            accounted_sources.add(source_id)
            source = source_rows.get(source_id)
            if source is None:
                errors.append(
                    issue(
                        path,
                        row_number,
                        f"source_resolution_id {source_id} does not resolve",
                    )
                )
            elif normalized(source["acquisition_state"]) != disposition:
                errors.append(
                    issue(
                        path,
                        row_number,
                        "terminal_disposition does not match source-resolution acquisition_state "
                        f"for {source_id}",
                    )
                )

    for source_id, row in source_rows.items():
        if IMPORTED_PROVENANCE.search(row["source_provenance"]) and source_id not in accounted_sources:
            errors.append(
                issue(
                    path,
                    None,
                    f"imported source-resolution row {source_id} lacks bibliography accountability",
                )
            )
    return errors


def read_sentinels(path: Path) -> tuple[dict[str, dict[str, str]], list[str]]:
    if not path.is_file():
        return {}, [issue(path, None, "file not found")]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {}, [
            issue(
                path,
                None,
                f"must be JSON-compatible YAML with a valid object: {exc}",
            )
        ]
    if payload.get("schema_version") != 1:
        return {}, [issue(path, None, "schema_version must be 1")]
    sentinels = payload.get("sentinels")
    if not isinstance(sentinels, list):
        return {}, [issue(path, None, "sentinels must be a list")]

    errors: list[str] = []
    by_id: dict[str, dict[str, str]] = {}
    required = (
        "sentinel_id",
        "source_id",
        "citation_key",
        "non_title_query",
        "retrieval_route",
        "expected_portfolio",
        "expected_collision_atom",
        "last_checked",
        "retrieval_status",
        "reopen_trigger",
    )
    for index, raw in enumerate(sentinels, start=1):
        if not isinstance(raw, dict):
            errors.append(issue(path, index, "sentinel must be an object"))
            continue
        row = {key: str(raw.get(key, "")).strip() for key in required}
        for field in required:
            if not row[field]:
                errors.append(issue(path, index, f"sentinel missing {field}"))
        sentinel_id = row["sentinel_id"]
        if sentinel_id in by_id:
            errors.append(issue(path, index, f"duplicate sentinel_id {sentinel_id}"))
        by_id[sentinel_id] = row
        if normalized(row["retrieval_status"]) not in {"PASS", "FAIL"}:
            errors.append(
                issue(path, index, "retrieval_status must be PASS or FAIL")
            )
    return by_id, errors


def validate_late(
    path: Path,
    rows: list[dict[str, str]],
    source_rows: dict[str, dict[str, str]],
    sentinels: dict[str, dict[str, str]],
    strict: bool,
) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    accounted_sources: set[str] = set()
    required_repair = (
        "affected_claim_ids",
        "route_that_should_have_found_it",
        "process_failure",
        "sibling_seed_ids",
        "sibling_records_screened",
        "query_or_graph_repair",
        "affected_claim_rerun",
        "regression_sentinel_id",
        "source_resolution_state",
        "completed_date",
    )
    for row_number, row in enumerate(rows, start=2):
        require(
            row,
            (
                "incident_id",
                "late_found_source_id",
                "citation_key",
                "discovery_date",
                "material_boundary_changed",
                "status",
            ),
            path,
            row_number,
            errors,
            "late-found-work row",
        )
        incident_id = row["incident_id"]
        if incident_id in seen:
            errors.append(issue(path, row_number, f"duplicate incident_id {incident_id}"))
        seen.add(incident_id)
        source_id = row["late_found_source_id"]
        accounted_sources.add(source_id)
        material = check_enum(
            row["material_boundary_changed"],
            {"YES", "NO"},
            "material_boundary_changed",
            path,
            row_number,
            errors,
        )
        status = check_enum(
            row["status"], LATE_STATUSES, "status", path, row_number, errors
        )
        if source_id not in source_rows:
            errors.append(
                issue(
                    path,
                    row_number,
                    f"late_found_source_id {source_id} does not resolve",
                )
            )
        if material == "YES":
            require(
                row,
                required_repair,
                path,
                row_number,
                errors,
                "material late-found work repair",
            )
            if strict and status != "COMPLETE":
                errors.append(
                    issue(
                        path,
                        row_number,
                        "material late-found work must be COMPLETE at bounded closure",
                    )
                )
            sentinel_id = row["regression_sentinel_id"]
            if sentinel_id and sentinel_id not in sentinels:
                errors.append(
                    issue(
                        path,
                        row_number,
                        f"regression_sentinel_id {sentinel_id} does not resolve",
                    )
                )
            elif sentinel_id and strict:
                sentinel_status = normalized(
                    sentinels[sentinel_id]["retrieval_status"]
                )
                if sentinel_status != "PASS":
                    errors.append(
                        issue(
                            path,
                            row_number,
                            f"regression sentinel {sentinel_id} has not passed",
                        )
                    )

    for source_id, row in source_rows.items():
        if LATE_PROVENANCE.search(row["source_provenance"]) and source_id not in accounted_sources:
            errors.append(
                issue(
                    path,
                    None,
                    f"late-found source-resolution row {source_id} lacks a postmortem",
                )
            )
    return errors


def validate_completion_markers(path: Path, strict: bool) -> list[str]:
    if not path.is_file():
        return [issue(path, None, "file not found")]
    if not strict:
        return []
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    for marker in COMPLETION_MARKERS:
        pattern = re.compile(
            rf"^-\s*\[[xX]\]\s+`{re.escape(marker)}`\s*$",
            re.MULTILINE,
        )
        if not pattern.search(text):
            errors.append(issue(path, None, f"unchecked completion marker {marker}"))
    return errors


def validate_project(
    project_dir: Path, strict: bool
) -> tuple[list[str], list[str], dict[str, int]]:
    errors: list[str] = []
    warnings: list[str] = []
    counts: dict[str, int] = {}

    accounting_path = project_dir / ACCOUNTING_FILE
    idea_path = project_dir / IDEA_FILE
    imported_path = project_dir / IMPORTED_FILE
    late_path = project_dir / LATE_FILE
    sentinel_path = project_dir / SENTINEL_FILE
    boundary_path = project_dir / BOUNDARY_FILE
    source_path = project_dir / SOURCE_RESOLUTION_FILE

    accounting_rows, read_errors, read_warnings = read_csv(
        accounting_path, ACCOUNTING_COLUMNS
    )
    errors.extend(read_errors)
    warnings.extend(read_warnings)
    counts["accounting"] = len(accounting_rows)
    if not read_errors:
        errors.extend(validate_accounting(accounting_path, accounting_rows, strict))

    idea_rows, read_errors, read_warnings = read_csv(idea_path, IDEA_COLUMNS)
    errors.extend(read_errors)
    warnings.extend(read_warnings)
    counts["ideas"] = len(idea_rows)
    if not read_errors:
        errors.extend(validate_ideas(idea_path, idea_rows))

    source_rows, source_errors = read_source_resolution(source_path)
    errors.extend(source_errors)
    counts["source_resolution"] = len(source_rows)

    imported_rows, read_errors, read_warnings = read_csv(
        imported_path, IMPORTED_COLUMNS
    )
    errors.extend(read_errors)
    warnings.extend(read_warnings)
    counts["imported"] = len(imported_rows)
    if not read_errors and not source_errors:
        errors.extend(
            validate_imported(
                imported_path, imported_rows, source_rows, strict
            )
        )

    sentinels, sentinel_errors = read_sentinels(sentinel_path)
    errors.extend(sentinel_errors)
    counts["sentinels"] = len(sentinels)

    late_rows, read_errors, read_warnings = read_csv(late_path, LATE_COLUMNS)
    errors.extend(read_errors)
    warnings.extend(read_warnings)
    counts["late"] = len(late_rows)
    if not read_errors and not source_errors and not sentinel_errors:
        errors.extend(
            validate_late(
                late_path,
                late_rows,
                source_rows,
                sentinels,
                strict,
            )
        )

    errors.extend(validate_completion_markers(boundary_path, strict))
    return errors, warnings, counts


def main() -> int:
    args = parse_args()
    strict = args.end_of_round or args.phase_ready
    errors, warnings, counts = validate_project(args.project_dir, strict)

    for message in warnings:
        print(f"WARNING: {message}")
    for message in errors:
        print(f"ERROR: {message}")

    summary = ", ".join(f"{name}={count}" for name, count in sorted(counts.items()))
    if errors:
        print(
            f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s); {summary}"
        )
        return 1
    print(f"PASS: {len(warnings)} warning(s); {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
