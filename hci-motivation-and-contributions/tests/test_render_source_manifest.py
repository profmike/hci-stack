"""The source manifest's identifiers are generated, not retyped.

Wrong DOIs reached an author because ``source-manifest.md`` held a second, hand-maintained
copy of the ledger's identifiers and nothing kept the two equal. These tests hold the fix in
place: the derived columns come from the ledger, the manifest-only judgements survive
regeneration untouched, and drift is an error rather than a surprise.
"""

from __future__ import annotations

import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).parents[1] / "scripts"


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RENDER = load("render_source_manifest")
CHECK = load("check_source_resolution")

HEADERS = (
    "Source ID",
    "Citation key",
    "Bibliographic identity",
    "Tier",
    "DOI/canonical URL",
    "Canonical repository location",
    "Source-resolution state/locator",
    "Claim-matched upgrade search / stronger source",
    "Author-access request surfaced date/locator",
    "Notes",
)


def ledger_row(**overrides: str) -> dict[str, str]:
    row = {column: "" for column in CHECK.REQUIRED_COLUMNS}
    row.update(
        {
            "source_id": "SR-001",
            "citation_key": "iwata-1996",
            "bibliographic_identity": "Iwata & Fujii 1996, Virtual Perambulator, VRAIS'96",
            "canonical_url": "https://doi.org/10.1109/VRAIS.1996.490511",
            "source_provenance": "independent concept search",
            "candidate_role": "prior-work comparator",
            "relevance": "retain",
            "acquisition_state": "FULL_TEXT_ASSESSED",
            "full_copy_locator": "sources/full-text/iwata-1996.pdf",
            "full_text_review_locator": "reviews/iwata-1996.md",
            "upgrade_search": "no stronger direct source found",
            "identity_verified_against": "held copy p.60 title page, 2026-01-01",
        }
    )
    row.update(overrides)
    return row


def write_project(directory: Path, rows: list[dict[str, str]], manifest_body: str) -> None:
    ledger = directory / "source-resolution.csv"
    with ledger.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CHECK.REQUIRED_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    separator = "|" + "|".join("---" for _ in HEADERS) + "|"
    manifest = (
        "# Source manifest\n\n"
        + "| " + " | ".join(HEADERS) + " |\n"
        + separator + "\n"
        + manifest_body
        + "\n## Search log\n"
    )
    (directory / "source-manifest.md").write_text(manifest, encoding="utf-8")


class RenderSourceManifestTests(unittest.TestCase):
    def test_a_stale_printed_doi_is_replaced_by_the_ledger_value(self):
        with tempfile.TemporaryDirectory() as name:
            directory = Path(name)
            stale = (
                "| SR-001 | iwata-1996 | Iwata & Fujii 1996 | T1 | "
                "https://doi.org/10.1109/VRAIS.1996.490509 | old/path.pdf | UNASSESSED | "
                " |  | reads well |\n"
            )
            write_project(directory, [ledger_row()], stale)
            output, changes = RENDER.render(directory)

            self.assertTrue(any("490511" in change for change in changes), changes)
            self.assertIn("10.1109/VRAIS.1996.490511", output)
            self.assertNotIn("490509", output)
            # A manifest-only judgement no ledger holds must survive regeneration.
            self.assertIn("reads well", output)
            self.assertIn("| T1 |", output)

    def test_a_ledger_row_absent_from_the_page_is_added(self):
        with tempfile.TemporaryDirectory() as name:
            directory = Path(name)
            write_project(directory, [ledger_row()], "")
            output, changes = RENDER.render(directory)
            self.assertTrue(any("row added" in change for change in changes), changes)
            self.assertIn("iwata-1996", output)

    def test_the_checker_fails_on_a_manifest_that_has_drifted(self):
        with tempfile.TemporaryDirectory() as name:
            directory = Path(name)
            stale = (
                "| SR-001 | iwata-1996 | Iwata & Fujii 1996 | T1 | "
                "https://doi.org/10.1109/VRAIS.1996.490509 | old/path.pdf | UNASSESSED | "
                " |  | reads well |\n"
            )
            write_project(directory, [ledger_row()], stale)
            errors = CHECK.check_source_manifest_generated(
                directory / "source-resolution.csv"
            )
            self.assertTrue(
                any("disagrees with source-resolution.csv" in error for error in errors),
                errors,
            )

    def test_a_regenerated_manifest_passes_the_checker(self):
        with tempfile.TemporaryDirectory() as name:
            directory = Path(name)
            write_project(directory, [ledger_row()], "")
            output, _ = RENDER.render(directory)
            (directory / "source-manifest.md").write_text(output, encoding="utf-8")
            self.assertEqual(
                CHECK.check_source_manifest_generated(directory / "source-resolution.csv"),
                [],
            )

    def test_a_pipe_inside_a_ledger_value_cannot_break_the_table(self):
        with tempfile.TemporaryDirectory() as name:
            directory = Path(name)
            row = ledger_row(bibliographic_identity="Iwata 1996 | VRAIS proceedings")
            write_project(directory, [row], "")
            output, _ = RENDER.render(directory)
            self.assertIn(r"Iwata 1996 \| VRAIS proceedings", output)
            (directory / "source-manifest.md").write_text(output, encoding="utf-8")
            # The escaped cell must still round-trip, or the next run would "fix" it forever.
            self.assertEqual(
                CHECK.check_source_manifest_generated(directory / "source-resolution.csv"),
                [],
            )


if __name__ == "__main__":
    unittest.main()
