Функционал:
- вывести список названий programming проектов (названия директорий с локальными git-репозиториями);
- чтение названия проекта с клавиатуры;
- сделать выбранную директорию текущей;
- подключение к github по ssh в текущем терминале;
- открыть дополнительные вкладки под vim и тесты в текущей директории.

Перед вводом на экране должно появляться следующее:
```
You have the following programming projects:
project_name1
project_name2
project_name3
...
project_nameX

Which one you want to work work with? Enter the name: <user enters the name>
```

Использованные материалы:
-[Append to variable](https://stackoverflow.com/questions/4181703/how-to-concatenate-string-variables-in-bash/18041780#18041780);
- идея создать шаблон сообщения, как array `(part1 part2 part3)` -- [по примеру](https://stackoverflow.com/a/15566034); использование `printf` вместо `echo` оттуда же;
- использование специальных символов (в частности `\n`) -- [по примеру](https://stackoverflow.com/a/3182519).

---

Возможно, пригодится для автозапуска
`xfce4-terminal --geometry=100x30+1250+0 --execute bash -c 'echo " " | termdown'`
