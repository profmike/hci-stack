from __future__ import annotations

import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_source_resolution.py"
SPEC = importlib.util.spec_from_file_location("check_source_resolution", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def base_row() -> dict[str, str]:
    row = {column: "" for column in MODULE.REQUIRED_COLUMNS}
    row.update(
        {
            "source_provenance": "independent concept search",
            "candidate_role": "motivation evidence",
        }
    )
    return row


class SourceResolutionTests(unittest.TestCase):
    def validate_rows(
        self,
        rows: list[dict[str, str]],
        *,
        end_of_round: bool = False,
        phase_ready: bool = False,
        reference_keys: list[str] | None = None,
        reference_rows: list[dict[str, str]] | None = None,
        claim_ids: list[str] | None = None,
    ):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source-resolution.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=MODULE.REQUIRED_COLUMNS)
                writer.writeheader()
                writer.writerows(rows)
            if phase_ready:
                if reference_rows is None:
                    keys = (
                        [row["citation_key"] for row in rows if row.get("citation_key")]
                        if reference_keys is None
                        else reference_keys
                    )
                    reference_rows = [
                        {
                            "citation_key": key,
                            "url": f"https://doi.org/10.0000/{key.lower()}",
                        }
                        for key in keys
                    ]
                with (Path(directory) / "references.csv").open(
                    "w",
                    newline="",
                    encoding="utf-8",
                ) as handle:
                    writer = csv.DictWriter(
                        handle,
                        fieldnames=("citation_key", "url"),
                    )
                    writer.writeheader()
                    writer.writerows(reference_rows)
            if (end_of_round or phase_ready) and any(
                row.get("acquisition_state") == "NEEDS_AUTHOR_SOURCE_ACCESS"
                for row in rows
            ):
                if claim_ids is None:
                    claim_ids = [
                        claim_id.strip()
                        for row in rows
                        for claim_id in row.get("affected_claims", "").split(
                            MODULE.CLAIM_ID_DELIMITER
                        )
                        if claim_id.strip()
                    ]
                with (Path(directory) / "claim-evidence-ledger.csv").open(
                    "w",
                    newline="",
                    encoding="utf-8",
                ) as handle:
                    writer = csv.DictWriter(handle, fieldnames=("claim_id",))
                    writer.writeheader()
                    writer.writerows({"claim_id": claim_id} for claim_id in claim_ids)
            return MODULE.validate(
                path,
                end_of_round=end_of_round,
                phase_ready=phase_ready,
            )

    def validate(
        self,
        row: dict[str, str],
        *,
        end_of_round: bool = False,
        phase_ready: bool = False,
        reference_keys: list[str] | None = None,
        reference_rows: list[dict[str, str]] | None = None,
        claim_ids: list[str] | None = None,
    ):
        return self.validate_rows(
            [row],
            end_of_round=end_of_round,
            phase_ready=phase_ready,
            reference_keys=reference_keys,
            reference_rows=reference_rows,
            claim_ids=claim_ids,
        )

    def test_full_text_assessed_closes_end_of_round_and_phase_ready(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "citation_key": "Example2026",
                "bibliographic_identity": "Example paper",
                "canonical_url": "https://doi.org/10.0000/example",
                "relevance": "retain",
                "acquisition_state": "FULL_TEXT_ASSESSED",
                "full_copy_locator": "governed:sources/example.pdf",
                "full_text_review_locator": "source-manifest.md#S1",
                "evidence_register_locator": "evidence-strength-register.md#S1",
                "upgrade_search": "Searched authority map and two scholarly indexes; no stronger direct source",
            }
        )
        self.assertEqual(self.validate(row, end_of_round=True), ([], [], 1))
        self.assertEqual(self.validate(row, phase_ready=True), ([], [], 1))

    def test_unassessed_is_never_a_valid_resolution_state(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Example paper",
                "canonical_url": "https://doi.org/10.0000/example",
                "relevance": "undecided",
                "acquisition_state": "UNASSESSED",
            }
        )
        errors, _, _ = self.validate(row)
        self.assertTrue(any("UNASSESSED is not a source-resolution state" in e for e in errors))

    def test_acquiring_is_allowed_during_work_but_not_at_end_of_round(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Example paper",
                "canonical_url": "https://doi.org/10.0000/example",
                "relevance": "undecided",
                "acquisition_state": "ACQUIRING",
                "next_action": "Try the author repository",
            }
        )
        self.assertEqual(self.validate(row), ([], [], 1))
        errors, _, _ = self.validate(row, end_of_round=True)
        self.assertTrue(any("cannot end the round" in error for error in errors))

    def test_author_access_requires_attempts_request_and_surfaced_date(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Example paper",
                "canonical_url": "https://doi.org/10.0000/example",
                "relevance": "retain",
                "acquisition_state": "NEEDS_AUTHOR_SOURCE_ACCESS",
            }
        )
        errors, _, _ = self.validate(row, end_of_round=True)
        for field in (
            "attempted_routes",
            "exact_author_action",
            "request_surfaced_date",
            "request_surfaced_locator",
            "affected_claims",
            "fallback_or_narrowing",
            "reopen_trigger",
            "next_action",
        ):
            self.assertTrue(any(field in error for error in errors))

        row.update(
            {
                "attempted_routes": "Publisher paywall; no lawful open copy",
                "exact_author_action": "Download through university VPN and attach the PDF",
                "request_surfaced_date": "2026-07-29",
                "request_surfaced_locator": "session:019f-example#2026-07-29",
                "affected_claims": "M7||RW3",
                "fallback_or_narrowing": "Keep M7 unsupported and omit the RW3 efficacy contrast",
                "reopen_trigger": "Attached full PDF is audited and entered in the evidence register",
                "next_action": "Await the requested PDF, then audit it",
            }
        )
        self.assertEqual(self.validate(row, end_of_round=True), ([], [], 1))
        errors, _, _ = self.validate(row, phase_ready=True)
        self.assertTrue(any("phase-ready status cannot retain" in error for error in errors))

    def test_full_text_obtained_still_requires_review_before_round_ends(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Example paper",
                "canonical_url": "https://doi.org/10.0000/example",
                "relevance": "retain",
                "acquisition_state": "FULL_TEXT_OBTAINED",
                "next_action": "Open methods, results, limitations, and supplements",
            }
        )
        errors, _, _ = self.validate(row, end_of_round=True)
        self.assertTrue(any("FULL_TEXT_OBTAINED" in error for error in errors))

    def test_screened_out_requires_an_exact_reason(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Keyword collision",
                "canonical_url": "https://doi.org/10.0000/example",
                "relevance": "exclude",
                "acquisition_state": "SCREENED_OUT",
            }
        )
        errors, _, _ = self.validate(row, end_of_round=True)
        self.assertTrue(any("terminal_reason" in error for error in errors))

    def test_retained_full_text_requires_an_independent_upgrade_search(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Author-provided paper",
                "canonical_url": "https://doi.org/10.0000/example",
                "relevance": "retain",
                "acquisition_state": "FULL_TEXT_ASSESSED",
                "full_copy_locator": "governed:sources/example.pdf",
                "full_text_review_locator": "source-manifest.md#S1",
                "evidence_register_locator": "evidence-strength-register.md#S1",
            }
        )
        errors, _, _ = self.validate(row, end_of_round=True)
        self.assertTrue(any("upgrade_search" in error for error in errors))

    def test_retained_full_text_requires_a_stable_citation_key(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Author-provided paper",
                "canonical_url": "https://doi.org/10.0000/example",
                "relevance": "retain",
                "acquisition_state": "FULL_TEXT_ASSESSED",
                "full_copy_locator": "governed:sources/example.pdf",
                "full_text_review_locator": "source-manifest.md#S1",
                "evidence_register_locator": "evidence-strength-register.md#S1",
                "upgrade_search": "Independent claim-matched upgrade search completed",
            }
        )
        errors, _, _ = self.validate(row, end_of_round=True)
        self.assertTrue(any("citation_key" in error for error in errors))

    def test_phase_ready_key_must_resolve_in_project_references(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "citation_key": "MissingFromRegistry2026",
                "bibliographic_identity": "Author-provided paper",
                "canonical_url": "https://doi.org/10.0000/example",
                "relevance": "retain",
                "acquisition_state": "FULL_TEXT_ASSESSED",
                "full_copy_locator": "governed:sources/example.pdf",
                "full_text_review_locator": "source-manifest.md#S1",
                "evidence_register_locator": "evidence-strength-register.md#S1",
                "upgrade_search": "Independent claim-matched upgrade search completed",
            }
        )
        errors, _, _ = self.validate(
            row,
            phase_ready=True,
            reference_keys=[],
        )
        self.assertTrue(any("absent from references.csv" in error for error in errors))

    def test_superseded_source_requires_stable_replacement_locator(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Weaker supplied source",
                "canonical_url": "https://doi.org/10.0000/weaker",
                "relevance": "exclude",
                "acquisition_state": "SUPERSEDED",
                "terminal_reason": "A stronger direct synthesis covers the intended claim",
            }
        )
        errors, _, _ = self.validate(row, end_of_round=True)
        self.assertTrue(any("superseded_by" in error for error in errors))

    def test_access_request_rejects_placeholder_date_locator_and_claim_provenance(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Paywalled paper",
                "canonical_url": "https://doi.org/10.0000/paywalled",
                "relevance": "retain",
                "acquisition_state": "NEEDS_AUTHOR_SOURCE_ACCESS",
                "attempted_routes": "Publisher, author site, repositories",
                "exact_author_action": "Download through university VPN and attach the PDF",
                "request_surfaced_date": "pending",
                "request_surfaced_locator": "no",
                "affected_claims": "pending",
                "fallback_or_narrowing": "pending",
                "reopen_trigger": "pending",
                "next_action": "Await the requested PDF, then audit it",
            }
        )
        errors, _, _ = self.validate(row, end_of_round=True)
        for phrase in (
            "actual, non-future YYYY-MM-DD date",
            "request_surfaced_locator",
            "placeholder value 'pending' for affected_claims",
            "placeholder value 'pending' for fallback_or_narrowing",
            "placeholder value 'pending' for reopen_trigger",
        ):
            self.assertTrue(any(phrase in error for error in errors), phrase)

    def test_access_request_rejects_wrapped_placeholder_locators(self):
        for locator in (
            "session:pending.",
            "conversation:no",
            "conversation:N/A",
            "thread:TBD.",
            "workboard.md#pending",
            "workboard.md#n/a",
        ):
            with self.subTest(locator=locator):
                row = base_row()
                row.update(
                    {
                        "source_id": "S1",
                        "bibliographic_identity": "Paywalled paper",
                        "canonical_url": "https://doi.org/10.0000/paywalled",
                        "relevance": "retain",
                        "acquisition_state": "NEEDS_AUTHOR_SOURCE_ACCESS",
                        "attempted_routes": "Publisher, author site, repositories",
                        "exact_author_action": "Download through university VPN and attach the PDF",
                        "request_surfaced_date": "2026-07-29",
                        "request_surfaced_locator": locator,
                        "affected_claims": "M7",
                        "fallback_or_narrowing": "Omit the efficacy claim",
                        "reopen_trigger": "Attached full PDF is audited",
                        "next_action": "Await the requested PDF, then audit it",
                    }
                )
                errors, _, _ = self.validate(
                    row,
                    end_of_round=True,
                    claim_ids=["M7"],
                )
                self.assertTrue(
                    any("request_surfaced_locator" in error for error in errors),
                    errors,
                )

    def test_punctuated_placeholders_cannot_close_access_assessment_or_screening(self):
        access = base_row()
        access.update(
            {
                "source_id": "S-access",
                "bibliographic_identity": "Paywalled paper",
                "canonical_url": "https://doi.org/10.0000/paywalled",
                "relevance": "retain",
                "acquisition_state": "NEEDS_AUTHOR_SOURCE_ACCESS",
                "attempted_routes": "`pending`",
                "exact_author_action": "pending.",
                "request_surfaced_date": "2026-07-29",
                "request_surfaced_locator": "session:pending.",
                "affected_claims": "M7",
                "fallback_or_narrowing": "**pending**",
                "reopen_trigger": "TBD.",
                "next_action": "unknown…",
            }
        )
        errors, _, _ = self.validate(
            access,
            end_of_round=True,
            claim_ids=["M7"],
        )
        for field in (
            "attempted_routes",
            "exact_author_action",
            "request_surfaced_locator",
            "fallback_or_narrowing",
            "reopen_trigger",
            "next_action",
        ):
            self.assertTrue(any(field in error for error in errors), errors)

        assessed = base_row()
        assessed.update(
            {
                "source_id": "S-assessed",
                "citation_key": "Assessed2026",
                "bibliographic_identity": "Purported assessed paper",
                "canonical_url": "https://doi.org/10.0000/assessed",
                "relevance": "retain",
                "acquisition_state": "FULL_TEXT_ASSESSED",
                "full_copy_locator": "pending.",
                "full_text_review_locator": "`pending`",
                "evidence_register_locator": "governed:sources/TBD.",
                "upgrade_search": "**pending**",
            }
        )
        errors, _, _ = self.validate(assessed, end_of_round=True)
        for field in (
            "full_copy_locator",
            "full_text_review_locator",
            "evidence_register_locator",
            "upgrade_search",
        ):
            self.assertTrue(any(field in error for error in errors), errors)

        screened = base_row()
        screened.update(
            {
                "source_id": "S-screened",
                "bibliographic_identity": "Purportedly irrelevant paper",
                "canonical_url": "https://doi.org/10.0000/screened",
                "relevance": "exclude",
                "acquisition_state": "SCREENED_OUT",
                "terminal_reason": "pending.",
            }
        )
        errors, _, _ = self.validate(screened, end_of_round=True)
        self.assertTrue(
            any("placeholder value 'pending.' for terminal_reason" in error for error in errors),
            errors,
        )

    def test_access_request_claim_ids_must_be_structured_and_resolve(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Paywalled paper",
                "canonical_url": "https://doi.org/10.0000/paywalled",
                "relevance": "retain",
                "acquisition_state": "NEEDS_AUTHOR_SOURCE_ACCESS",
                "attempted_routes": "Publisher, author site, repositories",
                "exact_author_action": "Download through university VPN and attach the PDF",
                "request_surfaced_date": "2026-07-29",
                "request_surfaced_locator": "session:019f-example#2026-07-29",
                "affected_claims": "some claim||UNKNOWN-CLAIM",
                "fallback_or_narrowing": "Omit the efficacy claim",
                "reopen_trigger": "Attached full PDF is audited",
                "next_action": "Await the requested PDF, then audit it",
            }
        )
        errors, _, _ = self.validate(
            row,
            end_of_round=True,
            claim_ids=["KNOWN-CLAIM"],
        )
        for phrase in (
            "'some claim' is not a stable claim ID",
            "'UNKNOWN-CLAIM' is absent from claim-evidence-ledger.csv",
        ):
            self.assertTrue(any(phrase in error for error in errors), errors)

    def test_phase_ready_rejects_external_reference_missing_from_resolution_ledger(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "citation_key": "Assessed2026",
                "bibliographic_identity": "Assessed paper",
                "canonical_url": "https://doi.org/10.0000/assessed",
                "relevance": "retain",
                "acquisition_state": "FULL_TEXT_ASSESSED",
                "full_copy_locator": "governed:sources/assessed.pdf",
                "full_text_review_locator": "source-manifest.md#S1",
                "evidence_register_locator": "evidence-strength-register.md#S1",
                "upgrade_search": "Independent claim-matched upgrade search completed",
            }
        )
        errors, _, _ = self.validate(
            row,
            phase_ready=True,
            reference_rows=[
                {
                    "citation_key": "Assessed2026",
                    "url": "https://doi.org/10.0000/assessed",
                },
                {
                    "citation_key": "MissingLedger2026",
                    "url": "https://doi.org/10.0000/missing",
                },
            ],
        )
        self.assertTrue(
            any(
                "external citation_key 'MissingLedger2026' is absent from "
                "source-resolution.csv" in error
                for error in errors
            )
        )

    def test_phase_ready_exempts_explicit_internal_project_evidence_from_source_ledger(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "citation_key": "Assessed2026",
                "bibliographic_identity": "Assessed paper",
                "canonical_url": "https://doi.org/10.0000/assessed",
                "relevance": "retain",
                "acquisition_state": "FULL_TEXT_ASSESSED",
                "full_copy_locator": "governed:sources/assessed.pdf",
                "full_text_review_locator": "source-manifest.md#S1",
                "evidence_register_locator": "evidence-strength-register.md#S1",
                "upgrade_search": "Independent claim-matched upgrade search completed",
            }
        )
        self.assertEqual(
            self.validate(
                row,
                phase_ready=True,
                reference_rows=[
                    {
                        "citation_key": "Assessed2026",
                        "url": "https://doi.org/10.0000/assessed",
                    },
                    {
                        "citation_key": "ProjectStudy2026",
                        "url": "internal:project-study",
                    },
                ],
            ),
            ([], [], 1),
        )

    def test_superseded_replacement_must_exist_and_be_retained_full_text(self):
        superseded = base_row()
        superseded.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Weaker supplied source",
                "canonical_url": "https://doi.org/10.0000/weaker",
                "relevance": "exclude",
                "acquisition_state": "SUPERSEDED",
                "terminal_reason": "A stronger direct source covers the intended claim",
                "superseded_by": "DOES_NOT_EXIST",
            }
        )
        errors, _, _ = self.validate(superseded, end_of_round=True)
        self.assertTrue(any("does not resolve" in error for error in errors))

        transient = base_row()
        transient.update(
            {
                "source_id": "S2",
                "citation_key": "Replacement2026",
                "bibliographic_identity": "Replacement candidate",
                "canonical_url": "https://doi.org/10.0000/replacement",
                "relevance": "retain",
                "acquisition_state": "ACQUIRING",
                "next_action": "Obtain and review the full text",
            }
        )
        superseded["superseded_by"] = "S2"
        errors, _, _ = self.validate_rows([superseded, transient])
        self.assertTrue(
            any("must resolve to a retained FULL_TEXT_ASSESSED source" in error for error in errors)
        )

    def test_superseded_source_cannot_point_to_itself(self):
        row = base_row()
        row.update(
            {
                "source_id": "S1",
                "citation_key": "Self2026",
                "bibliographic_identity": "Self-referencing source",
                "canonical_url": "https://doi.org/10.0000/self",
                "relevance": "exclude",
                "acquisition_state": "SUPERSEDED",
                "terminal_reason": "Purportedly replaced",
                "superseded_by": "Self2026",
            }
        )
        errors, _, _ = self.validate(row, end_of_round=True)
        self.assertTrue(any("cannot point superseded_by to itself" in error for error in errors))

    def test_valid_supersession_resolves_to_retained_assessed_source(self):
        superseded = base_row()
        superseded.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Weaker source",
                "canonical_url": "https://doi.org/10.0000/weaker",
                "relevance": "exclude",
                "acquisition_state": "SUPERSEDED",
                "terminal_reason": "Stronger direct source covers the intended claim",
                "superseded_by": "Replacement2026",
            }
        )
        replacement = base_row()
        replacement.update(
            {
                "source_id": "S2",
                "citation_key": "Replacement2026",
                "bibliographic_identity": "Stronger replacement",
                "canonical_url": "https://doi.org/10.0000/replacement",
                "relevance": "retain",
                "acquisition_state": "FULL_TEXT_ASSESSED",
                "full_copy_locator": "governed:sources/replacement.pdf",
                "full_text_review_locator": "source-manifest.md#S2",
                "evidence_register_locator": "evidence-strength-register.md#S2",
                "upgrade_search": "Independent upgrade and counterevidence search completed",
            }
        )
        self.assertEqual(
            self.validate_rows([superseded, replacement], end_of_round=True),
            ([], [], 2),
        )

    def test_placeholder_replacement_evidence_cannot_close_supersession(self):
        superseded = base_row()
        superseded.update(
            {
                "source_id": "S1",
                "bibliographic_identity": "Weaker source",
                "canonical_url": "https://doi.org/10.0000/weaker",
                "relevance": "exclude",
                "acquisition_state": "SUPERSEDED",
                "terminal_reason": "pending.",
                "superseded_by": "Replacement2026",
            }
        )
        replacement = base_row()
        replacement.update(
            {
                "source_id": "S2",
                "citation_key": "Replacement2026",
                "bibliographic_identity": "Purported stronger replacement",
                "canonical_url": "https://doi.org/10.0000/replacement",
                "relevance": "retain",
                "acquisition_state": "FULL_TEXT_ASSESSED",
                "full_copy_locator": "pending.",
                "full_text_review_locator": "`pending`",
                "evidence_register_locator": "governed:sources/TBD.",
                "upgrade_search": "**pending**",
            }
        )
        errors, _, _ = self.validate_rows(
            [superseded, replacement],
            end_of_round=True,
        )
        for phrase in (
            "placeholder value 'pending.' for terminal_reason",
            "placeholder value 'pending.' for full_copy_locator",
            "placeholder value '`pending`' for full_text_review_locator",
            "placeholder value 'governed:sources/TBD.' for evidence_register_locator",
            "placeholder value '**pending**' for upgrade_search",
        ):
            self.assertTrue(any(phrase in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
