"""Разложить файлы в папке по подпапкам-расширениям.

Пример: photo.jpg -> images/photo.jpg (категория определяется по расширению).

Использование:
    python organizer.py <папка> [--dry-run]
"""

import argparse
import shutil
import sys
from pathlib import Path

CATEGORY_MAP = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".ico", ".tiff", ".heic"},
    "documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".rtf", ".odt", ".xlsx", ".csv", ".pptx", ".epub"},
    "audio": {".mp3", ".wav", ".flac", ".ogg", ".m4a", ".wma", ".opus"},
    "video": {".mp4", ".mkv", ".avi", ".mov", ".webm", ".m4v", ".ts"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"},
    "code": {".py", ".js", ".ts", ".html", ".css", ".json", ".xml", ".sh", ".bat", ".java", ".c", ".cpp", ".rs", ".go", ".ipynb"},
    "fonts": {".ttf", ".otf", ".woff", ".woff2"},
    "programs": {".exe", ".msi", ".apk", ".dmg", ".appimage", ".deb", ".rpm"},
    "torrents": {".torrent"},
}


def category_for(suffix: str) -> str:
    for category, exts in CATEGORY_MAP.items():
        if suffix.lower() in exts:
            return category
    return "other"


def organize(folder: Path, dry_run: bool = False) -> int:
    if not folder.is_dir():
        print(f"Не папка: {folder}", file=sys.stderr)
        return 1

    moved = 0
    for item in sorted(folder.iterdir()):
        if item.is_dir() or item.name.startswith("."):
            continue
        target_dir = folder / category_for(item.suffix)
        target = target_dir / item.name
        if dry_run:
            print(f"[dry-run] {item.name} -> {target_dir.name}/")
        else:
            target_dir.mkdir(exist_ok=True)
            if target.exists():
                stem, num = target.stem, 1
                while target.exists():
                    target = target_dir / f"{stem}_{num}{item.suffix}"
                    num += 1
            shutil.move(str(item), target)
            print(f"{item.name} -> {target.relative_to(folder)}")
        moved += 1

    print(f"\nОбработано файлов: {moved}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Раскладка файлов по расширениям")
    parser.add_argument("folder", type=Path, help="папка для сортировки")
    parser.add_argument("--dry-run", action="store_true", help="только показать, что будет сделано")
    args = parser.parse_args()
    return organize(args.folder, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
