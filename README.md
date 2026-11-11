# boxkit

Небольшая коллекция полезных CLI-утилит на Python (только стандартная библиотека, без зависимостей).

## Утилиты

| Скрипт | Что делает |
|---|---|
| `boxkit/organizer.py` | Раскладывает файлы в папке по подпапкам-расширениям |
| `boxkit/genpass.py` | Генерирует надёжные пароли |
| `boxkit/diskreport.py` | Отчёт: самые большие файлы в дереве каталогов |
| `boxkit/renamer.py` | Массовое переименование файлов с нумерацией |
| `boxkit/timer.py` | Простой таймер/помодоро в терминале |

## Использование

```bash
python boxkit/organizer.py ~/Downloads
python boxkit/genpass.py --length 20 --count 5
python boxkit/diskreport.py . --top 10
python boxkit/renamer.py ./photos --prefix vacation --ext jpg
python boxkit/timer.py 25
```

Все скрипты поддерживают `--help`.

## Требования

Python 3.8+. Ничего устанавливать не нужно.
