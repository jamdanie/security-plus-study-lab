"""Check known vectors, content changes, and command-line failure cases."""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from hash_file import hash_file, main


class HashTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "sample.bin"
        self.path.write_bytes(b"abc")

    def run_cli(self, args):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return main(args)

    def test_known_vector(self):
        self.assertEqual(hash_file(self.path),
                         "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

    def test_empty_file(self):
        self.path.write_bytes(b"")
        self.assertEqual(hash_file(self.path),
                         "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")

    def test_edit_changes_hash_and_rename_does_not(self):
        before = hash_file(self.path)
        renamed = self.path.with_name("renamed.bin")
        self.path.rename(renamed)
        self.assertEqual(before, hash_file(renamed))
        renamed.write_bytes(b"abd")
        self.assertNotEqual(before, hash_file(renamed))

    def test_uppercase_reference_matches(self):
        self.assertEqual(self.run_cli([str(self.path), "--expected", hash_file(self.path).upper()]), 0)

    def test_wrong_reference_returns_one(self):
        self.assertEqual(self.run_cli([str(self.path), "--expected", "0" * 64]), 1)

    def test_missing_file_returns_two(self):
        self.assertEqual(self.run_cli([str(self.path.with_name("missing"))]), 2)

    def test_invalid_reference_is_rejected(self):
        with self.assertRaises(SystemExit) as result:
            self.run_cli([str(self.path), "--expected", "invalid"])
        self.assertEqual(result.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
