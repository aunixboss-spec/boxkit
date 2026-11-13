"""Тесты для boxkit.renamer. Запуск: python -m unittest discover tests"""

import shutil
import tempfile
import unittest
from pathlib import Path

from boxkit.renamer import rename


class RenamerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def touch(self, name: str, content: str = "x") -> Path:
        path = self.tmp / name
        path.write_text(content, encoding="utf-8")
        return path

    def test_dry_run_keeps_names(self) -> None:
        self.touch("IMG_1.jpg")
        rename(self.tmp, "trip", "jpg", 1, dry_run=True)
        self.assertTrue((self.tmp / "IMG_1.jpg").exists())

    def test_renames_with_numbering(self) -> None:
        self.touch("IMG_1.jpg")
        self.touch("IMG_2.jpg")
        self.assertEqual(rename(self.tmp, "trip", "jpg", 1, dry_run=False), 0)
        self.assertTrue((self.tmp / "trip1.jpg").exists())
        self.assertTrue((self.tmp / "trip2.jpg").exists())
        self.assertFalse((self.tmp / "IMG_1.jpg").exists())

    def test_ext_filter(self) -> None:
        self.touch("a.jpg")
        self.touch("b.png")
        rename(self.tmp, "f", "png", 1, dry_run=False)
        self.assertTrue((self.tmp / "a.jpg").exists())
        self.assertTrue((self.tmp / "f1.png").exists())

    def test_ext_all(self) -> None:
        self.touch("a.jpg")
        self.touch("b.png")
        rename(self.tmp, "f", "all", 1, dry_run=False)
        self.assertEqual(
            sorted(p.name for p in self.tmp.iterdir()), ["f1.jpg", "f2.png"]
        )

    def test_never_overwrites_existing(self) -> None:
        keeper = self.touch("f1.jpg", content="important")
        self.touch("IMG_1.jpg")
        rename(self.tmp, "f", "jpg", 1, dry_run=False)
        # существующий файл не должен быть перезаписан
        self.assertEqual(keeper.read_text(encoding="utf-8"), "important")

    def test_zero_padding(self) -> None:
        for i in range(1, 12):
            self.touch(f"IMG_{i}.jpg")
        rename(self.tmp, "trip", "jpg", 1, dry_run=False)
        self.assertTrue((self.tmp / "trip01.jpg").exists())
        self.assertTrue((self.tmp / "trip11.jpg").exists())


if __name__ == "__main__":
    unittest.main()
