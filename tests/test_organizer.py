"""Тесты для boxkit.organizer. Запуск: python -m unittest discover tests"""

import os
import shutil
import tempfile
import unittest
from pathlib import Path

from boxkit.organizer import category_for, organize


class OrganizerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def touch(self, name: str) -> Path:
        path = self.tmp / name
        path.write_text("x", encoding="utf-8")
        return path

    def test_category_for_known_and_unknown(self) -> None:
        self.assertEqual(category_for(".jpg"), "images")
        self.assertEqual(category_for(".PDF"), "documents")  # регистр не важен
        self.assertEqual(category_for(".xyz"), "other")

    def test_dry_run_moves_nothing(self) -> None:
        self.touch("photo.jpg")
        organize(self.tmp, dry_run=True)
        self.assertTrue((self.tmp / "photo.jpg").exists())
        self.assertFalse((self.tmp / "images").exists())

    def test_moves_by_category(self) -> None:
        self.touch("photo.jpg")
        self.touch("report.pdf")
        self.assertEqual(organize(self.tmp), 0)
        self.assertTrue((self.tmp / "images" / "photo.jpg").exists())
        self.assertTrue((self.tmp / "documents" / "report.pdf").exists())

    def test_name_collision_gets_suffix(self) -> None:
        self.touch("photo.jpg")
        (self.tmp / "images").mkdir()
        (self.tmp / "images" / "photo.jpg").write_text("old", encoding="utf-8")
        organize(self.tmp)
        self.assertTrue((self.tmp / "images" / "photo_1.jpg").exists())
        self.assertEqual((self.tmp / "images" / "photo.jpg").read_text(encoding="utf-8"), "old")

    def test_hidden_files_untouched(self) -> None:
        self.touch(".hidden.jpg")
        organize(self.tmp)
        self.assertTrue((self.tmp / ".hidden.jpg").exists())


if __name__ == "__main__":
    unittest.main()
