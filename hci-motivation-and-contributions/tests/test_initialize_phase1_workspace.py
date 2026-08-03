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
            self.assertEqual(existing.read_text(encoding="utf-8"), "# Preserve me\n")
            readme = (repo / "README.md").read_text(encoding="utf-8")
            self.assertIn("# Example Project", readme)
            self.assertIn("research-framing/reports/phase-1-progress.html", readme)
            reports = repo / "research-framing" / "reports"
            for name in (
                "phase-1-progress.html",
                "literature-and-evidence.html",
                "phase-1-final.html",
                "artifact-index.html",
            ):
                self.assertTrue((reports / name).is_file(), name)


if __name__ == "__main__":
    unittest.main()
