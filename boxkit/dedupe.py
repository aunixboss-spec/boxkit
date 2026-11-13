"""Поиск дубликатов файлов по хэшу.

Использование:
    python dedupe.py ~/Downloads
    python dedupe.py ~/Downloads --delete          # спросит подтверждение
    python dedupe.py ~/Downloads --delete --yes    # без вопросов
"""

import argparse
import hashlib
import os
import sys
from collections import defaultdict

CHUNK = 65536


def file_hash(path: str) -> str:
    """SHA-256 файла, читая его по частям (не грузим всё в память)."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(CHUNK):
            digest.update(chunk)
    return digest.hexdigest()


def find_duplicates(root: str) -> dict[str, list[str]]:
    """Возвращает {хэш: [пути]} только для групп с дубликатами."""
    by_hash: dict[str, list[str]] = defaultdict(list)
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            path = os.path.join(dirpath, name)
            try:
                by_hash[file_hash(path)].append(path)
            except OSError:
                continue  # нет доступа / файл исчез — пропускаем
    return {h: paths for h, paths in by_hash.items() if len(paths) > 1}


def pick_keeper(paths: list[str]) -> str:
    """Оставляем самый короткий путь — как «оригинал»."""
    return min(paths, key=len)


def main() -> None:
    parser = argparse.ArgumentParser(description="Поиск дубликатов по хэшу")
    parser.add_argument("path", help="каталог для проверки")
    parser.add_argument("--delete", action="store_true", help="удалить копии (сначала показать план)")
    parser.add_argument("--yes", action="store_true", help="удалить без подтверждения")
    args = parser.parse_args()

    if not os.path.isdir(args.path):
        parser.error(f"не каталог: {args.path}")

    duplicates = find_duplicates(args.path)
    if not duplicates:
        print("✅ Дубликатов не найдено.")
        return

    total_files = 0
    total_bytes = 0
    for paths in duplicates.values():
        keeper = pick_keeper(paths)
        print(f"\n{keeper}")
        for path in paths:
            if path == keeper:
                continue
            size = os.path.getsize(path)
            total_files += 1
            total_bytes += size
            print(f"  копия ({size:,} байт): {path}")

    print(
        f"\nНайдено копий: {total_files}, "
        f"можно освободить {total_bytes / 1024 / 1024:.1f} МБ"
    )

    if not args.delete:
        print("Это был только отчёт. Для удаления добавьте --delete.")
        return

    if not args.yes:
        answer = input("Удалить перечисленные копии? [y/N] ")
        if answer.strip().lower() != "y":
            print("Отменено.")
            return

    removed = 0
    for paths in duplicates.values():
        keeper = pick_keeper(paths)
        for path in paths:
            if path == keeper:
                continue
            try:
                os.remove(path)
                removed += 1
            except OSError as e:
                print(f"⚠️ Не удалось удалить {path}: {e}", file=sys.stderr)
    print(f"🗑 Удалено копий: {removed}.")


if __name__ == "__main__":
    main()
