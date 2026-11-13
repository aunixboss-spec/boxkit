"""Тесты для boxkit.timer. Запуск: python -m unittest discover tests"""

import unittest

from boxkit.timer import parse_time


class TimerTest(unittest.TestCase):
    def test_minutes(self) -> None:
        self.assertEqual(parse_time("25"), 25 * 60)
        self.assertEqual(parse_time("0"), 0)

    def test_minutes_seconds(self) -> None:
        self.assertEqual(parse_time("0:05"), 5)
        self.assertEqual(parse_time("1:30"), 90)
        self.assertEqual(parse_time("90:00"), 90 * 60)

    def test_invalid_raises_value_error(self) -> None:
        for value in ("abc", "", "1:", ":5", "1:2:3"):
            with self.assertRaises(ValueError):
                parse_time(value)


if __name__ == "__main__":
    unittest.main()
