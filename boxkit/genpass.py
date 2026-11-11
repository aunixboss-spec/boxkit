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


def generate(length: int, use_symbols: bool = True) -> str:
    if length < 4:
        raise ValueError("Длина пароля должна быть не меньше 4")

    pools = [LOWER, UPPER, DIGITS]
    if use_symbols:
        pools.append(SYMBOLS)

    # Гарантируем хотя бы по одному символу из каждого набора
    chars = [secrets.choice(pool) for pool in pools]
    alphabet = "".join(pools).translate(str.maketrans("", "", "".join(AMBIGUOUS)))
    chars += [secrets.choice(alphabet) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def main() -> None:
    parser = argparse.ArgumentParser(description="Генератор паролей")
    parser.add_argument("--length", type=int, default=16, help="длина пароля (по умолчанию 16)")
    parser.add_argument("--count", type=int, default=1, help="сколько паролей сгенерировать")
    parser.add_argument("--no-symbols", action="store_true", help="без спецсимволов")
    args = parser.parse_args()

    for _ in range(args.count):
        print(generate(args.length, use_symbols=not args.no_symbols))


if __name__ == "__main__":
    main()
