"""Таймер обратного отсчёта / помодоро в терминале.

Использование:
    python timer.py 25          # 25 минут
    python timer.py 0:05        # 5 минут в формате М:СС
    python timer.py 90 --label "Перерыв"
"""

import argparse
import sys
import time


def parse_time(value: str) -> int:
    """Принимает минуты ('25') или 'М:СС' ('0:05'). Возвращает секунды."""
    if ":" in value:
        minutes, seconds = value.split(":", 1)
        return int(minutes) * 60 + int(seconds)
    return int(value) * 60


def run(seconds: int, label: str = "", beep: bool = False) -> None:
    remaining = seconds
    try:
        while remaining > 0:
            mm, ss = divmod(remaining, 60)
            print(f"\r{label} ⏳ {mm:02d}:{ss:02d} ", end="", flush=True)
            time.sleep(1)
            remaining -= 1
    except KeyboardInterrupt:
        print("\nОстановлено.")
        raise SystemExit(130)
    if beep:
        print("\a", end="")
    print(f"\r{label} ✅ Время вышло!        ")


def main() -> None:
    parser = argparse.ArgumentParser(description="Таймер в терминале")
    parser.add_argument("time", help="минуты (25) или М:СС (0:05)")
    parser.add_argument("--label", default="Таймер", help="подпись таймера")
    parser.add_argument("--beep", action="store_true", help="звуковой сигнал по окончании")
    args = parser.parse_args()

    try:
        seconds = parse_time(args.time)
    except ValueError:
        parser.error(f"не понял время: {args.time!r} (примеры: 25 или 0:05)")
    if seconds <= 0:
        parser.error("время должно быть больше нуля")

    run(seconds, args.label, beep=args.beep)


if __name__ == "__main__":
    main()
