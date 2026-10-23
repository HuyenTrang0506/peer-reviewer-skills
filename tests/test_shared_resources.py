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
            path = self.root / "journal-peer-reviewer" / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"canonical {relative}\n")

    def test_check_is_read_only_and_reports_missing_resources(self):
        differences = SYNC.synchronize(self.root)
        self.assertEqual(set(differences), set(SYNC.SHARED_FILES))
        self.assertFalse((self.root / "conference-peer-reviewer").exists())

    def test_write_preserves_venue_specific_files_and_then_detects_drift(self):
        private_paths = ("SKILL.md", "assets/review-report.md", "references/worked-example.md")
        for relative in private_paths:
            path = self.root / "conference-peer-reviewer" / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("conference-specific\n")
        SYNC.synchronize(self.root, write=True)
        self.assertEqual(SYNC.synchronize(self.root), [])
        for relative in private_paths:
            self.assertEqual(
                (self.root / "conference-peer-reviewer" / relative).read_text(),
                "conference-specific\n",
            )
        changed = self.root / "conference-peer-reviewer" / SYNC.SHARED_FILES[0]
        changed.write_text("drift\n")
        self.assertEqual(SYNC.synchronize(self.root), [SYNC.SHARED_FILES[0]])
        self.assertEqual(changed.read_text(), "drift\n")

    def test_missing_source_prevents_partial_write(self):
        (self.root / "journal-peer-reviewer" / SYNC.SHARED_FILES[-1]).unlink()
        with self.assertRaises(FileNotFoundError):
            SYNC.synchronize(self.root, write=True)
        self.assertFalse((self.root / "conference-peer-reviewer").exists())


if __name__ == "__main__":
    unittest.main()
