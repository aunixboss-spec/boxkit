"""Массовое переименование файлов с нумерацией.

Пример: photo1.jpg, photo2.jpg, ...
    python renamer.py ./photos --prefix vacation --ext jpg --start 1

С флагом --dry-run ничего не переименовывает, только показывает план.
"""

import argparse
from pathlib import Path


def rename(folder: Path, prefix: str, ext: str, start: int, dry_run: bool) -> int:
    if not folder.is_dir():
        print(f"Не папка: {folder}")
        return 1

    ext = ext.lstrip(".").lower()
    files = sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() == f".{ext}")
    width = len(str(start + len(files) - 1))

    for index, path in enumerate(files, start=start):
        new_name = f"{prefix}{index:0{width}d}{path.suffix}"
        if dry_run:
            print(f"[dry-run] {path.name} -> {new_name}")
        else:
            path.rename(folder / new_name)
            print(f"{path.name} -> {new_name}")

    print(f"\nФайлов к переименованию: {len(files)}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Массовое переименование")
    parser.add_argument("folder", type=Path)
    parser.add_argument("--prefix", default="file", help="префикс имени")
    parser.add_argument("--ext", default="jpg", help="расширение файлов")
    parser.add_argument("--start", type=int, default=1, help="начальный номер")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    raise SystemExit(rename(args.folder, args.prefix, args.ext, args.start, args.dry_run))


if __name__ == "__main__":
    main()
