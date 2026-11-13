"""Генератор надёжных паролей.

Использование:
    python genpass.py --length 20 --count 5 --no-symbols
"""

import argparse
import secrets
import string

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?"

AMBIGUOUS = set("Il1O0o")


def generate(length: int, use_symbols: bool = True, keep_ambiguous: bool = False) -> str:
    if length < 4:
        raise ValueError("Длина пароля должна быть не меньше 4")

    pools = [LOWER, UPPER, DIGITS]
    if use_symbols:
        pools.append(SYMBOLS)

    if not keep_ambiguous:
        # Убираем неоднозначные символы (Il1O0o) из всех наборов,
        # а не только из «наполнителя» — иначе они всё равно попадают в пароль
        pools = ["".join(c for c in pool if c not in AMBIGUOUS) for pool in pools]

    # Гарантируем хотя бы по одному символу из каждого набора
    chars = [secrets.choice(pool) for pool in pools]
    alphabet = "".join(pools)
    chars += [secrets.choice(alphabet) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def main() -> None:
    parser = argparse.ArgumentParser(description="Генератор паролей")
    parser.add_argument("--length", type=int, default=16, help="длина пароля (по умолчанию 16)")
    parser.add_argument("--count", type=int, default=1, help="сколько паролей сгенерировать")
    parser.add_argument("--no-symbols", action="store_true", help="без спецсимволов")
    parser.add_argument("--keep-ambiguous", action="store_true", help="разрешить неоднозначные символы (Il1O0o)")
    args = parser.parse_args()

    if args.length < 4:
        parser.error("длина пароля должна быть не меньше 4")
    if args.count < 1:
        parser.error("--count должен быть не меньше 1")

    for _ in range(args.count):
        print(generate(args.length, use_symbols=not args.no_symbols, keep_ambiguous=args.keep_ambiguous))


if __name__ == "__main__":
    main()
