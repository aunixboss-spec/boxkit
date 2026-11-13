"""Тесты для boxkit.genpass. Запуск: python -m unittest discover tests"""

import string
import unittest

from boxkit.genpass import AMBIGUOUS, generate


class GenPassTest(unittest.TestCase):
    def test_length(self) -> None:
        self.assertEqual(len(generate(16)), 16)
        self.assertEqual(len(generate(25)), 25)

    def test_too_short_raises(self) -> None:
        with self.assertRaises(ValueError):
            generate(3)

    def test_has_lowercase_and_digit(self) -> None:
        # Гарантия: хотя бы по одному символу из каждого набора
        for _ in range(50):
            password = generate(8)
            self.assertTrue(any(c in string.ascii_lowercase for c in password))
            self.assertTrue(any(c in string.ascii_uppercase for c in password))
            self.assertTrue(any(c in string.digits for c in password))
            self.assertTrue(any(c not in string.ascii_letters + string.digits for c in password))

    def test_no_symbols(self) -> None:
        password = generate(12, use_symbols=False)
        self.assertFalse(any(c not in string.ascii_letters + string.digits for c in password))

    def test_ambiguous_excluded_by_default(self) -> None:
        for _ in range(50):
            password = generate(20)
            self.assertEqual(set(password) & AMBIGUOUS, set())

    def test_keep_ambiguous_allows_them(self) -> None:
        seen_ambiguous = any(
            set(generate(20, keep_ambiguous=True)) & AMBIGUOUS for _ in range(200)
        )
        self.assertTrue(seen_ambiguous)


if __name__ == "__main__":
    unittest.main()
