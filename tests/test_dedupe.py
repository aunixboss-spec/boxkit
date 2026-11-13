"""Тесты для boxkit.dedupe. Запуск: python -m unittest discover tests"""

import os
import shutil
import tempfile
import unittest

from boxkit.dedupe import find_duplicates, pick_keeper


class DedupeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write(self, name: str, content: bytes) -> str:
        path = os.path.normpath(os.path.join(self.tmp, name))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(content)
        return path

    def test_no_duplicates(self) -> None:
        self.write("a.txt", b"one")
        self.write("b.txt", b"two")
        self.assertEqual(find_duplicates(self.tmp), {})

    def test_finds_duplicates_in_subdirs(self) -> None:
        a = self.write("a.txt", b"same content")
        b = self.write("sub/b.txt", b"same content")
        self.write("c.txt", b"different")
        groups = find_duplicates(self.tmp)
        self.assertEqual(len(groups), 1)
        self.assertEqual(sorted(next(iter(groups.values()))), sorted([a, b]))

    def test_pick_keeper_is_shortest_path(self) -> None:
        paths = [os.path.join(self.tmp, "longer", "name.txt"), os.path.join(self.tmp, "orig.txt")]
        self.assertEqual(pick_keeper(paths), paths[1])


if __name__ == "__main__":
    unittest.main()
