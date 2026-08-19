from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts" / "initialize_phase1_workspace.py"


class InitializePhase1WorkspaceTests(unittest.TestCase):
    def test_initializer_creates_navigation_and_audited_reports_without_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary) / "project"
            repo.mkdir()
            existing = repo / "research-framing" / "author-decisions.md"
            existing.parent.mkdir()
            existing.write_text("# Preserve me\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(repo), "--project-name", "Example Project"],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("# Preserve me", existing.read_text(encoding="utf-8"))
            self.assertIn("HCI-PHASE1-NAV", existing.read_text(encoding="utf-8"))
            readme = (repo / "README.md").read_text(encoding="utf-8")
            self.assertIn("# Example Project", readme)
            self.assertIn("research-framing/reports/phase-1-progress.md", readme)
            for phrase in (
                "## The user value",
                "## Introduction — structure and outline",
                "Approach invariant",
                "Implementation substrate / empirical waist",
                "Platform-substitution result",
                "Adaptation-credit disposition",
                "Concrete behavior and consequence",
                "Why the focal context differs from the general intervention target",
                "Prior approaches and measured limits",
                "Outcome-oriented approach and mechanisms",
                "Newly enabled investigation",
                "Study and contribution statement",
                "split clusters as finely as the evidence permits",
                "has no numeric cap",
            ):
                self.assertIn(phrase, readme)
            headings = [line for line in readme.splitlines() if line.startswith("## ")]
            self.assertEqual(headings[0], "## At a glance")
            introduction = readme.split(
                "## Introduction — structure and outline", 1
            )[1].split("\n## ", 1)[0]
            self.assertLess(
                introduction.index("Approach invariant"),
                introduction.index("Implementation substrate / empirical waist"),
            )
            moves = (
                "Concrete behavior and consequence",
                "Why the focal context differs from the general intervention target",
                "Prior approaches and measured limits",
                "Outcome-oriented approach and mechanisms",
                "Newly enabled investigation",
                "Study and contribution statement",
            )
            positions = [introduction.index(move) for move in moves]
            self.assertEqual(positions, sorted(positions))
            framing = repo / "research-framing"
            for relative in (
                "starting-state.md",
                "search-log.md",
                "motivation-evidence-map.md",
                "related-work-matrix.md",
                "citation-chain-log.md",
                "approach-options.md",
                "contribution-options.md",
                "reviewer-panel/README.md",
            ):
                self.assertTrue((framing / relative).is_file(), relative)
            reports = framing / "reports"
            for name in (
                "README.md",
                "phase-1-progress.md",
                "literature-and-evidence.md",
                "phase-1-final.md",
                "artifact-index.md",
            ):
                self.assertTrue((reports / name).is_file(), name)
            self.assertFalse(list(reports.glob("*.html")))


if __name__ == "__main__":
    unittest.main()
