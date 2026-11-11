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


def report(folder: Path, top: int) -> int:
    if not folder.is_dir():
        print(f"Не папка: {folder}")
        return 1

    files = [p for p in folder.rglob("*") if p.is_file()]
    sizes = sorted(((p.stat().st_size, p) for p in files), key=lambda x: -x[0])

    print(f"Файлов: {len(files)}, суммарно: {human_size(sum(s for s, _ in sizes))}\n")
    print(f"Топ-{top} самых больших файлов:")
    for size, path in sizes[:top]:
        print(f"  {human_size(size):>10}  {path.relative_to(folder)}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Самые большие файлы в каталоге")
    parser.add_argument("folder", type=Path, nargs="?", default=Path("."))
    parser.add_argument("--top", type=int, default=10, help="сколько файлов показать")
    args = parser.parse_args()
    raise SystemExit(report(args.folder, args.top))


if __name__ == "__main__":
    main()
