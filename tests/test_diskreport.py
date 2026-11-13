"""Тесты для boxkit.diskreport. Запуск: python -m unittest discover tests"""

import shutil
import tempfile
import unittest
from pathlib import Path

from boxkit.diskreport import human_size, report


class DiskReportTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_human_size_bytes(self) -> None:
        self.assertEqual(human_size(0), "0 Б")
        self.assertEqual(human_size(512), "512 Б")

    def test_human_size_kib_and_mib(self) -> None:
        self.assertEqual(human_size(1024), "1.0 КиБ")
        self.assertEqual(human_size(5 * 1024 * 1024), "5.0 МиБ")

    def test_report_exit_codes(self) -> None:
        self.assertEqual(report(self.tmp, 5), 0)          # пустая папка — ок
        self.assertEqual(report(self.tmp / "nope", 5), 1)  # нет папки — ошибка

    def test_report_skips_hidden(self) -> None:
        (self.tmp / "big.bin").write_bytes(b"x" * 3000)
        hidden = self.tmp / ".hidden"
        hidden.mkdir()
        (hidden / "huge.bin").write_bytes(b"x" * 9000)
        self.assertEqual(report(self.tmp, 5), 0)


if __name__ == "__main__":
    unittest.main()
