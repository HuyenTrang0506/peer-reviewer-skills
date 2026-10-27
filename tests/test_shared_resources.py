"""Check non-destructive synchronization of standalone review packages."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location(
    "sync_shared", Path(__file__).resolve().parents[1] / "scripts/sync_shared_resources.py"
)
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


class SharedResourceTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for relative in SYNC.SHARED_FILES:
            path = self.root / "common" / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"canonical {relative}\n")

    def test_check_is_read_only_and_reports_missing_resources(self):
        differences = SYNC.synchronize(self.root)
        expected = {
            f"{package}/{relative}"
            for package in SYNC.REVIEW_PACKAGES
            for relative in SYNC.SHARED_FILES
        }
        expected.add("professional-office-language/references/professional-language.md")
        self.assertEqual(set(differences), expected)
        for package in (*SYNC.REVIEW_PACKAGES, "professional-office-language"):
            self.assertFalse((self.root / package).exists())

    def test_write_preserves_venue_specific_files_and_then_detects_drift(self):
        private_paths = (
            "SKILL.md",
            "references/CONTENTS.md",
            "assets/review-report.md",
            "references/04-review-rounds/worked-example.md",
        )
        for package in SYNC.REVIEW_PACKAGES:
            for relative in private_paths:
                path = self.root / package / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(f"{package}-specific\n")
        SYNC.synchronize(self.root, write=True)
        self.assertEqual(SYNC.synchronize(self.root), [])
        for package in SYNC.REVIEW_PACKAGES:
            for relative in private_paths:
                self.assertEqual(
                    (self.root / package / relative).read_text(),
                    f"{package}-specific\n",
                )
        changed = self.root / "conference-peer-reviewer" / SYNC.SHARED_FILES[0]
        changed.write_text("drift\n")
        self.assertEqual(
            SYNC.synchronize(self.root), [f"conference-peer-reviewer/{SYNC.SHARED_FILES[0]}"]
        )
        self.assertEqual(changed.read_text(), "drift\n")

    def test_missing_source_prevents_partial_write(self):
        (self.root / "common" / SYNC.SHARED_FILES[-1]).unlink()
        with self.assertRaises(FileNotFoundError):
            SYNC.synchronize(self.root, write=True)
        for package in (*SYNC.REVIEW_PACKAGES, "professional-office-language"):
            self.assertFalse((self.root / package).exists())

    def test_common_changes_reach_both_packages_and_language_skill(self):
        SYNC.synchronize(self.root, write=True)
        source = self.root / "common" / SYNC.LANGUAGE_SOURCE
        source.write_text("revised shared language guidance\n")
        expected = {
            *(f"{package}/{SYNC.LANGUAGE_SOURCE}" for package in SYNC.REVIEW_PACKAGES),
            "professional-office-language/references/professional-language.md",
        }
        self.assertEqual(set(SYNC.synchronize(self.root)), expected)
        SYNC.synchronize(self.root, write=True)
        for relative in expected:
            self.assertEqual((self.root / relative).read_bytes(), source.read_bytes())
        self.assertEqual(SYNC.synchronize(self.root), [])


if __name__ == "__main__":
    unittest.main()
