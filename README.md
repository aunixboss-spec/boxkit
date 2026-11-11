<div align="center">

# 🧰 boxkit

**Набор крошечных CLI-утилит на чистом Python — ничего устанавливать не нужно.**

🌐 **[Сайт проекта](https://aunixboss-spec.github.io/boxkit/)** · 📖 [Примеры](docs/EXAMPLES.md) · 📄 [Лицензия](LICENSE)

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Deps](https://img.shields.io/badge/dependencies-zero-success)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey)
![Site](https://img.shields.io/badge/site-GitHub%20Pages-58a6ff?logo=github)

</div>

---

## ✨ Утилиты

| | Скрипт | Что делает |
|---|---|---|
| 🗂️ | `boxkit/organizer.py` | Раскладывает файлы по папкам-категориям (images, documents, audio…) |
| 🔐 | `boxkit/genpass.py` | Генерирует надёжные пароли через модуль `secrets` |
| 💾 | `boxkit/diskreport.py` | Показывает самые большие файлы в дереве каталогов |
| ✏️ | `boxkit/renamer.py` | Массово переименовывает файлы с нумерацией |
| ⏱️ | `boxkit/timer.py` | Таймер обратного отсчёта / помодоро прямо в терминале |

## 🌐 Сайт

Лендинг проекта живёт в этом же репозитории (`docs/index.html`) и автоматически
публикуется через **GitHub Pages**: https://aunixboss-spec.github.io/boxkit/

Чтобы включить публикацию: *Settings → Pages → Source: Deploy from a branch → `main` → `/docs`*.

## 🚀 Быстрый старт

```bash
git clone https://github.com/aunixboss-spec/boxkit.git
cd boxkit
```

Никаких `pip install` — только стандартная библиотека. Python **3.8+**.

## 📖 Примеры

```bash
# Навести порядок в загрузках (сначала --dry-run, потом по-настоящему)
python boxkit/organizer.py ~/Downloads --dry-run
python boxkit/organizer.py ~/Downloads

# Три пароля по 24 символа
python boxkit/genpass.py --length 24 --count 3

# Куда делось место на диске
python boxkit/diskreport.py . --top 10

# Переименовать отпускные фото
python boxkit/renamer.py ./DCIM --prefix vacation --ext jpg

# Помодоро: 25 минут работы
python boxkit/timer.py 25 --label "Работа"
```

Больше примеров — в [`docs/EXAMPLES.md`](docs/EXAMPLES.md).

## 🗺️ Планы

- [ ] `qr.py` — генерация QR-кодов
- [ ] `dedupe.py` — поиск дубликатов файлов по хэшу
- [ ] Цветной вывод (ANSI) для всех утилит

## 📄 Лицензия

Распространяется по лицензии [MIT](LICENSE).
