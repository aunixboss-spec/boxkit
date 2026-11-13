"""Отчёт о самых больших файлах в дереве каталогов.

Использование:
    python diskreport.py <папка> --top 10
"""

import argparse
from pathlib import Path


def human_size(num: int) -> str:
    for unit in ("Б", "КиБ", "МиБ", "ГиБ", "ТиБ"):
        if num < 1024:
            return f"{num:.1f} {unit}" if unit != "Б" else f"{num} {unit}"
        num /= 1024
    return f"{num:.1f} ПиБ"


def report(folder: Path, top: int, min_size: int = 0) -> int:
    if not folder.is_dir():
        print(f"Не папка: {folder}")
        return 1

    files = [
        p for p in folder.rglob("*")
        if p.is_file() and not any(part.startswith(".") for part in p.relative_to(folder).parts)
    ]
    sizes = []
    for p in files:
        try:
            size = p.stat().st_size
        except OSError:
            continue  # файл исчез или нет доступа — не падаем
        if size >= min_size:
            sizes.append((size, p))
    sizes.sort(key=lambda x: -x[0])

    shown = sizes[:top]
    print(f"Файлов: {len(sizes)}, суммарно: {human_size(sum(s for s, _ in sizes))}\n")
    if not shown:
        print("Ничего не найдено (попробуйте уменьшить --min-size).")
        return 0
    print(f"Топ-{top} самых больших файлов:")
    for size, path in shown:
        print(f"  {human_size(size):>10}  {path.relative_to(folder)}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Самые большие файлы в каталоге")
    parser.add_argument("folder", type=Path, nargs="?", default=Path("."))
    parser.add_argument("--top", type=int, default=10, help="сколько файлов показать")
    parser.add_argument("--min-size", type=int, default=0, metavar="БАЙТЫ", help="игнорировать файлы меньше (в байтах)")
    args = parser.parse_args()
    if args.top < 1:
        parser.error("--top должен быть не меньше 1")
    raise SystemExit(report(args.folder, args.top, args.min_size))


if __name__ == "__main__":
    main()
