from __future__ import annotations

import csv
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
SCRIPT_DIR = ROOT / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

RENDER_SPEC = importlib.util.spec_from_file_location(
    "render_phase1_reports", SCRIPT_DIR / "render_phase1_reports.py"
)
RENDER = importlib.util.module_from_spec(RENDER_SPEC)
assert RENDER_SPEC.loader
sys.modules[RENDER_SPEC.name] = RENDER
RENDER_SPEC.loader.exec_module(RENDER)

AUDIT_SPEC = importlib.util.spec_from_file_location(
    "audit_phase1_reports", SCRIPT_DIR / "audit_phase1_reports.py"
)
AUDIT = importlib.util.module_from_spec(AUDIT_SPEC)
assert AUDIT_SPEC.loader
sys.modules[AUDIT_SPEC.name] = AUDIT
AUDIT_SPEC.loader.exec_module(AUDIT)


REFERENCE_HEADER = (
    "citation_key,author_year,short_title,venue_abbrev,full_title,"
    "full_authors,full_venue,url,aliases\n"
)


class Phase1MarkdownPublicationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp.name) / "Example"
        self.root = self.repo / "research-framing"
        self.output = self.root / "reports"
        self.root.mkdir(parents=True)
        self.output.mkdir()

        readme = (ROOT / "assets" / "project-readme.md").read_text(encoding="utf-8")
        (self.repo / "README.md").write_text(
            readme.replace("{{PROJECT_NAME}}", "Example"), encoding="utf-8"
        )

        for relative, text in {
            "phase-1-collaboration-workboard.md": (
                "# Workboard\n\n## Current state — read this first\n\n"
                "Direction is `planned`; no author decision is currently ready. "
                "Evidence comes from [@Example2024].\n"
            ),
            "starting-state.md": "# Starting state\n\nImported claims remain hypotheses.\n",
            "author-decisions.md": "# Author decisions\n\nNo decision yet.\n",
            "decision-packets/README.md": "# Decision packets\n\nNo packet yet.\n",
            "contribution-options.md": "# Contribution options\n\nCandidate C1 is `hypothesis`.\n",
            "terminology-contract.md": "# Terminology\n\nCandidate only.\n",
            "motivation-claim-research-queue.md": "# Motivation queue\n\nNo active row.\n",
            "missing-full-copies.md": "# Missing full copies\n\nNone.\n",
            "reviewer-panel/README.md": "# Reviewer panel\n\nPending.\n",
            "source-manifest.md": "# Source manifest\n\nLOCAL_SOURCE_FILES_RECONCILED\n",
            "notebooklm-maintenance.md": "# NotebookLM maintenance\n\nReconciled.\n",
            "authoritative-source-map.md": "# Authority map\n\nMapped.\n",
            "evidence-strength-register.md": "# Evidence register\n\nExample is assessed.\n",
            "current-practice-audit.md": "# Current practice\n\nAudited.\n",
            "consequence-severity-ranking.md": "# Consequences\n\nRanked.\n",
            "acm-sigchi-related-work-audit.md": "# ACM audit\n\nAudited.\n",
            "related-work-search-recall-audit.md": "# Search recall\n\nAudited.\n",
            "related-work-matrix.md": "# Related work matrix\n\nCompared.\n",
            "related-work-contribution-tier-audit.md": "# Contribution audit\n\nAudited.\n",
            "ranked-related-work-positioning.md": "# Ranked work\n\nExample [@Example2024].\n",
            "prior-work-contribution-boundary.md": "# Prior-work boundary\n\nBounded.\n",
            "citation-chain-log.md": "# Citation chain\n\nComplete.\n",
            "research-framing-outline.md": (
                "# Research framing outline\n\nDirection is planned.\n\n"
                "## 6. Selected approach hypothesis\n\nApproach remains planned.\n"
            ),
            "phase-2-handoff.md": "# Phase 2 handoff\n\nOptional and incomplete.\n",
        }.items():
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

        self.write_catalog()
        self.write_csv("source-resolution.csv", ["source_id", "citation_key", "acquisition_state"], [["S1", "Example2024", "FULL_TEXT_ASSESSED"]])
        self.write_csv("claim-evidence-ledger.csv", ["claim_id", "claim", "evidence_state"], [["C1", "Example claim", "established-external"]])
        self.write_csv("prior-work-evidence-accounting.csv", [f"field_{i}" for i in range(12)], [[str(i) for i in range(12)]])
        self.write_csv("idea-provenance-ledger.csv", ["idea_id", "proposal"], [["I1", "Example"]])
        self.write_csv("imported-bibliography-accountability.csv", ["source_id", "disposition"], [["S1", "retained"]])
        self.write_csv("late-found-work-postmortem.csv", ["source_id", "repair"], [])
        (self.root / "novelty-regression-sentinels.yaml").write_text("sentinels: []\n", encoding="utf-8")
        (self.root / "agent-context.json").write_text('{"phase": {"status": "active"}}\n', encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_catalog(self, *, duplicate_casefold: bool = False) -> None:
        rows = [
            [
                "Example2024",
                "Example et al., 2024",
                "Useful Example",
                "CHI",
                "A Useful Example for Testing",
                "Alex Example; Bailey Example",
                "Proceedings of CHI 2024",
                "https://doi.org/10.1000/example",
                "Example et al. 2024",
            ]
        ]
        if duplicate_casefold:
            rows.append(
                [
                    "example2024",
                    "Other et al., 2024",
                    "Other",
                    "CHI",
                    "Other Work",
                    "Other Author",
                    "Proceedings of CHI 2024",
                    "https://doi.org/10.1000/other",
                    "",
                ]
            )
        path = self.root / "references.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            handle.write(REFERENCE_HEADER)
            csv.writer(handle).writerows(rows)

    def write_csv(self, relative: str, fields: list[str], rows: list[list[str]]) -> None:
        path = self.root / relative
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(fields)
            writer.writerows(rows)

    def publish(self) -> dict[str, str]:
        return RENDER.generate_reports(self.root, project_title="Example")

    def test_publishes_markdown_only_and_all_required_views(self):
        documents = self.publish()
        self.assertEqual(set(documents), AUDIT.expected_report_names())
        self.assertFalse(list(self.output.glob("*.html")))
        for name in documents:
            self.assertTrue(name.endswith(".md"), name)
            self.assertTrue((self.output / name).is_file())

    def test_resolves_tokens_to_keyed_links_definitions_and_visible_references(self):
        self.publish()
        path = self.root / "ranked-related-work-positioning.md"
        source = path.read_text(encoding="utf-8")
        self.assertIn("[Example et al. (2024 CHI): Useful Example][Example2024]", source)
        self.assertIn(
            '[Example2024]: <https://doi.org/10.1000/example> "Alex Example; Bailey Example.',
            source,
        )
        self.assertIn("## References", source)
        self.assertIn("Stable key: `Example2024`", source)
        self.assertNotIn("[@Example2024]", RENDER.strip_code(RENDER.MANAGED_CITATION_RE.sub("", source)))

    def test_unknown_draft_key_fails_closed(self):
        path = self.root / "ranked-related-work-positioning.md"
        path.write_text("# Ranked\n\nUnknown [@Missing2025].\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unknown citation key"):
            self.publish()

    def test_completed_phase_fails_when_research_gates_are_open_or_templated(self):
        (self.root / "agent-context.json").write_text(
            '{"phase": {"status": "complete"}}\n', encoding="utf-8"
        )
        (self.root / "motivation-claim-research-queue.md").write_text(
            "# Queue\n\nStatus: `NEEDS_MOTIVATION_CLAIM_RESEARCH`\n\n"
            "Last sweep: YYYY-MM-DD\n\n- [ ] Search remains open.\n",
            encoding="utf-8",
        )
        errors: list[str] = []
        AUDIT.audit_phase_completion(self.root, errors)
        combined = "\n".join(errors)
        self.assertIn("requires Status `MOTIVATION_CLAIM_AUDIT_COMPLETE`", combined)
        self.assertIn("research gate item(s) remain unchecked", combined)
        self.assertIn("template placeholder 'YYYY-MM-DD' remains", combined)

    def test_completed_phase_accepts_terminal_populated_research_gates(self):
        (self.root / "agent-context.json").write_text(
            '{"phase": {"status": "complete"}}\n', encoding="utf-8"
        )
        terminal = {
            "motivation-claim-research-queue.md": (
                "MOTIVATION_CLAIM_AUDIT_COMPLETE",
                None,
                "Last sweep",
            ),
            "acm-sigchi-related-work-audit.md": (
                "ACM_SIGCHI_LANDSCAPE_AUDITED",
                "ACM_SIGCHI_LANDSCAPE_AUDITED",
                "Last checked",
            ),
            "related-work-search-recall-audit.md": (
                "RELATED_WORK_SEARCH_RECALL_AUDITED",
                "RELATED_WORK_SEARCH_RECALL_AUDITED",
                "Last checked",
            ),
        }
        for relative, (status, gate, date_label) in terminal.items():
            gate_line = f"\nGate: `{gate}`\n" if gate else ""
            (self.root / relative).write_text(
                f"# Gate\n\nStatus: `{status}`\n\n{date_label}: 2026-08-09\n"
                f"{gate_line}\n- [x] Completed.\n",
                encoding="utf-8",
            )
        errors: list[str] = []
        AUDIT.audit_phase_completion(self.root, errors)
        self.assertEqual(errors, [])

    def test_completed_phase_rejects_superficially_closed_real_gate_templates(self):
        (self.root / "agent-context.json").write_text(
            '{"phase": {"status": "complete"}}\n', encoding="utf-8"
        )
        replacements = {
            "motivation-claim-research-queue.md": (
                "NEEDS_MOTIVATION_CLAIM_RESEARCH",
                "MOTIVATION_CLAIM_AUDIT_COMPLETE",
                "Last sweep: YYYY-MM-DD",
                "Last sweep: 2026-08-09",
            ),
            "acm-sigchi-related-work-audit.md": (
                "NEEDS_ACM_SIGCHI_LANDSCAPE_RESEARCH",
                "ACM_SIGCHI_LANDSCAPE_AUDITED",
                "Last checked:",
                "Last checked: 2026-08-09",
            ),
            "related-work-search-recall-audit.md": (
                "NEEDS_RELATED_WORK_SEARCH_RECALL_AUDIT",
                "RELATED_WORK_SEARCH_RECALL_AUDITED",
                "Last checked: YYYY-MM-DD",
                "Last checked: 2026-08-09",
            ),
        }
        for relative, (open_status, terminal_status, old_date, new_date) in replacements.items():
            source = (ROOT / "assets" / relative).read_text(encoding="utf-8")
            source = source.replace(
                f"Status: `{open_status}`", f"Status: `{terminal_status}`", 1
            )
            source = source.replace(old_date, new_date, 1).replace("- [ ]", "- [x]")
            (self.root / relative).write_text(source, encoding="utf-8")

        errors: list[str] = []
        AUDIT.audit_phase_completion(self.root, errors)
        combined = "\n".join(errors)
        self.assertIn("requires Gate `ACM_SIGCHI_LANDSCAPE_AUDITED`", combined)
        self.assertIn("requires Gate `RELATED_WORK_SEARCH_RECALL_AUDITED`", combined)
        self.assertIn("blank table cell", combined)
        self.assertIn("unfinished table value", combined)

    def test_casefold_duplicate_catalog_key_fails_closed(self):
        self.write_catalog(duplicate_casefold=True)
        with self.assertRaisesRegex(ValueError, "case-folding"):
            self.publish()

    def test_managed_navigation_reaches_nested_documents(self):
        nested = self.root / "decision-packets" / "README.md"
        self.publish()
        source = nested.read_text(encoding="utf-8")
        self.assertIn("[Project overview](../../README.md)", source)
        self.assertIn("[Phase 1 index](../reports/artifact-index.md)", source)
        self.assertIn("[Live workboard](../phase-1-collaboration-workboard.md)", source)

    def test_fenced_tokens_remain_literal_but_inline_citation_tokens_are_published(self):
        path = self.root / "search-log.md"
        path.write_text(
            "# Search log\n\nUse `[@Example2024]` in migration examples.\n\n"
            "```markdown\n[@Example2024]\n```\n",
            encoding="utf-8",
        )
        self.publish()
        source = path.read_text(encoding="utf-8")
        self.assertEqual(source.count("[@Example2024]"), 1)
        self.assertIn("[Example et al. (2024 CHI): Useful Example][Example2024]", source)
        errors, _ = AUDIT.audit(self.root)
        self.assertEqual(errors, [])

    def test_source_resolution_mirror_links_existing_full_copy_locator(self):
        full_copy = self.root / "sources/full-text/example.pdf"
        full_copy.parent.mkdir(parents=True, exist_ok=True)
        full_copy.write_bytes(b"paper")
        self.write_csv(
            "source-resolution.csv",
            ["source_id", "citation_key", "acquisition_state", "full_copy_locator"],
            [["S1", "Example2024", "FULL_TEXT_ASSESSED", "sources/full-text/example.pdf"]],
        )
        documents = self.publish()
        self.assertIn(
            "[sources/full-text/example.pdf](<../sources/full-text/example.pdf>)",
            documents["source-resolution.md"],
        )

    def test_csv_semantic_prose_starting_with_url_is_not_linkified(self):
        prose = "https://publisher.example/paper returned CAPTCHA; then searched Crossref"
        self.write_csv(
            "source-resolution.csv",
            ["source_id", "citation_key", "acquisition_state", "attempted_routes"],
            [["S1", "Example2024", "NEEDS_AUTHOR_SOURCE_ACCESS", prose]],
        )
        documents = self.publish()
        mirror = documents["source-resolution.md"]
        self.assertIn(prose, mirror)
        self.assertNotIn(f"[{prose}]", mirror)

    def test_inline_code_citation_token_cannot_bypass_audit(self):
        (self.root / "search-log.md").write_text("# Search log\n", encoding="utf-8")
        self.publish()
        path = self.root / "search-log.md"
        source = path.read_text(encoding="utf-8")
        source = source.replace("# Search log", "# Search log\n\nHidden citation `[@Example2024]`.", 1)
        path.write_text(source, encoding="utf-8")
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("inline-code citation token" in error for error in errors), errors)

    def test_catalog_backed_author_or_title_year_shorthand_is_published_as_links(self):
        path = self.root / "research-framing-outline.md"
        path.write_text(
            "# Outline\n\n"
            "Closest idea work: Example et al. (CHI 2024).\n"
            "Closest system work: Useful Example (CHI 2024).\n",
            encoding="utf-8",
        )
        self.publish()
        published = path.read_text(encoding="utf-8")
        expected = "[Example et al. (2024 CHI): Useful Example][Example2024]"
        self.assertEqual(published.count(expected), 2)
        errors, _ = AUDIT.audit(self.root)
        self.assertEqual(errors, [])

    def test_unknown_author_year_shorthand_fails_closed(self):
        path = self.root / "research-framing-outline.md"
        path.write_text(
            "# Outline\n\nClosest work: Unknown et al. (CHI 2025).\n",
            encoding="utf-8",
        )
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        shorthand_errors = [
            error for error in errors if "unlinked scholarly citation shorthand" in error
        ]
        self.assertEqual(len(shorthand_errors), 1, shorthand_errors)
        self.assertIn("Unknown et al. (CHI 2025)", shorthand_errors[0])

    def test_ambiguous_catalog_shorthand_is_not_guessed(self):
        with (self.root / "references.csv").open("a", newline="", encoding="utf-8") as handle:
            csv.writer(handle).writerow(
                [
                    "ExampleOther2024",
                    "Example et al., 2024",
                    "A Different Example",
                    "CHI",
                    "A Different Example for Testing",
                    "Casey Example; Drew Example",
                    "Proceedings of CHI 2024",
                    "https://doi.org/10.1000/example-other",
                    "",
                ]
            )
        path = self.root / "research-framing-outline.md"
        path.write_text(
            "# Outline\n\nClosest work: Example et al. (CHI 2024).\n",
            encoding="utf-8",
        )
        self.publish()
        self.assertIn("Example et al. (CHI 2024)", path.read_text(encoding="utf-8"))
        errors, _ = AUDIT.audit(self.root)
        shorthand_errors = [
            error for error in errors if "unlinked scholarly citation shorthand" in error
        ]
        self.assertEqual(len(shorthand_errors), 1, shorthand_errors)
        self.assertNotIn("use [@", shorthand_errors[0])

    def test_linked_citation_shorthand_and_code_examples_pass(self):
        path = self.root / "research-framing-outline.md"
        path.write_text(
            "# Outline\n\n"
            "Closest work [@Example2024].\n\n"
            "`Example et al. (CHI 2024)` is a migration example.\n",
            encoding="utf-8",
        )
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertEqual(errors, [])

    def test_readme_framing_citations_require_explanation_and_difference(self):
        path = self.repo / "README.md"
        source = path.read_text(encoding="utf-8")
        source = source.replace(
            "## Closest prior work\n\n"
            "When the framing cites prior work, add one compact bullet per work using the exact structure\n"
            "`citation — **What it did:** evidence-bounded description. **How this project differs:** literal\n"
            "difference.` Do not leave citations as unexplained mechanism labels.\n",
            "## Closest prior work\n\n- [@Example2024] — progressive cues.\n",
        )
        path.write_text(source, encoding="utf-8")
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("comparison lacks **What it did:**" in error for error in errors))
        self.assertTrue(
            any("comparison lacks **How this project differs:**" in error for error in errors)
        )

        source = path.read_text(encoding="utf-8")
        source = RENDER.MANAGED_CITATION_RE.sub("", source)
        source = source.replace(
            "- [Example et al. (2024 CHI): Useful Example][Example2024] — progressive cues.",
            "- [@Example2024] — **What it did:** Tested a bounded intervention. "
            "**How this project differs:** Uses a different activation policy.",
        )
        path.write_text(source, encoding="utf-8")
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertEqual(errors, [])

    def test_readme_requires_iso_plain_language_profile_and_reader_tasks(self):
        path = self.repo / "README.md"
        source = path.read_text(encoding="utf-8")
        path.write_text(
            source.replace(
                "<!-- HCI-PLAIN-LANGUAGE: ISO 24495-1:2023 | audience=HCI researchers and project collaborators | tasks=understand the direction; inspect evidence; review decisions; continue to Phase 2 -->\n\n",
                "",
            ),
            encoding="utf-8",
        )
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("missing ISO 24495-1" in error for error in errors))

        source = path.read_text(encoding="utf-8")
        source = RENDER.MANAGED_CITATION_RE.sub("", source)
        source = source.replace(
            "# Example\n\n",
            "# Example\n\n"
            "<!-- HCI-PLAIN-LANGUAGE: ISO 24495-1:2023 | audience=reader | tasks=TBD -->\n\n",
        )
        path.write_text(source, encoding="utf-8")
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("must name intended readers" in error for error in errors))
        self.assertTrue(any("at least two reader tasks" in error for error in errors))

    def test_readme_requires_answer_first_and_task_grouped_structure(self):
        path = self.repo / "README.md"
        source = path.read_text(encoding="utf-8")
        source = source.replace("## At a glance", "## Background")
        source = source.replace(
            "### Inspect evidence\n\n",
            "",
        ).replace(
            "### Review decisions\n\n",
            "",
        ).replace(
            "### Continue to Phase 2 or inspect the complete record\n\n",
            "",
        )
        path.write_text(source, encoding="utf-8")
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("missing required section '## At a glance'" in error for error in errors))
        self.assertTrue(any("at least two reader goals" in error for error in errors))

    def test_readme_requires_user_value_intro_and_approach_substrate_boundary(self):
        path = self.repo / "README.md"
        source = path.read_text(encoding="utf-8")
        source = source.replace("## The user value", "## Value")
        source = source.replace("- **Platform-substitution result:**", "")
        path.write_text(source, encoding="utf-8")
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("missing required section '## The user value'" in error for error in errors))
        self.assertTrue(any("Introduction outline lacks 'Platform-substitution result'" in error for error in errors))

    def test_readme_requires_answer_first_and_approach_before_substrate_in_intro(self):
        path = self.repo / "README.md"
        source = path.read_text(encoding="utf-8")
        source = source.replace("## At a glance", "## Summary", 1)
        source = source.replace("## The user value", "## At a glance\n\nReplacement summary.\n\n## The user value", 1)
        source = source.replace(
            "- **Approach invariant:**\n- **Essential interaction/control-policy dimensions:**\n- **Implementation substrate / empirical waist:**",
            "- **Implementation substrate / empirical waist:**\n"
            "- **Essential interaction/control-policy dimensions:**\n"
            "- **Approach invariant:**",
            1,
        )
        path.write_text(source, encoding="utf-8")
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("At a glance must be the first" in error for error in errors))
        self.assertTrue(any("must state the approach invariant before" in error for error in errors))

    def test_readme_rejects_approach_labels_outside_intro(self):
        path = self.repo / "README.md"
        source = path.read_text(encoding="utf-8")
        source = source.replace("- **Platform-substitution result:**", "", 1)
        source += "\nOutside the outline: Platform-substitution result.\n"
        path.write_text(source, encoding="utf-8")
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("Introduction outline lacks 'Platform-substitution result'" in error for error in errors))

    def test_external_standard_url_ending_in_html_is_not_a_legacy_report(self):
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertEqual(errors, [])

    def test_legacy_token_wrapped_in_inline_link_becomes_one_keyed_citation(self):
        path = self.root / "approach-options.md"
        path.write_text(
            "# Approach\n\n"
            "The precedent is [GoalKeeper, `[@Example2024]`](https://doi.org/10.1000/example).\n",
            encoding="utf-8",
        )
        self.publish()
        source = path.read_text(encoding="utf-8")
        self.assertIn("[Example et al. (2024 CHI): Useful Example][Example2024]", source)
        self.assertNotIn("GoalKeeper,", source)
        self.assertNotIn("[@Example2024]", source)

    def test_wide_csv_uses_record_sections_instead_of_unreadable_table(self):
        self.publish()
        source = (self.output / "prior-work-evidence-accounting.md").read_text(encoding="utf-8")
        self.assertIn("### Record 1", source)
        self.assertIn("**field_11:** 11", source)
        self.assertNotIn("| field_0 |", source)

    def test_missing_optional_source_is_visible_without_broken_link(self):
        (self.root / "citation-chain-log.md").unlink()
        documents = self.publish()
        self.assertIn("`citation-chain-log.md` — **MISSING**", documents["literature-and-evidence.md"])

    def test_generated_publication_passes_audit(self):
        self.publish()
        errors, warnings = AUDIT.audit(self.root)
        self.assertEqual(warnings, [])
        self.assertEqual(errors, [])

    def test_second_publication_is_byte_identical(self):
        self.publish()
        first = {
            path.relative_to(self.repo): path.read_bytes()
            for path in sorted(self.repo.rglob("*.md"))
        }
        self.publish()
        second = {
            path.relative_to(self.repo): path.read_bytes()
            for path in sorted(self.repo.rglob("*.md"))
        }
        self.assertEqual(second, first)

    def test_ordinary_reference_style_link_is_preserved_and_audited(self):
        path = self.root / "approach-options.md"
        path.write_text(
            "# Approach\n\nSee [project documentation][project docs].\n\n"
            "[project docs]: <starting-state.md>\n",
            encoding="utf-8",
        )
        self.publish()
        source = path.read_text(encoding="utf-8")
        self.assertIn("[project documentation][project docs]", source)
        errors, _ = AUDIT.audit(self.root)
        self.assertEqual(errors, [])

    def test_internal_catalog_citation_resolves_through_reference_mirror(self):
        with (self.root / "references.csv").open("a", newline="", encoding="utf-8") as handle:
            csv.writer(handle).writerow(
                (
                    "Internal2024",
                    "Project team, 2024",
                    "Evidence Register",
                    "Project",
                    "Project Evidence Strength Register",
                    "Project team",
                    "Project evidence",
                    "internal:evidence-strength-register.md",
                    "",
                )
            )
        path = self.root / "approach-options.md"
        path.write_text("# Approach\n\nInternal evidence [@Internal2024].\n", encoding="utf-8")
        self.publish()
        mirror = (self.output / "references.md").read_text(encoding="utf-8")
        self.assertIn("](<../evidence-strength-register.md>)", mirror)
        errors, _ = AUDIT.audit(self.root)
        self.assertEqual(errors, [])

    def test_generated_links_encode_spaces_and_parentheses(self):
        path = self.root / "decision-packets" / "choice (final).md"
        path.write_text("# Final choice\n", encoding="utf-8")
        self.publish()
        index = (self.output / "artifact-index.md").read_text(encoding="utf-8")
        self.assertIn("choice%20%28final%29.md", index)
        errors, _ = AUDIT.audit(self.root)
        self.assertEqual(errors, [])

    def test_angle_wrapped_link_with_spaces_and_parentheses_is_valid(self):
        target = self.root / "decision-packets" / "choice (final).md"
        target.write_text("# Final choice\n", encoding="utf-8")
        source = self.root / "approach-options.md"
        source.write_text(
            "# Approach\n\n[Choice](<decision-packets/choice (final).md>)\n",
            encoding="utf-8",
        )
        self.publish()
        errors, _ = AUDIT.audit(self.root)
        self.assertEqual(errors, [])

    def test_source_change_makes_generated_report_stale(self):
        self.publish()
        path = self.root / "evidence-strength-register.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nChanged.\n", encoding="utf-8")
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("stale source hash" in error for error in errors), errors)

    def test_broken_relative_link_is_rejected(self):
        self.publish()
        path = self.root / "approach-options.md"
        path.write_text("# Approach\n\n[Missing](not-here.md)\n", encoding="utf-8")
        # Add the managed navigation block without republishing away the deliberate broken link.
        catalog = RENDER.load_citation_catalog(self.root)
        path.write_text(
            RENDER.synchronize_markdown(
                path, self.repo, self.root, self.output, catalog, add_navigation=True
            ),
            encoding="utf-8",
        )
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("broken relative link" in error for error in errors), errors)

    def test_machine_local_link_is_rejected(self):
        self.publish()
        path = self.root / "approach-options.md"
        path.write_text(
            "# Approach\n\n<!-- HCI-PHASE1-NAV:START -->\n"
            "[Project overview](../README.md)\n<!-- HCI-PHASE1-NAV:END -->\n\n"
            "[Local](/Users/example/private.pdf)\n",
            encoding="utf-8",
        )
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("machine-local absolute link" in error for error in errors), errors)

    def test_stale_html_is_rejected(self):
        self.publish()
        (self.output / "phase-1-final.html").write_text("legacy", encoding="utf-8")
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("stale generated HTML" in error for error in errors), errors)

    def test_nested_stale_html_is_rejected(self):
        self.publish()
        nested = self.output / "legacy" / "old.html"
        nested.parent.mkdir()
        nested.write_text("legacy", encoding="utf-8")
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any(str(nested) in error for error in errors), errors)

    def test_noncanonical_definition_is_rejected(self):
        self.publish()
        path = self.root / "ranked-related-work-positioning.md"
        source = path.read_text(encoding="utf-8").replace(
            "[Example2024]: <https://doi.org/10.1000/example>",
            "[Example2024]: <https://doi.org/10.1000/wrong>",
            1,
        )
        path.write_text(source, encoding="utf-8")
        errors, _ = AUDIT.audit(self.root)
        self.assertTrue(any("is not canonical" in error for error in errors), errors)

    def test_artifact_index_links_directly_and_hashes_sources(self):
        documents = self.publish()
        index = documents["artifact-index.md"]
        self.assertIn("[ranked-related-work-positioning.md](../ranked-related-work-positioning.md)", index)
        self.assertIn(RENDER.sha256(self.root / "ranked-related-work-positioning.md"), index)

    def test_progress_current_state_precedes_canonical_inventory(self):
        documents = self.publish()
        progress = documents["phase-1-progress.md"]
        self.assertLess(
            progress.index("## Current state — read this first"),
            progress.index("## Canonical records"),
        )


if __name__ == "__main__":
    unittest.main()
