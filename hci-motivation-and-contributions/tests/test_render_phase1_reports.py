from __future__ import annotations

import csv
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "render_phase1_reports.py"
SPEC = importlib.util.spec_from_file_location("render_phase1_reports", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
AUDIT_SCRIPT = Path(__file__).parents[1] / "scripts" / "audit_phase1_reports.py"
AUDIT_SPEC = importlib.util.spec_from_file_location("audit_phase1_reports", AUDIT_SCRIPT)
assert AUDIT_SPEC and AUDIT_SPEC.loader
AUDIT_MODULE = importlib.util.module_from_spec(AUDIT_SPEC)
sys.modules[AUDIT_SPEC.name] = AUDIT_MODULE
AUDIT_SPEC.loader.exec_module(AUDIT_MODULE)


class Phase1ReportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "research-framing"
        self.root.mkdir()
        (self.root / "decision-packets").mkdir()
        (self.root / "reviewer-panel").mkdir()
        (self.root / "reviews" / "2026-07-28").mkdir(parents=True)

        (self.root / "starting-state.md").write_text(
            "# Starting state\n\nA team project with <script>alert('x')</script>.",
            encoding="utf-8",
        )
        (self.root / "phase-1-collaboration-workboard.md").write_text(
            "# Phase 1 collaboration workboard\n\n"
            "Status: `ACTIVE`\n\n"
            "Highest-consequence open area: closest-work boundary.\n\n"
            "Constructive opposition: current support is insufficient; research first, "
            "then narrow or run a decision-matched probe.",
            encoding="utf-8",
        )
        (self.root / "author-decisions.md").write_text(
            "# Author decisions\n\n| Checkpoint | Choice | Rationale |\n"
            "|---|---|---|\n| Motivation | B — coordination | Stronger evidence |",
            encoding="utf-8",
        )
        (self.root / "terminology-contract.md").write_text(
            "# Terminology contract\n\n"
            "Semantic contract: player-specific names the addressee; "
            "recipient-differentiated names different content. "
            "Personalized remains reserved pending evidence.",
            encoding="utf-8",
        )
        (self.root / "prior-work-contribution-boundary.md").write_text(
            "# Prior-work contribution-boundary audit\n\n"
            "PWE-001: the shared channel is author-claimed, demonstrated, and operated. "
            "Its capability collision is exact and its matched contribution credit is full. "
            "Future-work proposals remain idea provenance with collision and credit both NONE.",
            encoding="utf-8",
        )
        template_assets = Path(__file__).parents[1] / "assets"
        for artifact_name in (
            "prior-work-evidence-accounting.csv",
            "idea-provenance-ledger.csv",
            "imported-bibliography-accountability.csv",
            "late-found-work-postmortem.csv",
            "novelty-regression-sentinels.yaml",
        ):
            (self.root / artifact_name).write_text(
                (template_assets / artifact_name).read_text(encoding="utf-8"),
                encoding="utf-8",
            )
        (self.root / "decision-packets" / "motivation.md").write_text(
            "# Motivation variations\n\n- A — participation scale\n"
            "- B — coordination consequence (Example et al.,\n"
            "  2024)\n- C — access and equity\n\n"
            "**Selected:** B — coordination consequence",
            encoding="utf-8",
        )
        (self.root / "source-manifest.md").write_text(
            "# Sources\n\n| Work | Full copy | DOI |\n|---|---|---|\n"
            "| Example et al. | checked | 10.1000/example |",
            encoding="utf-8",
        )
        (self.root / "source-resolution.csv").write_text(
            "source_id,citation_key,acquisition_state,relevance,"
            "request_surfaced_locator,affected_claims,"
            "fallback_or_narrowing,reopen_trigger\n"
            "S1,Example2024,NEEDS_AUTHOR_SOURCE_ACCESS,retain,"
            "session:019f-example#2026-07-29,WD-C001,"
            "Omit the blocked efficacy claim,"
            "Complete PDF obtained and fully audited\n",
            encoding="utf-8",
        )
        (self.root / "search-log.md").write_text(
            "# Search log\n\nQuery: `team coordination guidance CHI`",
            encoding="utf-8",
        )
        (self.root / "related-work-matrix.md").write_text(
            "# Related work\n\n## Same problem, different approach\n\n"
            "| Work | Effect | Interpretation |\n|---|---|---|\n"
            "| Example et al. 2024 | d\\|=1.028 | One intact evidence cell |\n",
            encoding="utf-8",
        )
        (self.root / "consequence-severity-ranking.md").write_text(
            "# Consequence severity ranking\n\n"
            "Status: `CONSEQUENCE_RANKING_COMPLETE`\n\n"
            "Lost sleep opportunity ranks first with moderate confidence; "
            "next-day impairment remains downstream.",
            encoding="utf-8",
        )
        (self.root / "evidence-strength-register.md").write_text(
            "# Evidence-strength register\n\n"
            "Ingestion: `FULL`. Claim strength: `ES2 — BOUNDED SUPPORT`.\n\n"
            "NotebookLM may propose a rating, but critical risk of bias can veto it. "
            "Unmarked references are `UNASSESSED`.",
            encoding="utf-8",
        )
        (self.root / "acm-sigchi-related-work-audit.md").write_text(
            "# ACM DL and SIGCHI related-work audit\n\n"
            "Status: `ACM_SIGCHI_LANDSCAPE_AUDITED`\n\n"
            "Native ACM DL queries locate the closest CHI and SIGCHI lineage. "
            "Venue priority does not upgrade evidence strength.",
            encoding="utf-8",
        )
        (self.root / "related-work-search-recall-audit.md").write_text(
            "# Related-work search-recall audit\n\n"
            "Status: `RELATED_WORK_SEARCH_RECALL_AUDITED`\n\n"
            "Mechanism sentinels pass after synonym and citation-title checks.",
            encoding="utf-8",
        )
        (self.root / "authoritative-source-map.md").write_text(
            "# Authoritative domain-source map\n\n"
            "Status: `AUTHORITATIVE_DOMAIN_SOURCES_MAPPED`\n\n"
            "Authority is mapped to remit, document type, and a cannot-support boundary.",
            encoding="utf-8",
        )
        (self.root / "motivation-claim-research-queue.md").write_text(
            "# Motivation-claim research queue\n\n"
            "Status: `MOTIVATION_CLAIM_AUDIT_COMPLETE`\n\n"
            "M7 used `B — official practice audit` and was narrowed after contradiction search.",
            encoding="utf-8",
        )
        (self.root / "current-practice-audit.md").write_text(
            "# Current-practice audit\n\n"
            "Official controls mix reminders, grayscale, bypasses, and hard blocks.",
            encoding="utf-8",
        )
        (self.root / "related-work-contribution-tier-audit.md").write_text(
            "# Contribution-strength audit\n\n"
            "Example et al. 2024 provides the closest capability comparison.\n\n"
            "**Rank:** Tier 1 — capability.",
            encoding="utf-8",
        )
        (self.root / "ranked-related-work-positioning.md").write_text(
            "# Ranked related-work positioning\n\n"
            "## 1. Example et al. (CHI 2024)\n\n"
            "Example et al. establish a complete comparison. CoachCast credits that "
            "capability before isolating one consequential interaction difference.",
            encoding="utf-8",
        )
        (self.root / "citation-chain-log.md").write_text(
            "# Citation chain\n\nA newer paper cites Example positively.",
            encoding="utf-8",
        )
        (self.root / "research-framing-outline.md").write_text(
            "# Research framing outline\n\nSelected direction: coordination support.",
            encoding="utf-8",
        )
        (self.root / "phase-2-handoff.md").write_text(
            "# Phase 2 handoff\n\nTest the core coordination premise.",
            encoding="utf-8",
        )
        (self.root / "exemplar-analysis.md").write_text(
            "# Exemplar analysis\n\nMRDrum informs the hourglass mechanism.",
            encoding="utf-8",
        )
        (self.root / "exemplar-related-work-positioning-analysis.md").write_text(
            "# Exemplar Related Work positioning\n\n"
            "Credit a predecessor, then isolate one contribution-level contrast.",
            encoding="utf-8",
        )
        (
            self.root
            / "reviews"
            / "2026-07-28"
            / "sol-pro-related-work-positioning.md"
        ).write_text(
            "# Sol Pro positioning correction\n\n"
            "Guided Teams is the strongest near-counterexample.",
            encoding="utf-8",
        )
        with (self.root / "references.csv").open(
            "w", newline="", encoding="utf-8"
        ) as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=(
                    "citation_key",
                    "author_year",
                    "short_title",
                    "venue_abbrev",
                    "full_title",
                    "full_authors",
                    "full_venue",
                    "url",
                    "aliases",
                ),
            )
            writer.writeheader()
            writer.writerow(
                {
                    "citation_key": "Example2024",
                    "author_year": "Example et al., 2024",
                    "short_title": "Guided Teams",
                    "venue_abbrev": "CHI",
                    "full_title": "Guided Teams: A Complete Example",
                    "full_authors": "Alice Example, Bob Example, and Carol Example",
                    "full_venue": "Proceedings of the ACM CHI Conference on Human Factors in Computing Systems",
                    "url": "https://doi.org/10.1000/example",
                    "aliases": "Example et al. 2024||Example-paper.pdf",
                }
            )

        ledger = self.root / "claim-evidence-ledger.csv"
        with ledger.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=(
                    "claim_id",
                    "framing_role",
                    "proposed_claim",
                    "evidence_state",
                    "status",
                ),
            )
            writer.writeheader()
            writer.writerow(
                {
                    "claim_id": "M1",
                    "framing_role": "motivation",
                    "proposed_claim": "The problem affects coordination.",
                    "evidence_state": "established-external",
                    "status": "verified",
                }
            )

    def tearDown(self):
        self.temporary.cleanup()

    def generate(self) -> dict[str, str]:
        output = self.root / "reports"
        paths = MODULE.generate_reports(
            self.root,
            output,
            project_title="CoachCast",
            generated_at="2026-07-26T12:00:00+08:00",
        )
        return {path.name: path.read_text(encoding="utf-8") for path in paths}

    def test_generates_all_three_self_contained_reports(self):
        reports = self.generate()
        self.assertEqual(set(reports), set(MODULE.ALL_REPORT_NAMES))
        for document in reports.values():
            self.assertIn("<style>", document)
            self.assertNotIn("<script", document.lower())
            self.assertNotIn("fonts.googleapis.com", document)
            self.assertIn("SHA-256", document)

    def test_acm_sigchi_audit_is_visible_in_all_reports(self):
        reports = self.generate()
        for name in MODULE.REPORT_NAMES:
            document = reports[name]
            self.assertIn("ACM DL and SIGCHI related-work audit", document)

    def test_incomplete_outline_is_not_labeled_final_or_decision_complete(self):
        document = self.generate()["phase-1-final.html"]
        self.assertIn("Phase 1 research direction — working draft", document)
        self.assertIn("this is not a completion or readiness decision", document)
        self.assertIn("Working research direction", document)
        self.assertNotIn("Phase 1 final research direction", document)
        self.assertNotIn("Decision-complete outline", document)

    def test_explicit_readiness_decision_uses_final_label(self):
        (self.root / "STATUS.md").write_text(
            "# Status\n\nReadiness: `READY_WITH_RISKS`\n",
            encoding="utf-8",
        )
        document = self.generate()["phase-1-final.html"]
        self.assertIn("Phase 1 final research direction", document)
        self.assertIn("Decision-complete outline", document)
        self.assertIn("Selected research direction", document)

    def test_progress_and_final_preserve_variations_and_choice(self):
        reports = self.generate()
        for name in ("phase-1-progress.html", "phase-1-final.html"):
            document = reports[name]
            self.assertIn("Motivation variations", document)
            self.assertIn("participation scale", document)
            self.assertIn("coordination consequence", document)
            self.assertIn("Author decisions", document)
            self.assertIn("Stronger evidence", document)

    def test_progress_and_final_include_live_collaboration_workboard(self):
        reports = self.generate()
        for name in ("phase-1-progress.html", "phase-1-final.html"):
            document = reports[name]
            self.assertIn("Phase 1 collaboration workboard", document)
            self.assertIn("Highest-consequence open area", document)
            self.assertIn("Constructive opposition", document)
        self.assertIn(
            "phase-1-collaboration-workboard.html",
            reports["artifact-index.html"],
        )

    def test_progress_and_final_include_the_terminology_contract(self):
        reports = self.generate()
        for name in ("phase-1-progress.html", "phase-1-final.html"):
            document = reports[name]
            self.assertIn("Terminology contract", document)
            self.assertIn("player-specific names the addressee", document)
            self.assertIn("Personalized remains reserved", document)

    def test_all_reports_preserve_prior_work_contribution_boundaries(self):
        reports = self.generate()
        for name in MODULE.REPORT_NAMES:
            document = reports[name]
            self.assertIn("Prior-work contribution-boundary audit", document)
            self.assertIn("author-claimed, demonstrated, and operated", document)
            self.assertIn("capability collision is exact", document)
            self.assertIn("contribution credit is full", document)
            self.assertIn("idea provenance with collision and credit both NONE", document)

    def test_all_reports_include_claim_strengthening_and_current_practice(self):
        reports = self.generate()
        for name in MODULE.REPORT_NAMES:
            document = reports[name]
            self.assertIn("Motivation-claim research queue", document)
            self.assertIn("MOTIVATION_CLAIM_AUDIT_COMPLETE", document)
            self.assertIn("Current-practice audit", document)
            self.assertIn("reminders, grayscale, bypasses, and hard blocks", document)

    def test_dated_review_syntheses_are_visible_in_progress_and_final(self):
        reports = self.generate()
        for name in ("phase-1-progress.html", "phase-1-final.html"):
            document = reports[name]
            self.assertIn("Sol Pro positioning correction", document)
            self.assertIn(
                "Example et al. (2024 CHI): Guided Teams</a> is the strongest",
                document,
            )

    def test_literature_report_contains_reference_and_evidence_records(self):
        document = self.generate()["literature-and-evidence.html"]
        self.assertIn("Example et al.", document)
        self.assertIn("10.1000/example", document)
        self.assertIn("team coordination guidance CHI", document)
        self.assertIn("established-external", document)
        self.assertIn("Citation chain", document)
        self.assertIn("MRDrum", document)
        self.assertIn("one contribution-level contrast", document)
        self.assertIn("Contribution-strength audit", document)
        self.assertIn("Tier 1 — capability", document)
        self.assertIn("Example et al. (2024 CHI): Guided Teams", document)
        self.assertIn("Guided Teams: A Complete Example", document)
        self.assertIn('title="Alice Example, Bob Example, and Carol Example.', document)
        self.assertIn("Consequence severity ranking", document)
        self.assertIn("Lost sleep opportunity ranks first", document)
        self.assertIn("Evidence-strength register", document)
        self.assertIn("ES2 — BOUNDED SUPPORT", document)
        self.assertIn("critical risk of bias can veto", document)
        self.assertIn("source-resolution.csv", document)
        self.assertIn("NEEDS_AUTHOR_SOURCE_ACCESS", document)
        self.assertIn("session:019f-example#2026-07-29", document)
        self.assertIn("WD-C001", document)
        self.assertIn("Omit the blocked efficacy claim", document)
        self.assertIn("Complete PDF obtained and fully audited", document)
        self.assertIn("Reader-facing artifact pages", document)
        self.assertIn("ranked-related-work-positioning.html", document)
        self.assertIn("Ranked related-work positioning", document)

    def test_venue_first_author_year_form_is_enriched(self):
        document = self.generate()["ranked-related-work-positioning.html"]
        self.assertIn(
            'class="citation" href="https://doi.org/10.1000/example"',
            document,
        )
        self.assertIn("Example et al. (2024 CHI): Guided Teams</a>", document)
        self.assertNotIn("Example et al. (CHI 2024)</h2>", document)

    def test_ranked_positioning_is_in_global_report_navigation(self):
        for document in self.generate().values():
            self.assertIn(
                '<a href="ranked-related-work-positioning.html">Ranked related work</a>',
                document,
            )

    def test_standalone_artifact_shelf_preserves_source_of_truth_boundary(self):
        reports = self.generate()
        index = reports["artifact-index.html"]
        self.assertIn("Markdown and CSV remain the editable, diffable sources of truth", index)
        self.assertIn("evidence-strength-register.html", index)
        self.assertIn("authoritative-source-map.html", index)
        self.assertIn("related-work-search-recall-audit.html", index)
        self.assertIn("source-resolution.html", index)
        positioning = reports["ranked-related-work-positioning.html"]
        self.assertIn("<code>ranked-related-work-positioning.md</code>", positioning)
        self.assertIn("SHA-256", positioning)

    def test_source_resolution_has_a_reader_facing_mirror(self):
        reports = self.generate()
        mirror = reports["source-resolution.html"]
        self.assertIn("<code>source-resolution.csv</code>", mirror)
        self.assertIn("NEEDS_AUTHOR_SOURCE_ACCESS", mirror)
        self.assertIn("Example et al. (2024 CHI): Guided Teams", mirror)

    def test_artifact_html_is_escaped(self):
        document = self.generate()["phase-1-progress.html"]
        self.assertIn("&lt;script&gt;", document)
        self.assertNotIn("<script>alert", document)

    def test_escaped_pipe_stays_in_one_table_cell(self):
        document = self.generate()["phase-1-progress.html"]
        self.assertIn("<td>d|=1.028</td>", document)
        self.assertNotIn("<td>d\\</td>", document)

    def test_unescaped_pipe_fails_instead_of_silently_truncating_table(self):
        malformed = (
            "| Work | Effect |\n"
            "|---|---|\n"
            "| Example et al. 2024 | d|=1.028 |\n"
        )
        with self.assertRaisesRegex(ValueError, "Escape literal pipes"):
            MODULE.markdown_to_html(malformed, MODULE.load_citation_catalog(self.root))

    def test_legacy_ledger_does_not_claim_all_states_are_unspecified(self):
        legacy_root = self.root / "legacy"
        legacy_root.mkdir()
        (legacy_root / "claim-evidence-ledger.csv").write_text(
            "claim_id,status\nC1,verified\n",
            encoding="utf-8",
        )
        metrics = MODULE.ledger_metrics(legacy_root)
        self.assertIn("legacy claim ledger", metrics)
        self.assertNotIn("<td>unspecified</td>", metrics)

    def test_citation_split_across_list_lines_is_enriched(self):
        document = self.generate()["phase-1-progress.html"]
        self.assertIn(
            "Example et al. (2024 CHI): Guided Teams</a>)</li>",
            document,
        )
        self.assertNotIn("Example et al.,\n", document)

    def test_explicit_citation_key_token_is_rendered(self):
        rendered = MODULE.inline_format(
            "The result is bounded [@Example2024].",
            MODULE.load_citation_catalog(self.root),
        )
        self.assertIn(
            'class="citation" href="https://doi.org/10.1000/example"',
            rendered,
        )
        self.assertIn("Example et al. (2024 CHI): Guided Teams</a>", rendered)
        complete_metadata = (
            "Alice Example, Bob Example, and Carol Example. "
            "Guided Teams: A Complete Example. "
            "Proceedings of the ACM CHI Conference on Human Factors in Computing Systems."
        )
        self.assertIn(f'title="{complete_metadata}"', rendered)
        self.assertIn(f'aria-label="{complete_metadata}"', rendered)
        self.assertNotIn("[@Example2024]", rendered)

    def test_unknown_explicit_citation_key_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "Unknown citation key 'Missing2024'"):
            MODULE.inline_format(
                "Unsupported [@Missing2024].",
                MODULE.load_citation_catalog(self.root),
            )

    def test_unique_first_author_surname_is_enriched(self):
        rendered = MODULE.inline_format(
            "Example provides the comparison.",
            MODULE.load_citation_catalog(self.root),
        )
        self.assertIn("Example et al. (2024 CHI): Guided Teams</a>", rendered)

    def test_ambiguous_alias_fails_instead_of_selecting_first_row(self):
        with (self.root / "references.csv").open(
            "a", newline="", encoding="utf-8"
        ) as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=(
                    "citation_key",
                    "author_year",
                    "short_title",
                    "venue_abbrev",
                    "full_title",
                    "full_authors",
                    "full_venue",
                    "url",
                    "aliases",
                ),
            )
            writer.writerow(
                {
                    "citation_key": "Other2025",
                    "author_year": "Other et al., 2025",
                    "short_title": "A Different System",
                    "venue_abbrev": "CHI",
                    "full_title": "A Different System",
                    "full_authors": "Olivia Other",
                    "full_venue": "Proceedings of CHI",
                    "url": "https://doi.org/10.1000/other",
                    "aliases": "Example-paper.pdf",
                }
            )
        with self.assertRaisesRegex(ValueError, "Ambiguous citation alias"):
            MODULE.load_citation_catalog(self.root)

    def test_duplicate_citation_key_fails_instead_of_overwriting(self):
        with (self.root / "references.csv").open(
            "a", newline="", encoding="utf-8"
        ) as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=(
                    "citation_key",
                    "author_year",
                    "short_title",
                    "venue_abbrev",
                    "full_title",
                    "full_authors",
                    "full_venue",
                    "url",
                    "aliases",
                ),
            )
            writer.writerow(
                {
                    "citation_key": "Example2024",
                    "author_year": "Other et al., 2025",
                    "short_title": "A Different System",
                    "venue_abbrev": "CHI",
                    "full_title": "A Different System",
                    "full_authors": "Olivia Other",
                    "full_venue": "Proceedings of CHI",
                    "url": "https://doi.org/10.1000/other",
                    "aliases": "",
                }
            )
        with self.assertRaisesRegex(ValueError, "Duplicate citation key 'Example2024'"):
            MODULE.load_citation_catalog(self.root)

    def test_audit_rejects_ambiguous_parenthetical_surname_shorthand(self):
        with (self.root / "references.csv").open(
            "a", newline="", encoding="utf-8"
        ) as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=(
                    "citation_key",
                    "author_year",
                    "short_title",
                    "venue_abbrev",
                    "full_title",
                    "full_authors",
                    "full_venue",
                    "url",
                    "aliases",
                ),
            )
            writer.writerow(
                {
                    "citation_key": "Example2025",
                    "author_year": "Example et al., 2025",
                    "short_title": "Second Guided Study",
                    "venue_abbrev": "CHI",
                    "full_title": "A Second Guided Study",
                    "full_authors": "Alice Example and Dana Different",
                    "full_venue": "Proceedings of CHI",
                    "url": "https://doi.org/10.1000/example2",
                    "aliases": "Example et al. 2025",
                }
            )
        (self.root / "research-framing-outline.md").write_text(
            "# Research framing outline\n\nHCI lineage (Example).",
            encoding="utf-8",
        )
        self.generate()
        errors, _ = AUDIT_MODULE.audit(self.root, self.root / "reports")
        self.assertTrue(
            any(
                "unresolved citation shorthand 'Example' could mean "
                "Example2024, Example2025" in error
                for error in errors
            )
        )

    def test_citation_alias_inside_file_path_is_not_rewritten(self):
        rendered = MODULE.inline_format(
            "internal:/papers/Example-paper.pdf",
            MODULE.load_citation_catalog(self.root),
        )
        self.assertEqual(rendered, "internal:/papers/Example-paper.pdf")

    def test_audit_rejects_noncanonical_citation_destination(self):
        self.generate()
        path = self.root / "reports" / "ranked-related-work-positioning.html"
        source = path.read_text(encoding="utf-8")
        source = source.replace(
            'class="citation" href="https://doi.org/10.1000/example"',
            'class="citation" href="https://doi.org/10.1000/wrong"',
            1,
        )
        path.write_text(source, encoding="utf-8")
        errors, _ = AUDIT_MODULE.audit(self.root, self.root / "reports")
        self.assertTrue(
            any("does not use its canonical destination" in error for error in errors)
        )

    def test_audit_rejects_citation_metadata_not_matching_catalog(self):
        self.generate()
        path = self.root / "reports" / "ranked-related-work-positioning.html"
        source = path.read_text(encoding="utf-8")
        source = source.replace(
            'title="Alice Example, Bob Example, and Carol Example.',
            'title="Incomplete metadata.',
            1,
        ).replace(
            'aria-label="Alice Example, Bob Example, and Carol Example.',
            'aria-label="Incomplete metadata.',
            1,
        )
        path.write_text(source, encoding="utf-8")
        errors, _ = AUDIT_MODULE.audit(self.root, self.root / "reports")
        self.assertTrue(
            any("metadata does not match full catalog record" in error for error in errors)
        )

    def test_generated_reports_pass_automated_audit(self):
        self.generate()
        errors, warnings = AUDIT_MODULE.audit(self.root, self.root / "reports")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_audit_fails_when_source_resolution_mirror_is_missing(self):
        self.generate()
        (self.root / "reports" / "source-resolution.html").unlink()
        errors, _ = AUDIT_MODULE.audit(self.root, self.root / "reports")
        self.assertTrue(
            any(
                "missing report" in error and "source-resolution.html" in error
                for error in errors
            )
        )

    def test_audit_fails_when_source_resolution_mirror_is_stale(self):
        self.generate()
        with (self.root / "source-resolution.csv").open(
            "a",
            encoding="utf-8",
        ) as handle:
            handle.write("S2,,DISCOVERED,undecided\n")
        errors, _ = AUDIT_MODULE.audit(self.root, self.root / "reports")
        self.assertTrue(
            any(
                "source-resolution.html: does not match current SHA-256" in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
