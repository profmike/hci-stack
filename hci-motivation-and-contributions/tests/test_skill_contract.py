import json
from pathlib import Path
import unittest


ROOT = Path(__file__).parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
PIPELINE = (ROOT / "references" / "pipeline-contract.md").read_text(encoding="utf-8")
POSITIONING = (
    ROOT / "references" / "related-work-positioning.md"
).read_text(encoding="utf-8")
ACM_SIGCHI = (
    ROOT / "references" / "acm-sigchi-related-work.md"
).read_text(encoding="utf-8")
FORWARD_CITATIONS = (
    ROOT / "references" / "forward-citation-expansion.md"
).read_text(encoding="utf-8")
RELATED_WORK_CONTRACT = f"{SKILL}\n{POSITIONING}"
ACM_AUDIT_TEMPLATE = (
    ROOT / "assets" / "acm-sigchi-related-work-audit.md"
).read_text(encoding="utf-8")
SEARCH_RECALL_TEMPLATE = (
    ROOT / "assets" / "related-work-search-recall-audit.md"
).read_text(encoding="utf-8")
SOURCE_RESOLUTION_TEMPLATE = (
    ROOT / "assets" / "source-resolution.csv"
).read_text(encoding="utf-8")
SOURCE_MANIFEST_TEMPLATE = (
    ROOT / "assets" / "source-manifest.md"
).read_text(encoding="utf-8")
MISSING_FULL_COPIES_TEMPLATE = (
    ROOT / "assets" / "missing-full-copies.md"
).read_text(encoding="utf-8")
NOTEBOOKLM = (
    ROOT / "references" / "notebooklm-research.md"
).read_text(encoding="utf-8")
NOTEBOOKLM_MAINTENANCE = (
    ROOT / "assets" / "notebooklm-maintenance.md"
).read_text(encoding="utf-8")
AGENT_CONTEXT = json.loads(
    (ROOT / "assets" / "agent-context.json").read_text(encoding="utf-8")
)
AUTHORITATIVE_SOURCES = (
    ROOT / "references" / "authoritative-domain-sources.md"
).read_text(encoding="utf-8")
AUTHORITATIVE_SOURCE_TEMPLATE = (
    ROOT / "assets" / "authoritative-source-map.md"
).read_text(encoding="utf-8")
AUDIT_TEMPLATE = (
    ROOT / "assets" / "related-work-contribution-tier-audit.md"
).read_text(encoding="utf-8")
OUTLINE_TEMPLATE = (
    ROOT / "assets" / "research-framing-outline.md"
).read_text(encoding="utf-8")
RUBRIC = (ROOT / "references" / "contribution-rubric.md").read_text(encoding="utf-8")
EVIDENCE = (ROOT / "references" / "evidence-protocol.md").read_text(
    encoding="utf-8"
)
CLAIM_FOCUSED_WRITING = (
    ROOT / "references" / "claim-focused-writing.md"
).read_text(encoding="utf-8")
QUADRANT = (ROOT / "references" / "related-work-quadrant.md").read_text(
    encoding="utf-8"
)
AUTHOR_COLLABORATION = (
    ROOT / "references" / "author-collaboration.md"
).read_text(encoding="utf-8")
ACTIVE_AUTHOR_COLLABORATION = (
    ROOT / "references" / "active-author-collaboration.md"
).read_text(encoding="utf-8")
PHASE_1_WORKBOARD = (
    ROOT / "assets" / "phase-1-collaboration-workboard.md"
).read_text(encoding="utf-8")
TERMINOLOGY = (
    ROOT / "references" / "terminology-contract.md"
).read_text(encoding="utf-8")
TERMINOLOGY_TEMPLATE = (
    ROOT / "assets" / "terminology-contract.md"
).read_text(encoding="utf-8")
BOUNDARY_TEMPLATE = (
    ROOT / "assets" / "prior-work-contribution-boundary.md"
).read_text(encoding="utf-8")
ACCOUNTING_TEMPLATE = (
    ROOT / "assets" / "prior-work-evidence-accounting.csv"
).read_text(encoding="utf-8")
IDEA_PROVENANCE_TEMPLATE = (
    ROOT / "assets" / "idea-provenance-ledger.csv"
).read_text(encoding="utf-8")
IMPORTED_ACCOUNTABILITY_TEMPLATE = (
    ROOT / "assets" / "imported-bibliography-accountability.csv"
).read_text(encoding="utf-8")
LATE_FOUND_TEMPLATE = (
    ROOT / "assets" / "late-found-work-postmortem.csv"
).read_text(encoding="utf-8")
NOVELTY_SENTINEL_TEMPLATE = (
    ROOT / "assets" / "novelty-regression-sentinels.yaml"
).read_text(encoding="utf-8")
PRIOR_WORK_CHECKER = (
    ROOT / "scripts" / "check_prior_work_accounting.py"
).read_text(encoding="utf-8")
PRIOR_WORK_BOUNDARIES = (
    ROOT / "references" / "prior-work-contribution-boundaries.md"
).read_text(encoding="utf-8")
AUTHOR_DECISIONS = (ROOT / "assets" / "author-decisions.md").read_text(
    encoding="utf-8"
)
DECISION_PACKET = (ROOT / "assets" / "decision-packet.md").read_text(
    encoding="utf-8"
)
PHASE_2_HANDOFF = (ROOT / "assets" / "phase-2-handoff.md").read_text(
    encoding="utf-8"
)
CONSEQUENCE_RESEARCH = (
    ROOT / "references" / "consequence-severity-research.md"
).read_text(encoding="utf-8")
CONSEQUENCE_TEMPLATE = (
    ROOT / "assets" / "consequence-severity-ranking.md"
).read_text(encoding="utf-8")
EVIDENCE_STRENGTH_TEMPLATE = (
    ROOT / "assets" / "evidence-strength-register.md"
).read_text(encoding="utf-8")
MOTIVATION_STRENGTHENING = (
    ROOT / "references" / "motivation-claim-strengthening.md"
).read_text(encoding="utf-8")
MOTIVATION_QUEUE_TEMPLATE = (
    ROOT / "assets" / "motivation-claim-research-queue.md"
).read_text(encoding="utf-8")
CURRENT_PRACTICE_TEMPLATE = (
    ROOT / "assets" / "current-practice-audit.md"
).read_text(encoding="utf-8")
RANKED_POSITIONING_TEMPLATE = (
    ROOT / "assets" / "ranked-related-work-positioning.md"
).read_text(encoding="utf-8")
HTML_REPORTS = (ROOT / "references" / "html-reports.md").read_text(
    encoding="utf-8"
)
PROJECT_README = (ROOT / "assets" / "project-readme.md").read_text(
    encoding="utf-8"
)
WORKSPACE_INITIALIZER = (
    ROOT / "scripts" / "initialize_phase1_workspace.py"
).read_text(encoding="utf-8")
CITATION_INTEGRITY = (
    ROOT / "references" / "citation-integrity.md"
).read_text(encoding="utf-8")
REPOSITORY_BOUNDARIES = (
    ROOT / "references" / "repository-boundaries.md"
).read_text(encoding="utf-8")
DETAILED_WORKFLOW = (
    ROOT / "references" / "phase-1-research-workflow.md"
).read_text(encoding="utf-8")
PHASE_ONE_INSTRUCTIONS = SKILL + "\n" + DETAILED_WORKFLOW


class SkillContractTests(unittest.TestCase):
    def test_acm_dl_and_sigchi_related_work_gate_is_required(self):
        self.assertIn("native ACM Digital Library pass", PHASE_ONE_INSTRUCTIONS)
        self.assertIn("[acm-sigchi-related-work.md]", PHASE_ONE_INSTRUCTIONS)
        self.assertIn("acm-sigchi-related-work-audit.md", PHASE_ONE_INSTRUCTIONS)
        self.assertIn("ACM_SIGCHI_LANDSCAPE_AUDITED", PHASE_ONE_INSTRUCTIONS)
        self.assertIn("https://sigchi.org/conferences/", ACM_SIGCHI)
        for family in (
            "Target problem",
            "Neighboring constructs",
            "Causal interaction mechanism",
            "Closest conjunction",
            "Known seeds and lineage",
        ):
            self.assertIn(family, ACM_SIGCHI)
            self.assertIn(family, ACM_AUDIT_TEMPLATE)

    def test_related_work_search_has_recall_regression_gates(self):
        self.assertIn("related-work-search-recall-audit.md", SKILL)
        self.assertIn("RELATED_WORK_SEARCH_RECALL_AUDITED", SKILL)
        for phrase in (
            "synonym lattice",
            "mechanism-only",
            "first page or first 20",
            "positive-control sentinels",
            "reference list",
            "two independent discovery routes",
            "process failure",
        ):
            self.assertIn(phrase, ACM_SIGCHI)
        for field in (
            "Mechanism and problem synonym lattice",
            "Positive-control and sentinel recall",
            "Reference-list title accountability",
            "Late-found-close-work postmortem",
            "Large-result-set handling",
        ):
            self.assertIn(field, SEARCH_RECALL_TEMPLATE)

    def test_forward_citation_expansion_is_broad_multiroute_and_multiwave(self):
        self.assertIn(
            "[forward-citation-expansion.md](references/forward-citation-expansion.md)",
            SKILL,
        )
        self.assertIn(
            "[forward-citation-expansion.md](forward-citation-expansion.md)",
            DETAILED_WORKFLOW,
        )
        for phrase in (
            "high-leverage seed portfolio",
            "every retained author-provided seed",
            "complements rather than replaces",
            "Citation graphs can be incomplete",
            "canonical intervention-family",
            "strongest design/mechanism foundation",
            "two genuinely independent cited-by indexes",
            "newest-first",
            "relevance- or citation-ranked",
            "Screen all unique citing records when tractable",
            "never treat the first page",
            "Wave 0",
            "Wave 1",
            "Wave 2+",
            "one complete promotion wave",
            "zero new decision-relevant works",
            "sibling citing records",
            "novelty-regression-sentinels.yaml",
            "decision relevance rather than title or semantic similarity",
        ):
            self.assertIn(phrase, FORWARD_CITATIONS)
        for field in (
            "High-leverage forward-citation seed portfolio",
            "Forward-citation expansion wave ledger",
            "Forward-citation candidate accountability",
            "Route A",
            "Route B",
            "Coverage current through",
            "New vocabulary or branch",
            "Promoted seeds for next wave",
            "Zero-yield/stopping result",
        ):
            self.assertIn(field, SEARCH_RECALL_TEMPLATE)
        for text in (ACM_SIGCHI, DETAILED_WORKFLOW, ACM_AUDIT_TEMPLATE):
            self.assertIn("high-leverage", text)
            self.assertIn("zero-yield", text)
        self.assertIn("sibling-citation sweep", SEARCH_RECALL_TEMPLATE)

    def test_every_component_gets_foundations_falsifiers_and_lineage(self):
        for text in (SKILL, DETAILED_WORKFLOW, ACM_SIGCHI):
            self.assertIn("component-foundation and falsification pass", text)
        for phrase in (
            "grayscale",
            "luminance",
            "blue-light",
            "latency",
            "rebuffering",
            "QoE",
            "abandonment",
            "product lineage",
            "supplied-bibliography accountability",
        ):
            self.assertIn(phrase.lower(), DETAILED_WORKFLOW.lower())
        for phrase in (
            "Component-foundation and falsification pass",
            "Discipline-specific vocabulary",
            "Counterevidence or failure-mode queries",
            "Product or intervention lineage",
        ):
            self.assertIn(phrase, ACM_AUDIT_TEMPLATE)
        self.assertIn("Supplied-bibliography accountability", SEARCH_RECALL_TEMPLATE)

    def test_author_provided_references_are_seeds_not_the_evidence_ceiling(self):
        for text in (
            SKILL,
            DETAILED_WORKFLOW,
            EVIDENCE,
            AUTHOR_COLLABORATION,
            NOTEBOOKLM,
        ):
            self.assertIn("seed", text.lower())
            self.assertIn("evidence ceiling", text)
        for text in (SKILL, DETAILED_WORKFLOW, EVIDENCE):
            self.assertIn("venue prestige", text.lower())
        for axis in (
            "institutional authority",
            "design validity",
            "directness",
            "currency",
            "publication",
        ):
            self.assertIn(axis, EVIDENCE.lower())
        for phrase in (
            "Claim-matched authority/method/directness upgrade search",
            "Stronger/counter source found",
            "retained with explicit bounds",
            "corroborated",
            "superseded",
        ):
            self.assertIn(phrase, SEARCH_RECALL_TEMPLATE)
        self.assertIn(
            "Author-provided references and stronger-source upgrades",
            PHASE_1_WORKBOARD,
        )
        self.assertIn(
            "Independent stronger/counter-source upgrade search",
            PHASE_1_WORKBOARD,
        )
        self.assertIn("Provenance / seed status", EVIDENCE_STRENGTH_TEMPLATE)
        self.assertIn(
            "Upgrade/counterevidence search and disposition",
            EVIDENCE_STRENGTH_TEMPLATE,
        )
        normalized_handoff = " ".join(PHASE_2_HANDOFF.split())
        for phrase in (
            "Stable citation keys and full-review locators",
            "Unobtained or inaccessible sources and affected blocked/narrowed claims",
            "Exact author-access request",
            "Component-foundation/falsification results",
            "Product or intervention lineage",
            "Author-provided seed provenance",
            "Independent stronger/counter-source search and disposition",
            "opened full copies or clearly marked project evidence",
            "prose cannot omit or upgrade",
        ):
            self.assertIn(phrase, normalized_handoff)
        self.assertIn(
            "treat author-provided references as search seeds rather than the evidence ceiling",
            (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8"),
        )

    def test_authoritative_sources_are_mapped_by_claim_and_remit(self):
        self.assertIn("[authoritative-domain-sources.md]", SKILL)
        self.assertIn("authoritative-source-map.md", SKILL)
        self.assertIn("AUTHORITATIVE_DOMAIN_SOURCES_MAPPED", SKILL)
        for phrase in (
            "Authority is claim-specific",
            "WHO",
            "AASM",
            "Sleep Research Society",
            "ACSM",
            "not “ASCM”",
            "Official product documentation",
            "cannot support",
        ):
            self.assertIn(phrase, AUTHORITATIVE_SOURCES)
        for field in (
            "Authoritative body and verified remit",
            "Document type",
            "Exact supported claim",
            "Explicitly cannot support",
            "Refresh or re-review trigger",
        ):
            self.assertIn(field, AUTHORITATIVE_SOURCE_TEMPLATE)

    def test_related_work_mechanisms_keep_duration_intensity_and_access_distinct(self):
        for dimension in (
            "Access state",
            "Changed parameter",
            "Progression variable",
            "Activation selector/gate",
            "Intention / goal anchor",
            "Configuration object and certainty",
            "Within-active ramp",
            "Duration",
            "Onset and cadence",
            "Cap and reset",
            "Scope",
            "Override and exceptions",
            "Selection/control",
            "Design provenance",
        ):
            self.assertIn(dimension, ACM_SIGCHI)
        self.assertIn("graduated **duration**", ACM_SIGCHI)
        self.assertIn("graduated **intensity**", ACM_SIGCHI)
        self.assertIn("intermittent access windows", ACM_SIGCHI)
        self.assertIn("post-budget ease-in", ACM_SIGCHI)
        self.assertIn("study-fixed threshold", ACM_SIGCHI)
        self.assertIn(
            "current-practice baseline → HCI adaptation → proposed project inheritance",
            ACM_SIGCHI,
        )
        self.assertIn("Design provenance / inherited baseline", ACM_AUDIT_TEMPLATE)
        self.assertIn(
            "Design-pattern provenance and inheritance",
            CURRENT_PRACTICE_TEMPLATE,
        )
        self.assertIn("reset", ACM_AUDIT_TEMPLATE)
        self.assertIn("still binary **access**", POSITIONING)
        self.assertIn("graduated **attenuation**", POSITIONING)
        self.assertIn("changed parameter", ACM_AUDIT_TEMPLATE)
        self.assertIn(
            "Intention/goal anchor; configuration object/certainty",
            ACM_AUDIT_TEMPLATE,
        )

    def test_daily_budget_and_target_bedtime_are_distinct_hypothesis_bearing_anchors(self):
        for text in (PHASE_ONE_INSTRUCTIONS, ACM_SIGCHI, POSITIONING):
            self.assertIn("daily", text.lower())
            self.assertIn("target-bedtime", text.lower())
            self.assertIn("hypothesis", text.lower())
        self.assertIn("cumulative budget versus clock/event transition", OUTLINE_TEMPLATE)
        self.assertIn("configuration burden", SKILL)

    def test_sigchi_priority_does_not_upgrade_evidence_strength(self):
        self.assertIn("coverage and situating gate", ACM_SIGCHI)
        self.assertIn("does **not** automatically assign `T1`", EVIDENCE)
        self.assertIn("Venue priority is a coverage heuristic", ACM_AUDIT_TEMPLATE)
        self.assertIn("implemented and evaluated", ACM_SIGCHI)
        self.assertIn("proposed-not-implemented", ACM_SIGCHI)

    def test_related_work_must_situate_broader_hci_relevance(self):
        for phrase in (
            "Community conversation",
            "Unresolved tension",
            "Project leverage",
            "Transfer boundary",
        ):
            self.assertIn(phrase, ACM_SIGCHI)
            self.assertIn(phrase, ACM_AUDIT_TEMPLATE)
        self.assertIn("Situate the work in the HCI community", POSITIONING)

    def test_independent_entry_is_explicit(self):
        self.assertIn("Every phase is independently enterable", SKILL)
        self.assertIn("Never require an Office Hours brief", SKILL)
        self.assertIn("Every HCI-stack phase must be useful without artifacts", PIPELINE)

    def test_office_hours_remains_standalone(self):
        self.assertIn("remains a complete standalone experience", SKILL)
        self.assertIn("Do not weaken Office Hours to eliminate overlap", PIPELINE)

    def test_phase_one_outputs_outline_not_final_prose(self):
        self.assertIn("research-framing-outline.md", SKILL)
        self.assertIn("Do not turn it into polished", SKILL)
        self.assertIn("final Abstract, Introduction, Related Work, or paper prose", SKILL)

    def test_phase_one_is_active_collaboration_not_batch_document_generation(self):
        flattened_skill = " ".join(SKILL.split())
        self.assertLessEqual(len(SKILL.splitlines()), 500)
        self.assertIn(
            "[phase-1-research-workflow.md]"
            "(references/phase-1-research-workflow.md)",
            SKILL,
        )
        detailed_gate = (
            "Before executing Steps 1–13, read "
            "[phase-1-research-workflow.md]"
            "(references/phase-1-research-workflow.md) completely."
        )
        self.assertIn(detailed_gate, flattened_skill)
        self.assertLess(
            flattened_skill.index(detailed_gate),
            flattened_skill.index("## Core workflow"),
        )
        self.assertIn(
            "Read this reference completely before executing the Phase 1 workflow.",
            DETAILED_WORKFLOW,
        )
        self.assertIn("## Contents", DETAILED_WORKFLOW)
        for phrase in (
            "[active-author-collaboration.md]",
            "phase-1-collaboration-workboard.md",
            "inspect → research → assess → challenge → compare → recommend",
            "constructive opposition",
            "author preference may choose among defensible paths",
            "AUTHOR-DECLINED-EVIDENCE",
            "one consequential question at a time",
            "Batch two to six tightly related, low-risk factual clarifications",
            "Ask one question at a time only for consequential choices",
            "decision-first current-state snapshot",
            "History and artifact inventories are supporting evidence",
        ):
            self.assertIn(phrase, flattened_skill)
        for phrase in (
            "Live Phase 1 coverage and workboard",
            "highest-consequence Phase 1 uncertainty",
            "Apply constructive opposition",
            "precise population, activity, construct, method, mechanism",
            "better-supported framing or approach",
            "AUTHOR-DECLINED-EVIDENCE",
            "Fast factual clarification batches",
            "Do not turn reconstruction",
            "Current state — read this first",
            "No author decision is currently ready",
        ):
            self.assertIn(phrase, AUTHOR_COLLABORATION)
        for phrase in (
            "Current state — read this first",
            "Direction and readiness",
            "Established now",
            "Settled decisions and claim boundaries",
            "Decisions needed now (maximum three)",
            "Decision-support evidence and populated artifacts",
            "Current round",
            "Phase coverage",
            "Consequential decision queue",
            "Decision-relevant research queue",
            "Constructive-opposition log",
            "One current author question",
            "Propagation / reopen trigger",
            "AUTHOR-DECLINED-EVIDENCE",
        ):
            self.assertIn(phrase, PHASE_1_WORKBOARD)
        self.assertIn(
            "Author preference may choose among defensible paths",
            ACTIVE_AUTHOR_COLLABORATION,
        )
        self.assertIn(
            "Decision-first current-state communication",
            ACTIVE_AUTHOR_COLLABORATION,
        )
        self.assertIn("Current state — read this first", DETAILED_WORKFLOW)
        self.assertIn("phase-1-collaboration-workboard.md", HTML_REPORTS)
        self.assertIn("Its first substantive section", HTML_REPORTS)
        for phrase in (
            "temporary loopback-only static server",
            "127.0.0.1",
            "A blocked `file:` URL is not a reason to omit visual",
            "explicit viewport capability",
            "stop the server immediately after inspection",
            "review server to `0.0.0.0`",
        ):
            self.assertIn(phrase, HTML_REPORTS)

    def test_phase_one_keeps_author_session_live_and_delegates_literature_work(self):
        openai_prompt = (
            ROOT / "agents" / "openai.yaml"
        ).read_text(encoding="utf-8")
        flattened_skill = " ".join(SKILL.split())
        flattened_workflow = " ".join(DETAILED_WORKFLOW.split())
        flattened_collaboration = " ".join(AUTHOR_COLLABORATION.split())

        for phrase in (
            "Keep the session interactive and parallelize evidence work",
            "Use available subagents by default",
            "sole writer, evidence integrator, workboard owner, and author-facing collaborator",
            "Do not shift routine literature search or analysis to the author",
        ):
            self.assertIn(phrase, flattened_skill)
        for phrase in (
            "Keep the session interactive and orchestrate parallel research",
            "methods/results/limitations audits",
            "read-only or non-writer boundary",
            "Treat a subagent report as analysis, not as a replacement for the underlying source",
        ):
            self.assertIn(phrase, flattened_workflow)
        for phrase in (
            "Interactive parallel-research protocol",
            "Use available subagents by default",
            "A set of updated files is not a substitute for this interaction",
            "Do not delegate routine literature search or analysis back to the author",
        ):
            self.assertIn(phrase, flattened_collaboration)
        for phrase in (
            "Parallel literature/research tasks, subagent owners, and status",
            "Last author-facing update and next update trigger",
            "Delegated task / owner / status / reconciliation",
            "Parallel/subagent findings reconciled",
        ):
            self.assertIn(phrase, PHASE_1_WORKBOARD)
        self.assertIn("keep this session interactive", openai_prompt)
        self.assertIn("use bounded subagents by default", openai_prompt)

    def test_unfinished_claim_states_are_required(self):
        for state in (
            "established-external",
            "inferred-external",
            "observed-project",
            "planned",
            "hypothesis",
            "aspiration",
            "unsupported",
        ):
            self.assertIn(f"`{state}`", SKILL)

    def test_html_reports_and_exemplar_routing_are_required(self):
        for report in (
            "phase-1-progress.html",
            "literature-and-evidence.html",
            "phase-1-final.html",
        ):
            self.assertIn(report, SKILL)
        self.assertIn("exemplar-routing.md", SKILL)
        self.assertIn(
            "corresponding section",
            (ROOT / "references" / "exemplar-routing.md")
            .read_text(encoding="utf-8")
            .lower(),
        )

    def test_consequence_severity_is_researched_before_author_choice(self):
        self.assertIn("consequence-severity-ranking.md", PHASE_ONE_INSTRUCTIONS)
        self.assertIn("consequence-severity-research.md", PHASE_ONE_INSTRUCTIONS)
        self.assertIn(
            "Do not ask the author to rank, select, or approve consequences",
            PHASE_ONE_INSTRUCTIONS,
        )
        self.assertIn("CONSEQUENCE_RANKING_COMPLETE", PHASE_ONE_INSTRUCTIONS)
        for dimension in (
            "magnitude",
            "coverage",
            "functional importance",
            "causal proximity",
            "duration and reversibility",
            "distribution",
            "evidence certainty",
        ):
            self.assertIn(dimension, CONSEQUENCE_RESEARCH)
        self.assertIn(
            "Do not collapse severity and evidence certainty into one score",
            CONSEQUENCE_RESEARCH,
        )
        self.assertIn("Ranking sensitivity", CONSEQUENCE_TEMPLATE)
        self.assertIn("Confidence in rank", CONSEQUENCE_TEMPLATE)
        self.assertIn(
            "do not ask the author to rank or choose consequences",
            CONSEQUENCE_TEMPLATE,
        )

    def test_evidence_strength_is_claim_specific_cached_and_vetoed(self):
        self.assertIn("evidence-strength-register.md", SKILL)
        for tag in ("FULL", "PARTIAL", "BROKEN", "ES3", "ES2", "ES1", "ES0"):
            self.assertIn(tag, EVIDENCE)
            self.assertIn(tag, EVIDENCE_STRENGTH_TEMPLATE)
        self.assertIn("Critical-risk-of-bias veto", EVIDENCE_STRENGTH_TEMPLATE)
        self.assertIn("Design labels", EVIDENCE_STRENGTH_TEMPLATE)
        self.assertIn("NotebookLM ratings never override the veto", EVIDENCE)
        self.assertIn("Unmarked sources are `UNASSESSED`", EVIDENCE_STRENGTH_TEMPLATE)
        self.assertIn("Re-review", EVIDENCE_STRENGTH_TEMPLATE)

    def test_evidence_labels_are_independent_and_disambiguated(self):
        for axis in (
            "source tier",
            "ingestion completeness",
            "claim directness",
            "claim-specific evidence strength",
        ):
            self.assertIn(axis, EVIDENCE)
        self.assertIn("[T2A | FULL | Adjacent | ES1]", EVIDENCE)
        self.assertIn("Tier 1 — capability", EVIDENCE)
        self.assertIn("it does not rate evidence", EVIDENCE)

    def test_hypothesis_and_unsupported_claims_run_through_research_loop(self):
        self.assertIn("motivation-claim-strengthening.md", SKILL)
        self.assertIn("motivation-claim-research-queue.md", SKILL)
        self.assertIn("current-practice-audit.md", SKILL)
        self.assertIn("MOTIVATION_CLAIM_AUDIT_COMPLETE", SKILL)
        for route in (
            "A — external research",
            "B — official practice audit",
            "C — author/project evidence",
            "D — future system evaluation",
            "E — retire or supersede",
        ):
            self.assertIn(route, MOTIVATION_STRENGTHENING)
            self.assertIn(route, MOTIVATION_QUEUE_TEMPLATE)
        self.assertIn("every active claim-ledger row", MOTIVATION_STRENGTHENING)
        self.assertIn("do not pretend external adjacency validates", MOTIVATION_STRENGTHENING)
        self.assertIn("Contradictory", CURRENT_PRACTICE_TEMPLATE)
        self.assertIn("Unsupported failure or abandonment claims", CURRENT_PRACTICE_TEMPLATE)

    def test_missing_full_sources_trigger_concrete_author_access_help(self):
        missing_template = (
            ROOT / "assets" / "missing-full-copies.md"
        ).read_text(encoding="utf-8")
        flattened_instructions = " ".join(PHASE_ONE_INSTRUCTIONS.split())
        for phrase in (
            "NEEDS_AUTHOR_SOURCE_ACCESS",
            "Do not merely log an inaccessible decision-relevant source",
            "not a framing-choice gate",
            "complete the CAPTCHA",
            "university IP or university VPN",
            "Never ask for passwords, cookies, session tokens",
        ):
            self.assertIn(phrase, flattened_instructions)
        self.assertIn("Do not stop at writing `missing-full-copies.md`", AUTHOR_COLLABORATION)
        self.assertIn("university IP/library access or a university VPN", AUTHOR_COLLABORATION)
        self.assertIn("A CAPTCHA must be completed by the author", AUTHOR_COLLABORATION)
        self.assertIn("Request surfaced date", missing_template)
        self.assertIn("Conversation/workboard locator", missing_template)
        self.assertIn("Fallback if unavailable", CONSEQUENCE_TEMPLATE)
        self.assertIn("NEEDS_AUTHOR_SOURCE_ACCESS", CONSEQUENCE_RESEARCH)

    def test_unassessed_sources_cannot_be_terminal_or_phase_ready(self):
        for text in (
            SKILL,
            DETAILED_WORKFLOW,
            EVIDENCE,
            AUTHOR_COLLABORATION,
            NOTEBOOKLM,
        ):
            self.assertIn("source-resolution.csv", text)
        self.assertIn(
            "UNASSESSED` is a transient acquisition state",
            SKILL,
        )
        self.assertIn(
            "Never call a bounded audit or research round complete",
            AUTHOR_COLLABORATION,
        )
        self.assertIn("FULL_TEXT_OBTAINED", EVIDENCE)
        self.assertIn("successful metadata import does not", NOTEBOOKLM)
        self.assertIn("check_source_resolution.py", SKILL)
        self.assertIn("--end-of-round", SKILL)
        self.assertIn("--phase-ready", SKILL)
        for column in (
            "source_id",
            "citation_key",
            "bibliographic_identity",
            "source_provenance",
            "candidate_role",
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
        ):
            self.assertIn(column, SOURCE_RESOLUTION_TEMPLATE)
        self.assertIn("Source-resolution state", SOURCE_MANIFEST_TEMPLATE)
        self.assertIn("Author-access request", SOURCE_MANIFEST_TEMPLATE)
        self.assertIn(
            "Separate multiple affected claim IDs with `||`",
            MISSING_FULL_COPIES_TEMPLATE,
        )
        self.assertIn("claim-evidence-ledger.csv", MISSING_FULL_COPIES_TEMPLATE)
        self.assertIn("session:pending", MISSING_FULL_COPIES_TEMPLATE)
        self.assertIn(
            "declared bounded audit or research-round closure",
            (ROOT / "scripts" / "check_source_resolution.py").read_text(
                encoding="utf-8"
            ),
        )
        for phrase in (
            "every external HTTP(S) key",
            "actual surfaced date/locator",
            "different retained `FULL_TEXT_ASSESSED` row",
        ):
            self.assertIn(phrase, " ".join(SKILL.split()))

    def test_notebooklm_is_reconciled_as_a_human_facing_working_set(self):
        for phrase in (
            "Keep the notebook human-readable",
            "START HERE",
            "verify that each object contains the intended work",
            "replace broken imports",
            "notebooklm-maintenance.md",
            "explicit confirmation",
            "exact source-ID deletion set",
        ):
            self.assertIn(phrase, NOTEBOOKLM)
        for phrase in (
            "Human-facing working set",
            "Irreversible cleanup candidates",
            "Every new source contains the intended paper",
            "author explicitly confirmed",
        ):
            self.assertIn(phrase, NOTEBOOKLM_MAINTENANCE)
        self.assertIn("Keep the notebook human-readable", SKILL)
        self.assertIn("notebooklm-maintenance.md", DETAILED_WORKFLOW)

    def test_agent_context_rehydrates_phase_one_in_codex_and_claude(self):
        for text in (SKILL, DETAILED_WORKFLOW, NOTEBOOKLM):
            self.assertIn("agent-context.json", text)
            self.assertIn("$gpt-pro", text)
            self.assertIn("/gpt-pro", text)
        self.assertEqual(AGENT_CONTEXT["schema_version"], 1)
        self.assertEqual(AGENT_CONTEXT["project"]["repository_root"], ".")
        self.assertEqual(
            AGENT_CONTEXT["phase"],
            {
                "name": "Phase 1",
                "skill": "hci-motivation-and-contributions",
                "status": "active",
            },
        )
        self.assertEqual(
            AGENT_CONTEXT["context"]["always_include"],
            [
                "research-framing/phase-1-collaboration-workboard.md",
                "research-framing/author-decisions.md",
                "research-framing/starting-state.md",
            ],
        )
        self.assertEqual(
            AGENT_CONTEXT["context"]["repo_read_allow"],
            ["research-framing/**"],
        )
        self.assertEqual(
            AGENT_CONTEXT["notebooklm"]["source_manifest"],
            "research-framing/source-manifest.md",
        )
        self.assertEqual(
            AGENT_CONTEXT["notebooklm"]["maintenance"],
            "research-framing/notebooklm-maintenance.md",
        )
        self.assertIn("same work round", NOTEBOOKLM)
        self.assertIn("phase.status` to `complete", DETAILED_WORKFLOW)
        self.assertNotIn("/", AGENT_CONTEXT["notebooklm"]["profile"])

    def test_html_reports_require_citation_catalog_and_post_render_audit(self):
        reports_contract = (
            ROOT / "references" / "html-reports.md"
        ).read_text(encoding="utf-8")
        self.assertIn("references.csv", SKILL)
        self.assertIn("audit_phase1_reports.py", SKILL)
        self.assertIn("references.csv", reports_contract)
        self.assertIn("headed browser", reports_contract)
        self.assertIn("escaped pipes", reports_contract)
        self.assertIn("Author (Year Venue): Short Title", reports_contract)
        self.assertIn("source-resolution.html", reports_contract)
        for phrase in (
            "[@CitationKey]",
            "unknown key",
            "alias can resolve to more than one work",
            "full authors, full title, and full",
            "repository-wide contract test",
        ):
            self.assertIn(phrase, CITATION_INTEGRITY)

    def test_workspace_creation_requires_readme_and_initial_audited_reports(self):
        for text in (SKILL, DETAILED_WORKFLOW):
            self.assertIn("initialize_phase1_workspace.py", text)
            self.assertIn("README.md", text)
            self.assertIn("before every", text.lower())
            self.assertIn("push", text.lower())
        for report in (
            "phase-1-progress.html",
            "literature-and-evidence.html",
            "phase-1-final.html",
            "artifact-index.html",
        ):
            self.assertIn(report, PROJECT_README)
            self.assertIn(report, HTML_REPORTS)
        self.assertIn("render_phase1_reports.py", WORKSPACE_INITIALIZER)
        self.assertIn("audit_phase1_reports.py", WORKSPACE_INITIALIZER)

    def test_project_artifacts_never_fall_back_to_the_skill_repository(self):
        self.assertIn("[repository-boundaries.md]", SKILL)
        for phrase in (
            "commit the skill and shared-contract changes",
            "push the commit",
            "synchronize every existing local installation",
            "remove stale files",
            "verify recursive equality",
            "Never finish a skill-update task",
            "continue only read-only inspection, research, and interactive planning",
            "Do not create",
            "an arbitrary workspace",
        ):
            self.assertIn(phrase, REPOSITORY_BOUNDARIES)

    def test_private_project_stores_do_not_screen_sources_by_copyright(self):
        for text in (SKILL, REPOSITORY_BOUNDARIES, NOTEBOOKLM, DETAILED_WORKFLOW):
            normalized = text.lower()
            self.assertIn("private", normalized)
            self.assertIn("copyright", normalized)
            self.assertIn("version control", normalized)
            self.assertIn("notebooklm", normalized)
            self.assertIn("per-source author confirmation", normalized)

        for phrase in (
            "research-framing/sources/full-text/",
            "canonical repository copy",
            "repository-relative path",
            "NotebookLM source ID",
        ):
            self.assertIn(phrase, PHASE_ONE_INSTRUCTIONS)

        self.assertIn("Canonical repository location", SOURCE_MANIFEST_TEMPLATE)
        self.assertIn(
            "both a canonical repository copy and a verified NotebookLM source ID",
            SOURCE_MANIFEST_TEMPLATE,
        )
        self.assertNotIn(
            "Copyrighted PDFs are excluded from version control",
            SOURCE_MANIFEST_TEMPLATE,
        )
        self.assertNotIn("never commit it by default", NOTEBOOKLM)
        self.assertNotIn("whose license/terms prohibit the upload", NOTEBOOKLM)

    def test_closest_work_positioning_compares_interaction_not_maturity(self):
        self.assertIn("[related-work-positioning.md]", SKILL)
        self.assertIn("Trace the full information flow", POSITIONING)
        self.assertIn("one data stream *about* each person", POSITIONING)
        self.assertIn("one decisive contribution-level contrast", POSITIONING)
        self.assertIn("Do not substitute a limitation inventory", POSITIONING)

    def test_contribution_strength_ladder_is_ordered_and_complete(self):
        self.assertIn("ordered contribution-strength ladder", POSITIONING)
        self.assertIn("**capability:**", POSITIONING)
        self.assertIn("**experience or outcome:**", POSITIONING)
        self.assertIn("**cost or access:**", POSITIONING)
        self.assertIn("comparison proximity", POSITIONING)
        self.assertIn("related-work-contribution-tier-audit.md", SKILL)
        self.assertIn("label them `N/A`", POSITIONING)

    def test_related_work_requires_classification_and_conjunctive_comparison(self):
        flattened = " ".join(POSITIONING.split())
        self.assertIn("causal interaction approach", SKILL)
        self.assertIn("relationship-classification gate", POSITIONING)
        self.assertIn("conjunctive claim test", POSITIONING)
        self.assertIn("Treat under-description as unresolved by default", POSITIONING)
        self.assertIn("Apply six-field prior-work evidence accounting", POSITIONING)
        self.assertIn("Capability collision", flattened)
        self.assertIn("Contribution attribution", flattened)

    def test_ranked_related_work_requires_full_working_positioning_paragraphs(self):
        for text in (SKILL, POSITIONING, RANKED_POSITIONING_TEMPLATE):
            self.assertIn("ranked-related-work-positioning.md", text)
            self.assertIn("approximately ten", text)
        for requirement in (
            "target people",
            "causal interaction",
            "literal operational difference",
            "what the project inherits",
            "replication",
            "extension",
            "contrast",
            "instantiation",
            "test",
        ):
            self.assertIn(requirement, POSITIONING)
        self.assertIn("one full working paragraph per ranked work", POSITIONING)
        self.assertIn("not final manuscript prose", POSITIONING)

    def test_related_work_ranking_is_problem_first_and_keeps_distant_collisions_separate(self):
        for text in (
            SKILL,
            DETAILED_WORKFLOW,
            POSITIONING,
            RANKED_POSITIONING_TEMPLATE,
            AUDIT_TEMPLATE,
            SEARCH_RECALL_TEMPLATE,
            ACM_AUDIT_TEMPLATE,
            OUTLINE_TEMPLATE,
            PHASE_2_HANDOFF,
        ):
            self.assertIn("target-problem identity", text.lower())

        for band in (
            "SAME-SPECIFIC-PROBLEM",
            "SIMILAR-PROBLEM",
            "ADJACENT-PROBLEM",
            "DIFFERENT-PROBLEM",
        ):
            self.assertIn(band, POSITIONING)
            self.assertIn(band, RANKED_POSITIONING_TEMPLATE)

        for phrase in (
            "Primary problem-space portfolio",
            "Mechanism/capability-collision portfolio",
            "Concept, theory, and foundation inventory",
            "Same-domain vocabulary",
            "claim-specific collision",
            "cannot displace",
            "do not pad",
            "lexicographically",
            "Do not use an unvalidated mechanism hypothesis",
        ):
            self.assertIn(phrase.lower(), POSITIONING.lower())

        self.assertLess(
            POSITIONING.index("assign a problem-proximity band"),
            POSITIONING.index("mandatory **relationship-classification gate**"),
        )
        self.assertIn("Same/similar-problem saturation", SEARCH_RECALL_TEMPLATE)
        self.assertIn(
            "Same/similar-problem results were searched to their own stopping criterion",
            ACM_AUDIT_TEMPLATE,
        )
        self.assertIn(
            "Hypothesized mechanism(s), kept outside the problem identity",
            RANKED_POSITIONING_TEMPLATE,
        )
        self.assertIn(
            "chart proximity has not been substituted",
            QUADRANT.lower(),
        )
        self.assertIn(
            "NotebookLM's semantic similarity",
            NOTEBOOKLM,
        )
        self.assertIn(
            "different-problem mechanism collisions",
            PHASE_ONE_INSTRUCTIONS.lower(),
        )

    def test_related_work_calibrates_capability_and_value_novelty_separately(self):
        for phrase in (
            "Calibrate novelty assertiveness",
            "novelty-bearing causal core",
            "supporting implementation",
            "realization evidence",
            "value evidence",
            "semantic control signals",
            "idea-provenance-ledger.csv",
            "strongest attributed claimed-and-demonstrated contribution statement now",
        ):
            self.assertIn(phrase, POSITIONING)
        for phrase in (
            "What is actually different",
            "Novelty-bearing causal core versus supporting implementation",
            "Ranked novelty hypotheses",
            "Strongest safe claim now",
        ):
            self.assertIn(phrase, RANKED_POSITIONING_TEMPLATE)
        self.assertIn(
            "Do not conflate untested human value with absence of capability novelty",
            SKILL,
        )

    def test_contribution_discovery_covers_objectives_states_identification_and_nulls(self):
        for phrase in (
            "Intervention-objective and equal-quantity gate",
            "Concept-lineage versus in-domain-collision gate",
            "Collision–delta and control-policy anatomy gate",
            "Residual-state topology gate",
            "Anchor semantics versus anchor quality gate",
            "Temporal-role and identifiability gate",
            "Construct-independence and composite-measure veto",
            "Causal-ladder and fidelity gate",
            "Null-survival gate",
            "engineered setting → delivered operational exposure",
            "Prefer a multidimensional profile over a scalar",
            "Retire novelty only at the overlapping level",
        ):
            self.assertIn(phrase, POSITIONING)
        self.assertIn("general concept lineage", RUBRIC)
        self.assertIn("in-domain HCI translation", RUBRIC)
        self.assertIn("concept lineage/in-domain collision", SKILL)
        self.assertIn(
            "meaningful human action, state, control relationship, or information relationship",
            RUBRIC,
        )
        self.assertIn("treatment assignment", RUBRIC)
        self.assertIn("null, worse, heterogeneous", RUBRIC)
        for template in (
            RANKED_POSITIONING_TEMPLATE,
            AUDIT_TEMPLATE,
            OUTLINE_TEMPLATE,
            PHASE_2_HANDOFF,
        ):
            for phrase in (
                "equal-quantity",
                "concept lineage",
                "residual-state",
                "Anchor semantics",
                "Temporal",
                "Causal",
                "Null-surviving",
            ):
                self.assertIn(phrase, template)
        self.assertIn("Reject treatment-coded composites", RANKED_POSITIONING_TEMPLATE)

    def test_loaded_control_policy_terms_do_not_upgrade_evidence(self):
        for term in (
            "intention-anchored",
            "intention-aligned",
            "anticipatory",
            "attenuated access",
            "operational exposure",
            "stimulation",
            "reduced impact",
        ):
            self.assertIn(term, TERMINOLOGY)
        self.assertIn("Prefer `intention-anchored` before validation", TERMINOLOGY)
        self.assertIn("Reduced harm", TERMINOLOGY)

    def test_local_candidate_source_files_must_be_reconciled_before_closure(self):
        for text in (SKILL, DETAILED_WORKFLOW):
            self.assertIn("LOCAL_SOURCE_FILES_RECONCILED", text)
            self.assertIn("source-resolution.csv", text)
        for phrase in (
            "Candidate source/import roots inventoried",
            "Files reconciled by bibliographic identity",
            "Unresolved files and consequence",
            "LOCAL_SOURCE_FILES_NOT_RECONCILED",
        ):
            self.assertIn(phrase, SOURCE_MANIFEST_TEMPLATE)

    def test_reader_facing_artifact_shelf_keeps_markdown_as_source(self):
        self.assertIn("artifact-index.html", SKILL)
        self.assertIn("artifact-index.html", HTML_REPORTS)
        self.assertIn("authoritative, editable, diffable research record", HTML_REPORTS)
        for source in (
            "phase-1-collaboration-workboard.md",
            "ranked-related-work-positioning.md",
            "acm-sigchi-related-work-audit.md",
            "related-work-search-recall-audit.md",
            "prior-work-contribution-boundary.md",
            "prior-work-evidence-accounting.csv",
            "idea-provenance-ledger.csv",
            "imported-bibliography-accountability.csv",
            "late-found-work-postmortem.csv",
            "novelty-regression-sentinels.yaml",
            "evidence-strength-register.md",
            "authoritative-source-map.md",
            "current-practice-audit.md",
            "source-manifest.md",
            "source-resolution.csv",
            "missing-full-copies.md",
        ):
            self.assertIn(source, HTML_REPORTS)
        self.assertIn("visible missing-source page", HTML_REPORTS)

    def test_prior_work_boundary_uses_six_independent_fields(self):
        fields = (
            "AUTHOR CLAIM",
            "DEMONSTRATED ARTIFACT OR STUDY",
            "OPERATED CAPABILITY",
            "EVALUATED RESULT",
            "CAPABILITY COLLISION",
            "CONTRIBUTION CREDIT",
        )
        for text in (SKILL, POSITIONING, EVIDENCE, BOUNDARY_TEMPLATE):
            for field in fields:
                self.assertIn(field, text)
            self.assertIn("independent", text.lower())
        for artifact in (
            "prior-work-evidence-accounting.csv",
            "idea-provenance-ledger.csv",
            "imported-bibliography-accountability.csv",
            "late-found-work-postmortem.csv",
            "novelty-regression-sentinels.yaml",
        ):
            self.assertIn(artifact, SKILL)
        for column in (
            "author_claim_status",
            "demonstration_status",
            "operated_capability_status",
            "evaluated_result_status",
            "capability_collision",
            "contribution_credit",
            "attribution_status",
            "classification_scope",
            "port_credit_gate",
            "source_silence_disposition",
        ):
            self.assertIn(column, ACCOUNTING_TEMPLATE)
        self.assertIn("DEMONSTRATED_UNCLAIMED", PRIOR_WORK_BOUNDARIES)
        self.assertIn("CLAIMED_UNDEMONSTRATED", PRIOR_WORK_BOUNDARIES)

    def test_capability_boundary_requires_positive_artifact_evidence(self):
        for text in (POSITIONING, EVIDENCE, BOUNDARY_TEMPLATE, PRIOR_WORK_BOUNDARIES):
            self.assertIn("positive evidence", text.lower())
            self.assertIn("silence", text.lower())
        self.assertIn("smallest named operation", PRIOR_WORK_BOUNDARIES)
        self.assertIn("OPERATED CAPABILITY=UNRESOLVED", PRIOR_WORK_BOUNDARIES)
        self.assertIn("SEARCH_PRIORITY", PRIOR_WORK_BOUNDARIES)
        self.assertIn("REOPEN_QUERY", PRIOR_WORK_BOUNDARIES)

    def test_unclaimed_operation_and_claimed_undemonstrated_are_separate(self):
        for text in (SKILL, POSITIONING, EVIDENCE, BOUNDARY_TEMPLATE):
            normalized = text.lower().replace("_", "-")
            self.assertIn("demonstrated-unclaimed", normalized)
            self.assertIn("claimed-undemonstrated", normalized)
        self.assertIn("can create a capability collision", SKILL)
        self.assertIn("contribution credit `NONE`", POSITIONING)
        self.assertIn(
            "explicit author claim that a realized capability exists without matched evidence remains visible",
            " ".join(SKILL.lower().split()),
        )
        self.assertIn("not hidden only in this ledger", PRIOR_WORK_BOUNDARIES)

    def test_future_work_is_idea_provenance_not_collision_or_credit(self):
        for text in (SKILL, POSITIONING, ACM_SIGCHI, BOUNDARY_TEMPLATE):
            flattened = " ".join(text.lower().split())
            self.assertIn("idea provenance", flattened)
            self.assertIn("collision", flattened)
            self.assertIn("credit", flattened)
        self.assertIn("capability_collision", IDEA_PROVENANCE_TEMPLATE)
        self.assertIn("contribution_credit", IDEA_PROVENANCE_TEMPLATE)
        self.assertNotIn("contribution-salience", POSITIONING.lower())
        self.assertNotIn("contribution-salience", EVIDENCE.lower())

    def test_quadrants_cannot_bypass_atomic_prior_work_accounting(self):
        for phrase in (
            "prior-work-evidence-accounting.csv",
            "DEMONSTRATED_UNCLAIMED",
            "CLAIMED_UNDEMONSTRATED",
            "spoken \"next\" → advance-one-slide command",
            "task-performance score → badge",
            "CAPABILITY COLLISION=NONE",
            "CONTRIBUTION CREDIT=NONE",
        ):
            self.assertIn(phrase, QUADRANT)
        self.assertIn(
            "Keep capability collision separate from contribution attribution",
            QUADRANT,
        )
        self.assertIn(
            "a port alone receives no contribution credit",
            " ".join(QUADRANT.lower().split()),
        )

    def test_port_credit_requires_demonstrated_adaptation_or_finding(self):
        self.assertIn("zero-credit port", POSITIONING.lower())
        self.assertIn("nontrivial reusable adaptation", POSITIONING)
        self.assertIn("new class of use", POSITIONING)
        self.assertIn("directly validated empirical finding", POSITIONING)
        self.assertIn("PORT_ONLY", PRIOR_WORK_CHECKER)

    def test_exclusion_first_accounting_has_fail_closed_completion_markers(self):
        for marker in (
            "IMPORTED_BIBLIOGRAPHY_ACCOUNTED",
            "CLAIM_DEMONSTRATION_OPERATION_EVALUATION_DECOMPOSED",
            "CAPABILITY_COLLISION_AND_CREDIT_SEPARATED",
            "DEMONSTRATED_UNCLAIMED_OPERATIONS_REVIEWED",
            "MIXED_CHANNELS_DECOMPOSED",
            "PORT_CREDIT_GATES_APPLIED",
            "NO_PROPOSAL_GRANTED_CAPABILITY_CREDIT",
            "NO_SILENCE_DERIVED_CAPABILITY_OR_ABSENCE",
            "LATE_FOUND_WORK_REPAIR_COMPLETE",
            "NOVELTY_REGRESSION_SENTINELS_RECHECKED",
            "ZERO_YIELD_PROMOTION_WAVE_COMPLETE",
        ):
            self.assertIn(marker, BOUNDARY_TEMPLATE)
            self.assertIn(marker, PRIOR_WORK_CHECKER)
        self.assertIn("check_prior_work_accounting.py", SKILL)
        self.assertIn("--phase-ready", SKILL)

    def test_mixed_channels_and_smallest_operated_unit_are_explicit(self):
        for phrase in (
            "spoken \"next\" → advance-one-slide command",
            "establish backward navigation",
            "task-performance score → badge",
            "computed-state-to-reward",
            "three channels",
            "whole-system label",
        ):
            self.assertIn(phrase, PRIOR_WORK_BOUNDARIES)
        for column in (
            "smallest_operated_unit",
            "channel_id",
            "input_or_signal",
            "mapped_command_or_effect",
            "generalization_boundary",
            "required_channel_set",
            "qualified_channel_set",
        ):
            self.assertIn(column, ACCOUNTING_TEMPLATE)

    def test_imported_and_late_work_have_separate_accountability_artifacts(self):
        for column in (
            "supplied_artifact",
            "source_resolution_id",
            "terminal_disposition",
            "upgrade_search",
            "stronger_or_counter_source",
        ):
            self.assertIn(column, IMPORTED_ACCOUNTABILITY_TEMPLATE)
        for column in (
            "route_that_should_have_found_it",
            "sibling_records_screened",
            "query_or_graph_repair",
            "affected_claim_rerun",
            "regression_sentinel_id",
        ):
            self.assertIn(column, LATE_FOUND_TEMPLATE)
        self.assertIn('"schema_version": 1', NOVELTY_SENTINEL_TEMPLATE)
        self.assertIn('"sentinels": []', NOVELTY_SENTINEL_TEMPLATE)

    def test_conjunctive_comparison_is_symmetric_and_terms_require_evidence(self):
        flattened = " ".join(POSITIONING.split())
        self.assertIn("symmetrically to the proposed project", POSITIONING)
        self.assertIn("claimed in an author draft", POSITIONING)
        self.assertIn("record only `AUTHOR CLAIM`", POSITIONING)
        self.assertIn("The claim cannot be stronger than its weakest necessary qualifier", POSITIONING)
        self.assertIn("“Independently addressed” requires routing evidence", flattened)
        self.assertIn("“private” requires an access or audibility rule", flattened)
        self.assertIn("“simultaneous” or “concurrent”", flattened)
        self.assertIn("during the same unfolding activity", POSITIONING)

    def test_activity_is_separated_from_implementation(self):
        self.assertIn("activity-versus-implementation counterfactual", RELATED_WORK_CONTRACT)
        self.assertIn(
            "If both systems used the same hardware, interface, and output modality",
            POSITIONING,
        )
        self.assertIn("only as hardware or medium", POSITIONING)
        self.assertIn("not independent novelty", AUDIT_TEMPLATE)
        self.assertIn("Activity-versus-implementation counterfactual", AUDIT_TEMPLATE)
        self.assertIn("physical versus virtual", RUBRIC)
        self.assertIn("not merely the rendering environment", QUADRANT)

    def test_existing_workflow_and_fair_comparator_are_required(self):
        self.assertIn("existing human workflow", POSITIONING)
        self.assertIn(
            "replaces, complements, extends, or bridges",
            " ".join(POSITIONING.split()),
        )
        self.assertIn("same workflow plus the proposed layer", SKILL)
        self.assertIn("Existing-workflow and communication map", AUDIT_TEMPLATE)
        self.assertIn("Existing-workflow map", OUTLINE_TEMPLATE)
        self.assertIn("Fair future comparator", OUTLINE_TEMPLATE)
        self.assertIn("workflow relationship or significance", DECISION_PACKET)
        self.assertIn("fair future comparator", DECISION_PACKET)
        self.assertIn("Existing workflow before, during, and after", PHASE_2_HANDOFF)
        self.assertIn("Fair future comparator", PHASE_2_HANDOFF)

    def test_current_human_practice_is_checked_before_claiming_a_new_stage(self):
        self.assertIn("current-practice collision check", RELATED_WORK_CONTRACT)
        self.assertIn(
            "“No prior system supports this” does not mean “no current practice supports this.”",
            POSITIONING,
        )
        self.assertIn("speech, gesture", POSITIONING)
        self.assertIn("Current-practice collision check", AUDIT_TEMPLATE)
        self.assertIn("Current-practice collision check", OUTLINE_TEMPLATE)
        self.assertIn("Current-practice collision result", PHASE_2_HANDOFF)

    def test_communication_structure_is_compared_explicitly(self):
        self.assertIn("communication and information-distribution structure", POSITIONING)
        self.assertIn("sender → author or selector → intended and actual recipients", POSITIONING)
        self.assertIn("same or different content", POSITIONING)
        self.assertIn("concurrent or serialized delivery", POSITIONING)
        self.assertIn("Communication structure", AUDIT_TEMPLATE)
        self.assertIn("Existing communication structure", OUTLINE_TEMPLATE)
        self.assertIn("Existing communication structure", PHASE_2_HANDOFF)

    def test_contribution_layers_are_separated_then_ranked(self):
        self.assertIn(
            "Separate these layers, then rank them—do not impose a universal order",
            PHASE_ONE_INSTRUCTIONS,
        )
        self.assertIn(
            "strongest defensible consequential difference",
            PHASE_ONE_INSTRUCTIONS,
        )
        self.assertIn(
            "workflow relationship may explain\nsignificance while an interaction",
            PHASE_ONE_INSTRUCTIONS,
        )
        self.assertIn("Primary contribution layer and ranking rationale", AUDIT_TEMPLATE)
        self.assertIn("Primary contribution layer and ranking rationale", OUTLINE_TEMPLATE)
        self.assertIn("then rank them; do not assume", DECISION_PACKET)
        self.assertIn("a universal order", DECISION_PACKET)

    def test_differentiation_and_adaptation_terms_are_not_conflated(self):
        for term in (
            "shared or group-wide",
            "player-specific or recipient-specific",
            "recipient-differentiated",
            "role- or profile-configured",
            "personalizable or user-adjustable",
            "system-personalized",
            "**adaptive:**",
        ):
            self.assertIn(term, POSITIONING)
        self.assertIn("Do not use it as a catch-all", POSITIONING)
        self.assertIn("Personalized", POSITIONING)
        self.assertIn("Content differentiation", QUADRANT)
        self.assertIn("delivery concurrency", QUADRANT)
        self.assertIn("adaptation provenance", QUADRANT)
        self.assertIn(
            "Do not conflate recipient differentiation with automatic personalization",
            QUADRANT,
        )
        self.assertIn("Distinguish recipient scope from selection provenance", AUTHOR_COLLABORATION)

    def test_terminology_is_a_semantic_contract_before_a_lexical_spine(self):
        self.assertIn("Treat terminology as claim discipline", SKILL)
        self.assertIn("terminology-contract.md", SKILL)
        self.assertIn("semantic contract", TERMINOLOGY.lower())
        self.assertIn("lexical spine", TERMINOLOGY.lower())
        self.assertIn("approve the semantic contract", SKILL)
        self.assertIn("semantic contract before selecting the lexical spine", AUTHOR_COLLABORATION)

    def test_terminology_contract_decomposes_loaded_claims(self):
        for dimension in (
            "Addressee",
            "Content relationship",
            "Selection provenance",
            "Tailoring basis",
            "User control",
            "Adaptation",
            "Timing",
            "Access",
            "Outcome",
        ):
            self.assertIn(dimension, TERMINOLOGY)
        for term in (
            "player-specific",
            "recipient-differentiated",
            "individualized delivery",
            "individualized",
            "personalizable",
            "personalized",
            "adaptive",
            "independently addressed",
            "recipient-exclusive",
            "concurrent",
            "real-time",
        ):
            self.assertIn(term, TERMINOLOGY.lower())

    def test_terminology_options_author_choice_and_propagation_are_required(self):
        self.assertIn("three to five coherent systems", TERMINOLOGY)
        self.assertIn("Reserved terms", TERMINOLOGY_TEMPLATE)
        self.assertIn("likely reader inference", TERMINOLOGY.lower())
        self.assertIn("Terminology contract", AUTHOR_DECISIONS)
        self.assertIn("Paper-facing lexical hierarchy", AUTHOR_DECISIONS)
        self.assertIn("Reserved and superseded terms", AUTHOR_DECISIONS)
        self.assertIn("future Abstract, Introduction, Related Work", TERMINOLOGY)
        self.assertIn("Terminology contract and lexical hierarchy", OUTLINE_TEMPLATE)
        self.assertIn("Terminology-contract status", PHASE_2_HANDOFF)

    def test_familiar_terms_lead_and_precise_constructs_follow(self):
        for document in (
            SKILL,
            TERMINOLOGY,
            AUTHOR_COLLABORATION,
            DETAILED_WORKFLOW,
        ):
            self.assertIn("familiar", document.lower())
            self.assertIn("first use", document.lower())
        self.assertIn("familiar-to-precise terminology rule", CLAIM_FOCUSED_WRITING)
        self.assertIn("reusable across domains", CLAIM_FOCUSED_WRITING)
        self.assertIn("exact source-matched scientific construct", CLAIM_FOCUSED_WRITING)
        self.assertIn("blue light", CLAIM_FOCUSED_WRITING)
        self.assertIn("short-wavelength", CLAIM_FOCUSED_WRITING)
        self.assertIn("melanopic", CLAIM_FOCUSED_WRITING)
        self.assertIn("Do not treat", CLAIM_FOCUSED_WRITING)
        self.assertIn("Precise construct or metric", TERMINOLOGY_TEMPLATE)
        self.assertIn("Approved later short form", TERMINOLOGY_TEMPLATE)
        self.assertIn("Precise construct or metric", AUTHOR_DECISIONS)
        self.assertIn("Approved later short form", AUTHOR_DECISIONS)

    def test_internal_evidence_completeness_is_separate_from_reader_facing_caveats(self):
        self.assertIn(
            "[claim-focused-writing.md](references/claim-focused-writing.md)",
            SKILL,
        )
        self.assertIn(
            "[claim-focused-writing.md](claim-focused-writing.md)",
            DETAILED_WORKFLOW,
        )
        for phrase in (
            "internal evidence record",
            "reader-facing narrative",
            "claim-local caveat test",
            "Do not append a disclaimer about an outcome the text does not claim",
            "whole-night sleep outcomes",
            "never permits hiding contrary evidence",
        ):
            self.assertIn(phrase, CLAIM_FOCUSED_WRITING)
        self.assertIn("Do not demand a redundant project study", EVIDENCE)
        self.assertIn("unclaimed distal outcome", EVIDENCE)
        self.assertIn("Separate review cautions from reader-facing prose", AUTHOR_COLLABORATION)
        self.assertIn(
            "Reader-facing qualifier: required / not required + claim-local reason",
            OUTLINE_TEMPLATE,
        )
        self.assertIn("Claim communication boundary", PHASE_1_WORKBOARD)
        self.assertIn("Complete internal evidence boundary / non-claims", PHASE_1_WORKBOARD)
        self.assertIn(
            "Reader-facing qualifier: required / not required + reason",
            PHASE_1_WORKBOARD,
        )
        self.assertIn("Internal-only review cautions", PHASE_2_HANDOFF)
        self.assertIn(
            "do not append a disclaimer about an unclaimed distal outcome",
            PHASE_2_HANDOFF,
        )

    def test_reusable_examples_cannot_become_or_replace_project_state(self):
        for phrase in (
            "Examples in this reusable skill illustrate the method",
            "not project evidence",
            "not project evidence, author\ndecisions, active project claims, or a durable project record",
            "target\nproject repository before relying on it",
            "author rationale",
            "evidence boundary",
            "reader-facing qualifier disposition",
            "reopen trigger",
            "project-owned record remains authoritative",
            "keep the decision session-only",
            "never use the skill repository as substitute project storage",
        ):
            self.assertIn(phrase, CLAIM_FOCUSED_WRITING)

    def test_shared_awareness_is_a_rationale_or_hypothesis_until_evidenced(self):
        self.assertIn("Shared communication can also provide mutual awareness", POSITIONING)
        self.assertIn("design rationales or\noutcome hypotheses", POSITIONING)
        self.assertIn("Shared-awareness value or risk", AUDIT_TEMPLATE)
        self.assertIn("Shared-awareness value, risk, and evidence status", OUTLINE_TEMPLATE)

    def test_relationship_categories_are_domain_generic(self):
        self.assertIn("adjacent system or analogous intervention", POSITIONING)
        self.assertNotIn("adjacent coaching or feedback system", RELATED_WORK_CONTRACT)


if __name__ == "__main__":
    unittest.main()
