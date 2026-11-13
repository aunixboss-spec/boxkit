# Примеры использования

## organizer — навести порядок в загрузках
```bash
# Сначала посмотреть, что произойдёт (ничего не перемещает)
python boxkit/organizer.py ~/Downloads --dry-run

# Потом выполнить
python boxkit/organizer.py ~/Downloads
```

## genpass — пароли
```bash
python boxkit/genpass.py                      # один пароль, 16 символов
python boxkit/genpass.py -l 24 -c 3           # три пароля по 24 символа
python boxkit/genpass.py -l 12 --no-symbols   # без спецсимволов
python boxkit/genpass.py --keep-ambiguous     # разрешить Il1O0o
```

## diskreport — куда делось место
```bash
python boxkit/diskreport.py D:\\ --top 20
python boxkit/diskreport.py ~/Downloads --min-size 10485760   # файлы больше 10 МБ
```

## renamer — фото с отпуска
```bash
python boxkit/renamer.py ./DCIM --prefix vacation --ext jpg --start 1
python boxkit/renamer.py ./DCIM --prefix vacation --ext jpg --dry-run
python boxkit/renamer.py ./DCIM --ext all      # все файлы подряд
```

## dedupe — дубликаты на диске
```bash
# Только отчёт: что где дублируется и сколько можно освободить
python boxkit/dedupe.py ~/Downloads

# Удалить копии (оригиналы остаются) — спросит подтверждение
python boxkit/dedupe.py ~/Downloads --delete
```

## timer — помодоро
```bash
python boxkit/timer.py 25 --label "Работа"
python boxkit/timer.py 5 --label "Перерыв" --beep
```
