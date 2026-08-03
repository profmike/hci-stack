#!/usr/bin/env python3
"""Validate an HCI research-framing claim-evidence ledger."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


REQUIRED_COLUMNS = (
    "claim_id",
    "framing_role",
    "proposed_claim",
    "evidence_state",
    "claim_type",
    "source_tier",
    "directness",
    "citation_key",
    "source_identity",
    "method",
    "population_or_context",
    "sample_or_coverage",
    "effect_or_estimate",
    "uncertainty_or_precision",
    "locator",
    "doi_url_or_internal_path",
    "limitations",
    "status",
)

ALLOWED_TIERS = {"T1", "T2A", "T2B"}
ALLOWED_DIRECTNESS = {"direct", "inferred", "adjacent", "analogy"}
ALLOWED_STATUS = {"candidate", "verified", "rejected"}
ALLOWED_EVIDENCE_STATES = {
    "established-external",
    "inferred-external",
    "observed-project",
    "planned",
    "hypothesis",
    "aspiration",
    "unsupported",
}
VERIFIED_REQUIRED = (
    "proposed_claim",
    "claim_type",
    "citation_key",
    "source_identity",
    "method",
    "population_or_context",
    "sample_or_coverage",
    "effect_or_estimate",
    "uncertainty_or_precision",
    "locator",
    "doi_url_or_internal_path",
    "limitations",
)
PLACEHOLDER = re.compile(
    r"(\bTODO\b|\bTBD\b|citation needed|\[\?\]|<[^>]+>|\{[^}]+\})",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate structure and evidence completeness in a claim ledger."
    )
    parser.add_argument("ledger", type=Path, help="CSV claim-evidence ledger")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Require at least one row and every evidence-backed row to be verified.",
    )
    return parser.parse_args()


def issue(kind: str, row_number: int | None, message: str) -> str:
    location = f"row {row_number}: " if row_number is not None else ""
    return f"{kind}: {location}{message}"


def validate(path: Path, strict: bool) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warnings: list[str] = []

    if not path.is_file():
        return [issue("ERROR", None, f"file not found: {path}")], warnings, 0

    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            columns = reader.fieldnames or []
            missing = [column for column in REQUIRED_COLUMNS if column not in columns]
            extra = [column for column in columns if column not in REQUIRED_COLUMNS]
            if missing:
                errors.append(
                    issue("ERROR", None, f"missing required columns: {', '.join(missing)}")
                )
            if extra:
                warnings.append(
                    issue("WARNING", None, f"unrecognized columns: {', '.join(extra)}")
                )
            if missing:
                return errors, warnings, 0
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        return [issue("ERROR", None, f"could not read CSV: {exc}")], warnings, 0

    if not rows:
        target = errors if strict else warnings
        target.append(issue("ERROR" if strict else "WARNING", None, "ledger has no claims"))
        return errors, warnings, 0

    seen_ids: set[str] = set()
    for index, raw_row in enumerate(rows, start=2):
        row = {key: (value or "").strip() for key, value in raw_row.items()}
        claim_id = row["claim_id"]
        status = row["status"].lower()
        tier = row["source_tier"].upper()
        directness = row["directness"].lower()
        evidence_state = row["evidence_state"].lower()

        if not claim_id:
            errors.append(issue("ERROR", index, "claim_id is empty"))
        elif claim_id in seen_ids:
            errors.append(issue("ERROR", index, f"duplicate claim_id: {claim_id}"))
        else:
            seen_ids.add(claim_id)

        if evidence_state not in ALLOWED_EVIDENCE_STATES:
            errors.append(
                issue(
                    "ERROR",
                    index,
                    "evidence_state must be one of "
                    f"{sorted(ALLOWED_EVIDENCE_STATES)}",
                )
            )
        evidence_backed = evidence_state in {
            "established-external",
            "inferred-external",
            "observed-project",
        }
        if evidence_backed and tier not in ALLOWED_TIERS:
            errors.append(
                issue("ERROR", index, f"source_tier must be one of {sorted(ALLOWED_TIERS)}")
            )
        elif tier and tier not in ALLOWED_TIERS:
            errors.append(
                issue("ERROR", index, f"source_tier must be one of {sorted(ALLOWED_TIERS)}")
            )
        if evidence_backed and directness not in ALLOWED_DIRECTNESS:
            errors.append(
                issue(
                    "ERROR",
                    index,
                    f"directness must be one of {sorted(ALLOWED_DIRECTNESS)}",
                )
            )
        elif directness and directness not in ALLOWED_DIRECTNESS:
            errors.append(
                issue(
                    "ERROR",
                    index,
                    f"directness must be one of {sorted(ALLOWED_DIRECTNESS)}",
                )
            )
        if evidence_state == "inferred-external":
            if directness != "inferred":
                errors.append(
                    issue(
                        "ERROR",
                        index,
                        "inferred-external claims require directness=inferred",
                    )
                )
            if not re.search(
                r"\b(published|reported|documented|demonstrated|first-party)\b",
                row["proposed_claim"],
                re.IGNORECASE,
            ):
                errors.append(
                    issue(
                        "ERROR",
                        index,
                        "inferred-external claim must be scoped to the published, "
                        "reported, documented, demonstrated, or first-party record",
                    )
                )
        elif directness == "inferred":
            errors.append(
                issue(
                    "ERROR",
                    index,
                    "directness=inferred is reserved for inferred-external claims",
                )
            )
        if status not in ALLOWED_STATUS:
            errors.append(
                issue("ERROR", index, f"status must be one of {sorted(ALLOWED_STATUS)}")
            )

        combined = " ".join(row.values())
        if PLACEHOLDER.search(combined):
            errors.append(issue("ERROR", index, "contains a placeholder token"))

        if status == "verified" and not evidence_backed:
            errors.append(
                issue(
                    "ERROR",
                    index,
                    f"{evidence_state} claims cannot be marked verified",
                )
            )
        if status == "verified" and evidence_backed:
            for field in VERIFIED_REQUIRED:
                if not row[field]:
                    errors.append(
                        issue("ERROR", index, f"verified claim is missing {field}")
                    )
            identifier = row["doi_url_or_internal_path"]
            if identifier and not identifier.startswith(
                ("http://", "https://", "10.", "doi:", "internal:", "manuscript:")
            ):
                errors.append(
                    issue(
                        "ERROR",
                        index,
                        "doi_url_or_internal_path must be a URL, DOI, internal:, or manuscript: locator",
                    )
                )
            if evidence_state != "inferred-external" and directness != "direct":
                warnings.append(
                    issue(
                        "WARNING",
                        index,
                        f"verified claim relies on {directness} rather than direct support",
                    )
                )

        if strict and status == "candidate" and evidence_backed:
            errors.append(issue("ERROR", index, "candidate claim remains in strict mode"))
        if not strict and status == "candidate" and evidence_backed:
            warnings.append(issue("WARNING", index, "candidate claim still needs verification"))
        if evidence_state == "unsupported" and status != "rejected":
            warnings.append(
                issue("WARNING", index, "unsupported claim remains in the framing")
            )

        if status != "rejected" and not row["framing_role"]:
            errors.append(issue("ERROR", index, "framing_role is empty"))
        if status != "rejected" and not row["proposed_claim"]:
            errors.append(issue("ERROR", index, "proposed_claim is empty"))

    return errors, warnings, len(rows)


def main() -> int:
    args = parse_args()
    errors, warnings, row_count = validate(args.ledger, args.strict)

    for message in warnings:
        print(message)
    for message in errors:
        print(message)

    if errors:
        print(
            f"FAIL: {row_count} claim row(s), {len(errors)} error(s), "
            f"{len(warnings)} warning(s)"
        )
        return 1

    print(f"PASS: {row_count} claim row(s), {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
