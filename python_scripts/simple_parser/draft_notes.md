## Предварительные настройки

Для работы скриптов требуются следующие пакеты:
- [beautifulsoap4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup);
- [requests](https://docs.python-requests.org/en/latest/);

Установка через с помощью `pip`, предпочтительно в отдельное виртуальное окружение.

## Подготовка списка адресов страниц курса для загрузки

[Код](extract_links.py)

Использованные материалы:
- найти все блоки `<a href>...</a>` и извлечь из каждого url -- [пример](https://stackoverflow.com/a/14470595);
- найти блоки `<a href>...</a>` c определенным атрибутом -- [офф. доки](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all);
- как извлечь текст блока -- офф. доки, конец [Quick Start](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start);
- использование функции `zip()` при подготовке строк для файла `urls.txt` -- [пост](https://vk.com/wall-11462611_11550);
- как вызывать скрипт с аргументами в формате `python3 script.py arg1 arg2 ...` -- [example3](https://www.geeksforgeeks.org/executing-functions-with-multiple-arguments-at-a-terminal-in-python/);

Использование:
```
python extract_links.py /full/path/to/course_index.html /full/path/to/download_dir
```

## Скрипт-парсер

[Программа](html_parser.py) получает на вход строку с URL, сохраняет соответствующий html-файл на диск.

Использование:
```
echo "https://google.com /home/user/dir/google.html" | python3 html_parser.py
```

Если в название файла включить путь к существующей директории, файл будет создан в ней.

Использованные материалы:
- https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
- https://docs.python-guide.org/scenarios/scrape/

## Bash-скрипт

Построчно считывает данные подготовленного ранее файла `urls.txt`, для каждой строки производит вызов [скрипта-парсера](html_parser.py).

Запуск осуществляется из директории со скриптами (bash и python):
```bash
cat urls.txt | bash parse_addresses.sh
```

Bash-скрипт написал по материалам:
- запись stdin в переменную -- по [статье](https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php); 
- итерация по строкам текстового файла -- по [статье](https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/);
- вызов python-скрипта внутри bash-скрипта --[ветка](https://stackoverflow.com/questions/4377109/shell-script-execute-a-python-program-from-within-a-shell-script) 

## Парсинг одной командой 

[Скрипт](download_course.py)

Использование:
```
# option 1
python3 download_course.py course_main_page_url /full/path/to/download_dir
# option 2
echo "course_main_page_url /full/path/to/download_dir" | python3 download_course.py
```

Использованные материалы:
- правильная передача тела response в BeautifulSoap -- [пример](https://stackoverflow.com/a/39757879);
- использование `hashlib` в коде -- [пример](https://stackoverflow.com/a/59056837);
- работа с `hashlib`: метод `encode()` на [примерах](https://www.atqed.com/python-hashlib);
- присваивание значения переменных во время вычисления другого выражения (строка `while chunk := f.read(8192):`) -- [статья](https://medium.com/nuances-of-programming/%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0-%D0%B8-%D0%B7%D0%B0%D1%87%D0%B5%D0%BC-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80-%D0%B2-python-d2e70bf85a40);
- заменять все знаки, кроме букв и подчеркиваний, из текста для будущих названий файлов -- [пример](https://stackoverflow.com/a/875978);


## Загрузка нескольких курсов одной командой

[Скрипт](download_several.sh)

Использование:
```
cat urls_and_dirs.txt | bash download_several.sh
```

Файл `urls_and_dirs.txt` содержит строки формата `https://.../page /home/user/dir`      
URL и path разделены пробелом.

Использованные материалы:
- [bash-скрипт](download_several.sh): выборка адреса из строки -- см. [example 1](https://www.tutorialkart.com/bash-shell-scripting/bash-split-string/);
- [bash-скрипт](download_several.sh): проверка существования директории и создание, при необходимости, перед вызовом python-скрипта -- [пример](https://www.cyberciti.biz/faq/howto-check-if-a-directory-exists-in-a-bash-shellscript/) конструкции `if ...`;
