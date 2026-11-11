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
```

## diskreport — куда делось место
```bash
python boxkit/diskreport.py D:\\ --top 20
```

## renamer — фото с отпуска
```bash
python boxkit/renamer.py ./DCIM --prefix vacation --ext jpg --start 1
python boxkit/renamer.py ./DCIM --prefix vacation --ext jpg --dry-run
```

## timer — помодоро
```bash
python boxkit/timer.py 25 --label "Работа"
python boxkit/timer.py 5 --label "Перерыв"
```
