from __future__ import annotations

import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_claim_ledger.py"
SPEC = importlib.util.spec_from_file_location("check_claim_ledger", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def base_row() -> dict[str, str]:
    return {column: "" for column in MODULE.REQUIRED_COLUMNS}


class ClaimLedgerTests(unittest.TestCase):
    def validate(self, row: dict[str, str], *, strict: bool = False):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=MODULE.REQUIRED_COLUMNS)
                writer.writeheader()
                writer.writerow(row)
            return MODULE.validate(path, strict)

    def test_verified_external_claim_requires_and_accepts_full_evidence(self):
        row = base_row()
        row.update(
            {
                "claim_id": "M1",
                "framing_role": "motivation",
                "proposed_claim": "A measured problem affects the target activity.",
                "evidence_state": "established-external",
                "claim_type": "prevalence",
                "source_tier": "T1",
                "directness": "direct",
                "citation_key": "Example2026",
                "source_identity": "Example study",
                "method": "Representative survey",
                "population_or_context": "Target population",
                "sample_or_coverage": "N=1000",
                "effect_or_estimate": "20%",
                "uncertainty_or_precision": "95% CI 18–22%",
                "locator": "p. 4",
                "doi_url_or_internal_path": "https://example.org/source",
                "limitations": "One country",
                "status": "verified",
            }
        )
        errors, warnings, count = self.validate(row, strict=True)
        self.assertEqual((errors, warnings, count), ([], [], 1))

    def test_hypothesis_can_remain_candidate_in_strict_mode(self):
        row = base_row()
        row.update(
            {
                "claim_id": "H1",
                "framing_role": "approach",
                "proposed_claim": "The proposed interaction may reduce coordination overhead.",
                "evidence_state": "hypothesis",
                "claim_type": "prospective benefit",
                "limitations": "Requires Phase 2 and Phase 3 evidence",
                "status": "candidate",
            }
        )
        errors, warnings, count = self.validate(row, strict=True)
        self.assertEqual((errors, warnings, count), ([], [], 1))

    def test_hypothesis_cannot_be_marked_verified(self):
        row = base_row()
        row.update(
            {
                "claim_id": "H1",
                "framing_role": "approach",
                "proposed_claim": "The proposed interaction improves coordination.",
                "evidence_state": "hypothesis",
                "claim_type": "prospective benefit",
                "status": "verified",
            }
        )
        errors, _, _ = self.validate(row)
        self.assertTrue(any("cannot be marked verified" in error for error in errors))

    def test_external_claim_without_source_tier_fails(self):
        row = base_row()
        row.update(
            {
                "claim_id": "M1",
                "framing_role": "motivation",
                "proposed_claim": "The problem is widespread.",
                "evidence_state": "established-external",
                "claim_type": "prevalence",
                "directness": "direct",
                "status": "candidate",
            }
        )
        errors, _, _ = self.validate(row)
        self.assertTrue(any("source_tier" in error for error in errors))

    def test_verified_bounded_external_inference_is_valid(self):
        row = base_row()
        row.update(
            {
                "claim_id": "RW1",
                "framing_role": "related-work boundary",
                "proposed_claim": (
                    "The published and demonstrated system uses one shared voice channel."
                ),
                "evidence_state": "inferred-external",
                "claim_type": "published-system communication topology",
                "source_tier": "T2A",
                "directness": "inferred",
                "citation_key": "Example2026",
                "source_identity": "Exact paper, supplement, and official demo",
                "method": "Complete first-party record plus bounded analytical inference",
                "population_or_context": "Published and demonstrated prototype",
                "sample_or_coverage": "All available first-party interaction records",
                "effect_or_estimate": "High-confidence shared-channel classification",
                "uncertainty_or_precision": "Scoped to the published/demonstrated system",
                "locator": "Internal inference record and source sections",
                "doi_url_or_internal_path": "internal:evidence-strength-register.md",
                "limitations": (
                    "Does not establish technical impossibility or unpublished behavior"
                ),
                "status": "verified",
            }
        )
        errors, warnings, count = self.validate(row, strict=True)
        self.assertEqual((errors, warnings, count), ([], [], 1))

    def test_inferred_external_requires_inferred_directness(self):
        row = base_row()
        row.update(
            {
                "claim_id": "RW1",
                "framing_role": "related-work boundary",
                "proposed_claim": "The published system uses one shared channel.",
                "evidence_state": "inferred-external",
                "claim_type": "published-system topology",
                "source_tier": "T2A",
                "directness": "direct",
                "method": "Complete first-party record plus bounded analytical inference",
                "status": "candidate",
            }
        )
        errors, _, _ = self.validate(row)
        self.assertTrue(
            any("require directness=inferred" in error for error in errors)
        )

    def test_inferred_external_must_use_published_scope(self):
        row = base_row()
        row.update(
            {
                "claim_id": "RW1",
                "framing_role": "related-work boundary",
                "proposed_claim": "The system uses one shared channel.",
                "evidence_state": "inferred-external",
                "claim_type": "system topology",
                "source_tier": "T2A",
                "directness": "inferred",
                "method": "Paper reading",
                "status": "candidate",
            }
        )
        errors, _, _ = self.validate(row)
        self.assertTrue(any("must be scoped" in error for error in errors))

    def test_inferred_directness_is_reserved_for_inferred_external(self):
        row = base_row()
        row.update(
            {
                "claim_id": "M1",
                "framing_role": "motivation",
                "proposed_claim": "A published study measured the problem.",
                "evidence_state": "established-external",
                "claim_type": "prevalence",
                "source_tier": "T1",
                "directness": "inferred",
                "status": "candidate",
            }
        )
        errors, _, _ = self.validate(row)
        self.assertTrue(
            any("reserved for inferred-external" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
