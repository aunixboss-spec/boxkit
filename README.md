<div align="center">

# boxkit

### Твой терминал перестаёт быть свалкой

**6 CLI-утилит на чистом Python.** Ноль зависимостей, ноль настройки —
скачал и запустил. Наведи порядок в файлах, сгенерируй пароль, найди, куда делось место на диске.

[![Website](https://img.shields.io/badge/website-GitHub_Pages-58a6ff?logo=github)](https://aunixboss-spec.github.io/boxkit/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Deps](https://img.shields.io/badge/dependencies-zero-success)](#быстрый-старт)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)](#быстрый-старт)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey)](#быстрый-старт)

</div>

---

## Проблема

Downloads — это свалка из 400 файлов. Пароли из маркета ненадёжны. Диск забит — непонятно чем.
Для каждой мелочи ставить отдельный пакет с десятью зависимостями не хочется.

## Решение

**boxkit** — маленькие утилиты, которые решают одну задачу и не лезут в систему:
только стандартная библиотека Python, ничего не устанавливается, ничего не ломается.

```text
$ python boxkit/organizer.py ~/Downloads

photo.jpg   -> images/photo.jpg
report.pdf  -> documents/report.pdf
song.mp3    -> audio/song.mp3
```

## Что внутри

| Утилита | Что делает | Почему удобно |
|---|---|---|
| [`organizer`](boxkit/organizer.py) | Раскладывает файлы по категориям | Сначала `--dry-run` — ничего не перемещает |
| [`genpass`](boxkit/genpass.py) | Криптостойкие пароли | Модуль `secrets`, без неоднозначных символов |
| [`diskreport`](boxkit/diskreport.py) | Топ самых больших файлов | Мгновенный ответ «куда делось место» |
| [`renamer`](boxkit/renamer.py) | Массовое переименование | Нумерация с нулями: `trip01.jpg` |
| [`timer`](boxkit/timer.py) | Помодоро в терминале | Без браузера и уведомлений |
| [`dedupe`](boxkit/dedupe.py) | Поиск дубликатов по хэшу | Сначала отчёт, удаление — только по `--delete` |

## Почему это работает

- **Zero dependencies** — только стандартная библиотека, Python 3.8+
- **Безопасно по умолчанию** — все деструктивные операции сначала показывают план (`--dry-run`)
- **Кроссплатформенно** — Windows, Linux, macOS из коробки
- **Один формат** — все утилиты понимают `--help`

## Быстрый старт

```bash
git clone https://github.com/aunixboss-spec/boxkit.git
cd boxkit
python boxkit/organizer.py ~/Downloads --dry-run
```

Больше примеров — в [`docs/EXAMPLES.md`](docs/EXAMPLES.md). Сайт проекта: [aunixboss-spec.github.io/boxkit](https://aunixboss-spec.github.io/boxkit/).

## Roadmap

- [x] `dedupe.py` — поиск дубликатов по хэшу
- [ ] `qr.py` — генерация QR-кодов
- [ ] Цветной ANSI-вывод для всех утилит

<div align="center">

**Полезно? Поставь звезду — это единственная валюта open source**

[Сообщить об ошибке](https://github.com/aunixboss-spec/boxkit/issues) · [Предложить утилиту](https://github.com/aunixboss-spec/boxkit/issues)

</div>

---

MIT © [adrenachrome](https://github.com/aunixboss-spec)
