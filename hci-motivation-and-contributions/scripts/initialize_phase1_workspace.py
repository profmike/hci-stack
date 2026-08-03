#!/usr/bin/env python3
"""Initialize a Phase 1 project workspace and render its navigable report shelf."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = SKILL_ROOT / "assets"

ROOT_ASSETS = (
    "agent-context.json",
    "phase-1-collaboration-workboard.md",
    "author-decisions.md",
    "source-manifest.md",
    "source-resolution.csv",
    "imported-bibliography-accountability.csv",
    "notebooklm-maintenance.md",
    "evidence-strength-register.md",
    "references.csv",
    "missing-full-copies.md",
    "claim-evidence-ledger.csv",
    "motivation-claim-research-queue.md",
    "authoritative-source-map.md",
    "current-practice-audit.md",
    "consequence-severity-ranking.md",
    "acm-sigchi-related-work-audit.md",
    "related-work-search-recall-audit.md",
    "related-work-contribution-tier-audit.md",
    "ranked-related-work-positioning.md",
    "prior-work-contribution-boundary.md",
    "prior-work-evidence-accounting.csv",
    "idea-provenance-ledger.csv",
    "late-found-work-postmortem.csv",
    "novelty-regression-sentinels.yaml",
    "exemplar-analysis.md",
    "terminology-contract.md",
    "related-work-quadrant-variations.md",
    "research-framing-outline.md",
    "phase-2-handoff.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create missing Phase 1 templates, a project README, and initial HTML reports."
    )
    parser.add_argument("repo", type=Path, help="Project repository root")
    parser.add_argument("--project-name", help="Display name (default: repository folder name)")
    parser.add_argument(
        "--no-render", action="store_true", help="Create source artifacts without rendering HTML"
    )
    return parser.parse_args()


def copy_missing(source: Path, destination: Path) -> bool:
    if destination.exists():
        return False
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return True


def main() -> int:
    args = parse_args()
    repo = args.repo.expanduser().resolve()
    if not repo.is_dir():
        raise SystemExit(f"project repository does not exist: {repo}")
    project_name = args.project_name or repo.name
    framing = repo / "research-framing"
    framing.mkdir(parents=True, exist_ok=True)
    for directory in (
        framing / "sources" / "full-text",
        framing / "decision-packets",
        framing / "quadrants",
        framing / "reviewer-panel",
        framing / "reports",
    ):
        directory.mkdir(parents=True, exist_ok=True)

    created: list[Path] = []
    for name in ROOT_ASSETS:
        destination = framing / name
        if copy_missing(ASSET_ROOT / name, destination):
            created.append(destination)
    if copy_missing(
        ASSET_ROOT / "decision-packet.md",
        framing / "decision-packets" / "decision-packet-template.md",
    ):
        created.append(framing / "decision-packets" / "decision-packet-template.md")
    if copy_missing(
        ASSET_ROOT / "related-work-quadrant.csv",
        framing / "quadrants" / "related-work-quadrant.csv",
    ):
        created.append(framing / "quadrants" / "related-work-quadrant.csv")

    readme = repo / "README.md"
    if not readme.exists():
        template = (ASSET_ROOT / "project-readme.md").read_text(encoding="utf-8")
        readme.write_text(template.replace("{{PROJECT_NAME}}", project_name), encoding="utf-8")
        created.append(readme)

    if not args.no_render:
        subprocess.run(
            [
                sys.executable,
                str(SKILL_ROOT / "scripts" / "render_phase1_reports.py"),
                str(framing),
                "--project-title",
                project_name,
            ],
            check=True,
        )
        subprocess.run(
            [
                sys.executable,
                str(SKILL_ROOT / "scripts" / "audit_phase1_reports.py"),
                str(framing),
            ],
            check=True,
        )

    print(f"PASS: initialized {framing}; created {len(created)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
