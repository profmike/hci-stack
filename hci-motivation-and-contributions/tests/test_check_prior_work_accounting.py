from __future__ import annotations

import csv
import importlib.util
import json
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_prior_work_accounting.py"
SPEC = importlib.util.spec_from_file_location("check_prior_work_accounting", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def write_csv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


class PriorWorkAccountingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.accounting_rows = [self.valid_accounting_row()]
        self.idea_rows: list[dict[str, str]] = []
        self.imported_rows: list[dict[str, str]] = []
        self.late_rows: list[dict[str, str]] = []
        self.source_rows = [
            {
                "source_id": "SRC-1",
                "source_provenance": "SEARCH",
                "acquisition_state": "FULL_TEXT_ASSESSED",
            }
        ]
        self.sentinels: list[dict[str, str]] = []
        self.write_project()

    def tearDown(self):
        self.temp.cleanup()

    def valid_accounting_row(self) -> dict[str, str]:
        row = {field: "" for field in MODULE.ACCOUNTING_COLUMNS}
        row.update(
            {
                "record_id": "PWE-001",
                "work_id": "WORK-1",
                "source_id": "SRC-1",
                "citation_key": "Example2026",
                "proposition_type": "ARTIFACT_CAPABILITY",
                "atomic_proposition": "A body movement triggers one jump command.",
                "unit_kind": "INPUT_CHANNEL",
                "smallest_operated_unit": "body movement to jump command",
                "channel_id": "movement-to-jump",
                "input_or_signal": "body movement",
                "mapped_command_or_effect": "jump command",
                "generalization_boundary": "jump only; no other command or whole-system class",
                "author_claim_status": "YES",
                "author_claim_evidence": "Contribution statement names the mapping.",
                "author_claim_locator": "p. 2",
                "demonstration_status": "YES",
                "demonstrated_artifact_or_study": "Implemented prototype condition",
                "demonstration_evidence": "The mapping executed during the study.",
                "demonstration_locator": "pp. 5-6",
                "operated_capability_status": "YES",
                "operated_capability": "movement triggered jump",
                "operation_evidence": "Execution trace and study task",
                "operation_locator": "p. 5",
                "evaluated_result_status": "N/A",
                "evidence_granularity": "ATOMIC_OPERATION",
                "causal_attribution_scope": "ATOMIC",
                "capability_collision": "EXACT",
                "collision_atom": "movement-to-jump mapping",
                "collision_scope": "one jump command",
                "collision_evidence_locator": "p. 5",
                "contribution_credit": "FULL",
                "contribution_atom": "movement-to-jump mapping",
                "credit_basis": "explicit claim plus matched demonstrated operation",
                "credit_scope": "one jump command",
                "credit_evidence_locator": "pp. 2, 5",
                "attribution_status": "CLAIMED_AND_DEMONSTRATED",
                "port_status": "NOT_A_PORT",
                "port_credit_gate": "NONE",
                "classification_scope": "ATOMIC_CHANNEL",
                "source_silence_disposition": "NOT_USED",
                "reopen_trigger": "new artifact version or stronger execution evidence",
            }
        )
        return row

    def valid_idea_row(self) -> dict[str, str]:
        row = {field: "" for field in MODULE.IDEA_COLUMNS}
        row.update(
            {
                "idea_id": "IDEA-001",
                "work_id": "WORK-1",
                "source_id": "SRC-1",
                "citation_key": "Example2026",
                "idea_type": "FUTURE_WORK",
                "idea_text": "Future versions could map a performance score to a badge.",
                "source_wording": "We envision score-driven badges.",
                "locator": "p. 10",
                "provenance_scope": "computed-state-to-reward idea only",
                "first_idea_language_consequence": "Do not claim first proposed.",
                "capability_collision": "NONE",
                "contribution_credit": "NONE",
                "prohibited_use": "realized capability, feasibility, effectiveness, or prior art",
                "reopen_trigger": "positive evidence that the channel actually operated",
            }
        )
        return row

    def valid_imported_row(self) -> dict[str, str]:
        row = {field: "" for field in MODULE.IMPORTED_COLUMNS}
        row.update(
            {
                "accountability_id": "IMP-1",
                "supplied_artifact": "draft.pdf",
                "bibliographic_identity": "Example Work",
                "citation_key": "Example2026",
                "potential_relevance": "MATERIAL",
                "independent_discovery_route": "mechanism query plus cited-by route",
                "source_resolution_id": "SRC-1",
                "terminal_disposition": "FULL_TEXT_ASSESSED",
                "terminal_reason": "material comparator",
                "full_copy_locator": "sources/example.pdf",
                "evidence_accounting_ids": "PWE-001",
                "upgrade_search": "authority and directness search complete",
                "affected_claims": "CLAIM-1",
                "reopen_trigger": "new version or changed focal claim",
            }
        )
        return row

    def write_project(self):
        write_csv(
            self.root / MODULE.ACCOUNTING_FILE,
            MODULE.ACCOUNTING_COLUMNS,
            self.accounting_rows,
        )
        write_csv(self.root / MODULE.IDEA_FILE, MODULE.IDEA_COLUMNS, self.idea_rows)
        write_csv(
            self.root / MODULE.IMPORTED_FILE,
            MODULE.IMPORTED_COLUMNS,
            self.imported_rows,
        )
        write_csv(self.root / MODULE.LATE_FILE, MODULE.LATE_COLUMNS, self.late_rows)
        write_csv(
            self.root / MODULE.SOURCE_RESOLUTION_FILE,
            ("source_id", "source_provenance", "acquisition_state"),
            self.source_rows,
        )
        (self.root / MODULE.SENTINEL_FILE).write_text(
            json.dumps({"schema_version": 1, "sentinels": self.sentinels}),
            encoding="utf-8",
        )
        (self.root / MODULE.BOUNDARY_FILE).write_text(
            "\n".join(f"- [x] `{marker}`" for marker in MODULE.COMPLETION_MARKERS),
            encoding="utf-8",
        )

    def validate(self) -> list[str]:
        errors, _, _ = MODULE.validate_project(self.root, strict=True)
        return errors

    def test_valid_atomic_accounting_passes(self):
        self.assertEqual(self.validate(), [])

    def test_future_work_stays_in_idea_ledger_with_zero_credit(self):
        self.idea_rows = [self.valid_idea_row()]
        self.write_project()
        self.assertEqual(self.validate(), [])

        self.idea_rows[0]["capability_collision"] = "EXACT"
        self.write_project()
        self.assertTrue(
            any("future work must use capability_collision=NONE" in error for error in self.validate())
        )

    def test_operated_but_unclaimed_can_collide_without_attribution(self):
        row = self.accounting_rows[0]
        row["author_claim_status"] = "NO"
        row["author_claim_evidence"] = "All contribution and capability claims audited."
        row["author_claim_locator"] = "pp. 1-12"
        row["contribution_credit"] = "NONE"
        for field in (
            "contribution_atom",
            "credit_basis",
            "credit_scope",
            "credit_evidence_locator",
        ):
            row[field] = ""
        row["attribution_status"] = "DEMONSTRATED_UNCLAIMED"
        self.write_project()
        self.assertEqual(self.validate(), [])

    def test_claimed_but_undemonstrated_gets_no_credit(self):
        row = self.accounting_rows[0]
        row["demonstration_status"] = "UNRESOLVED"
        row["operated_capability_status"] = "UNRESOLVED"
        row["capability_collision"] = "NONE"
        row["attribution_status"] = "CLAIMED_UNDEMONSTRATED"
        self.write_project()
        self.assertTrue(
            any("contribution credit requires both" in error for error in self.validate())
        )

    def test_claimed_but_undemonstrated_with_zero_credit_passes(self):
        row = self.accounting_rows[0]
        row.update(
            {
                "demonstration_status": "UNRESOLVED",
                "operated_capability_status": "UNRESOLVED",
                "capability_collision": "NONE",
                "contribution_credit": "NONE",
                "attribution_status": "CLAIMED_UNDEMONSTRATED",
            }
        )
        for field in (
            "collision_atom",
            "collision_scope",
            "collision_evidence_locator",
            "contribution_atom",
            "credit_basis",
            "credit_scope",
            "credit_evidence_locator",
        ):
            row[field] = ""
        self.write_project()
        self.assertEqual(self.validate(), [])

    def test_positive_operation_requires_positive_demonstration(self):
        row = self.accounting_rows[0]
        row.update(
            {
                "demonstration_status": "UNRESOLVED",
                "contribution_credit": "NONE",
                "attribution_status": "CLAIMED_UNDEMONSTRATED",
            }
        )
        for field in (
            "contribution_atom",
            "credit_basis",
            "credit_scope",
            "credit_evidence_locator",
        ):
            row[field] = ""
        self.write_project()
        self.assertTrue(
            any(
                "positive operated capability requires a matched positive demonstration"
                in error
                for error in self.validate()
            )
        )

    def test_pure_port_cannot_receive_contribution_credit(self):
        row = self.accounting_rows[0]
        row["port_status"] = "PORT_ONLY"
        self.write_project()
        self.assertTrue(
            any("PORT_ONLY receives contribution_credit=NONE" in error for error in self.validate())
        )

    def test_pure_port_cannot_claim_an_adaptation_gate(self):
        row = self.accounting_rows[0]
        row.update(
            {
                "port_status": "PORT_ONLY",
                "port_credit_gate": "DEMONSTRATED_NONTRIVIAL_ADAPTATION",
                "contribution_credit": "NONE",
            }
        )
        for field in (
            "contribution_atom",
            "credit_basis",
            "credit_scope",
            "credit_evidence_locator",
        ):
            row[field] = ""
        self.write_project()
        self.assertTrue(
            any(
                "PORT_ONLY must use port_credit_gate=NONE" in error
                for error in self.validate()
            )
        )

    def test_mixed_channels_pass_atomically_but_fail_as_unsupported_whole_system(self):
        advance = self.accounting_rows[0]
        advance.update(
            {
                "record_id": "PWE-ADVANCE",
                "channel_id": "speech-to-next-slide",
                "smallest_operated_unit": "spoken next to advance-one-slide command",
                "input_or_signal": "spoken next",
                "mapped_command_or_effect": "advance one slide",
                "generalization_boundary": "one slide advance only; not arbitrary navigation or general presentation control",
                "operated_capability": "spoken next advanced one slide",
                "collision_atom": "speech-to-next-slide",
                "collision_scope": "one slide advance only",
                "contribution_atom": "speech-to-next-slide",
                "credit_scope": "one slide advance only",
            }
        )
        navigation = deepcopy(advance)
        navigation.update(
            {
                "record_id": "PWE-NAVIGATION",
                "channel_id": "keyboard-to-navigation",
                "smallest_operated_unit": "keyboard to slide navigation",
                "input_or_signal": "keyboard",
                "mapped_command_or_effect": "slide navigation",
                "generalization_boundary": "keyboard navigation only",
                "operated_capability": "keyboard controlled slide navigation",
                "collision_atom": "conventional slide navigation",
                "collision_scope": "slide navigation only",
                "contribution_atom": "conventional slide navigation",
                "credit_scope": "slide navigation only",
            }
        )
        reward = deepcopy(advance)
        reward.update(
            {
                "record_id": "PWE-REWARD",
                "unit_kind": "REWARD_CHANNEL",
                "channel_id": "score-to-badge",
                "smallest_operated_unit": "task-performance score to badge",
                "input_or_signal": "task-performance score",
                "mapped_command_or_effect": "badge",
                "generalization_boundary": "computed-state-to-reward only; not user-action-to-command",
                "operated_capability": "task-performance score yielded a badge",
                "collision_atom": "computed-state-to-reward",
                "collision_scope": "reward channel only",
                "contribution_atom": "computed-state-to-reward",
                "credit_scope": "reward channel only",
            }
        )
        self.accounting_rows = [advance, navigation, reward]
        self.write_project()
        self.assertEqual(self.validate(), [])

        whole = deepcopy(advance)
        whole.update(
            {
                "record_id": "PWE-WHOLE",
                "unit_kind": "CONDITION",
                "channel_id": "",
                "classification_scope": "WHOLE_SYSTEM",
                "required_channel_set": "forward||direction||reward",
                "qualified_channel_set": "forward",
            }
        )
        self.accounting_rows.append(whole)
        self.write_project()
        self.assertTrue(
            any("every required channel" in error for error in self.validate())
        )

        whole["required_channel_set"] = (
            "speech-to-next-slide||keyboard-to-navigation||score-to-badge"
        )
        whole["qualified_channel_set"] = whole["required_channel_set"]
        self.accounting_rows = [advance, navigation, whole]
        self.write_project()
        self.assertTrue(
            any(
                "score-to-badge" in error
                and "lacks a positively demonstrated operated ATOMIC_CHANNEL row" in error
                for error in self.validate()
            )
        )

    def test_source_silence_cannot_become_negative_capability_evidence(self):
        row = self.accounting_rows[0]
        row.update(
            {
                "author_claim_status": "UNRESOLVED",
                "demonstration_status": "UNRESOLVED",
                "operated_capability_status": "NO",
                "evaluated_result_status": "UNRESOLVED",
                "capability_collision": "UNRESOLVED",
                "contribution_credit": "NONE",
                "attribution_status": "UNRESOLVED",
                "source_silence_disposition": "REOPEN_QUERY",
                "search_priority_or_reopen_query": "inspect artifact repository",
            }
        )
        self.write_project()
        self.assertTrue(
            any("source silence can only leave operated capability UNRESOLVED" in error for error in self.validate())
        )

    def test_package_condition_cannot_support_operator_specific_causality(self):
        row = self.accounting_rows[0]
        row["evidence_granularity"] = "PACKAGE_CONDITION"
        row["causal_attribution_scope"] = "PACKAGE_ONLY"
        row["classification_scope"] = "PACKAGE_ONLY"
        row["collision_scope"] = "isolated repetition operator"
        row["credit_scope"] = "isolated repetition operator"
        self.write_project()
        self.assertTrue(
            any("package evidence cannot support operator-specific" in error for error in self.validate())
        )

    def test_nonsignificance_cannot_establish_comparability(self):
        row = self.accounting_rows[0]
        row["evaluated_result_status"] = "YES"
        row["evaluated_result"] = "Enjoyment was maintained and comparable to baseline."
        row["evaluation_design_or_measure"] = "Within-subject test with nonsignificant p-value"
        row["evaluation_locator"] = "p. 8"
        self.write_project()
        self.assertTrue(
            any("requires an equivalence or non-inferiority design" in error for error in self.validate())
        )

    def test_material_imported_citation_must_resolve_terminally(self):
        row = self.valid_imported_row()
        row["source_resolution_id"] = "SRC-MISSING"
        self.imported_rows = [row]
        self.write_project()
        self.assertTrue(
            any("does not resolve" in error for error in self.validate())
        )

    def test_imported_citation_requires_an_independent_discovery_route(self):
        row = self.valid_imported_row()
        self.imported_rows = [row]
        self.write_project()
        self.assertEqual(self.validate(), [])

        row["independent_discovery_route"] = ""
        self.write_project()
        self.assertTrue(
            any(
                "imported bibliography row" in error
                and "independent_discovery_route" in error
                for error in self.validate()
            )
        )

    def test_late_found_source_requires_postmortem_and_regression_sentinel(self):
        self.source_rows.append(
            {
                "source_id": "SRC-LATE",
                "source_provenance": "LATE_FOUND",
                "acquisition_state": "FULL_TEXT_ASSESSED",
            }
        )
        self.write_project()
        self.assertTrue(
            any("lacks a postmortem" in error for error in self.validate())
        )

    def test_unchecked_completion_marker_fails_closed(self):
        marker_text = "\n".join(
            f"- [{' ' if index == 0 else 'x'}] `{marker}`"
            for index, marker in enumerate(MODULE.COMPLETION_MARKERS)
        )
        (self.root / MODULE.BOUNDARY_FILE).write_text(marker_text, encoding="utf-8")
        self.assertTrue(
            any("unchecked completion marker" in error for error in self.validate())
        )


if __name__ == "__main__":
    unittest.main()
