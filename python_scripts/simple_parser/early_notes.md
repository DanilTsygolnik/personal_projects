## Предварительные настройки

Для работы программ на Python в рабочем окружении должны присутствовать следующие пакеты:
- [beautifulsoap4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup);
- [requests](https://docs.python-requests.org/en/latest/);

Установка через с помощью `pip`, предпочтительно в отдельное виртуальное окружение.

## Автоматизированный сбор ссылок на уроки с главной страницы курса

Использование:
```
python extract_links.py /full/path/to/course_index.html /full/path/to/download_dir
```

[Программа](extract_links.py) получает на вход аргументы: URL главной страницы курса и путь к директории, в которую требуется сохранить выходные данные. 

Производится парсинг страницу курса, выбирает из html-кода блоки `<a>..<a/>` со ссылками и названиями уроков курса. Уроки курса сохраняются на диск html-файлами, при создании имен файлов используется текст из соответствующих блоков `<a>..</a>`.

Замечание: если в строке есть символы `/` или апострофы, это точно "поломает" программу. Таким образом, в коде требуется реализовать замену любых небуквенных символов на знаки подчеркивания (использовать regexp).

Использованные материалы:
- найти все блоки `<a href>...</a>` и извлечь из каждого url -- [пример](https://stackoverflow.com/a/14470595);
- найти блоки `<a href>...</a>` c определенным атрибутом -- [офф. доки](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all);
- как извлечь текст блока -- офф. доки, конец [Quick Start](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start);
- использование функции `zip()` при подготовке строк для файла `urls.txt` -- [пост](https://vk.com/wall-11462611_11550);
- как вызывать скрипт с аргументами в формате `python3 script.py arg1 arg2 ...` -- [example3](https://www.geeksforgeeks.org/executing-functions-with-multiple-arguments-at-a-terminal-in-python/);

## Загрузчик html-страниц 

Использование:
```
echo "https://google.com /home/user/dir/google.html" | python3 html_parser.py
```

[Программа](html_parser.py) получает на вход строку с URL, сохраняет соответствующий html-файл на диск.

Если в название файла включить путь к существующей директории, файл будет создан в ней. Директория должна быть создана перед вызовом программы, иначе код отработает с ошибкой.

Использованные материалы:
- https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
- https://docs.python-guide.org/scenarios/scrape/

## Автоматизация вызова загрузчика страниц

Запуск осуществляется из директории со скриптами (bash и python):
```bash
cat urls.txt | bash parse_addresses.sh
```

В текстовый файл записаны строки формата `https://.../page /home/user/dir`. URL и path разделены пробелом. Bash-скрипт поочередно передает пары URL-path в качестве параметров [загрузчику страниц](html_parser.py) для сохранения нужных страниц на диск.

Bash-скрипт написал по материалам:
- запись stdin в переменную -- по [статье](https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php); 
- итерация по строкам текстового файла -- по [статье](https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/);
- вызов python-скрипта внутри bash-скрипта --[ветка](https://stackoverflow.com/questions/4377109/shell-script-execute-a-python-program-from-within-a-shell-script) 

## Загрузка html-страниц всех уроков отдельного курса 

Использование:
```
python3 download_course.py course_main_page_url /full/path/to/download_dir
```
Передать параметры можно и в pipeline:
```
echo "course_main_page_url /full/path/to/download_dir" | python3 download_course.py
```

[Программа](download_course.py) получает на вход два аргумента: ссылку на главную страницу курса hexlet и абсолютный путь к директории для загрузки файлов. Директория уже должна быть создана, иначе скрипт "ломается", и не все html-страницы будут сохранены на диск.

Производится парсинг страницу курса, выбирает из html-кода блоки `<a>...<a/>` со ссылками и названиями уроков курса. С помощью регулярных выражений из текста заголовков удаляются любые символы, кроме букв и подчеркиваний, на выходе получается название для файла: строка из слов, разделённых `_`. Уроки курса сохраняются на диск html-файлами с соответсвующими названиями.


TODO: нужные директории создает bash-скрипт (см. следующий раздел), но это при загрузке сразу нескольких курсов. Однако, данную функцию разумнее реализовать внутри данной программы - чтобы при работе с URL по одной не приходилось каждый раз вручную вызывать `mkdir ...`.


Использованные материалы:
- правильная передача тела response в BeautifulSoap -- [пример](https://stackoverflow.com/a/39757879);
- использование `hashlib` в коде -- [пример](https://stackoverflow.com/a/59056837);
- работа с `hashlib`: метод `encode()` на [примерах](https://www.atqed.com/python-hashlib);
- присваивание значения переменных во время вычисления другого выражения (строка `while chunk := f.read(8192):`) -- [статья](https://medium.com/nuances-of-programming/%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0-%D0%B8-%D0%B7%D0%B0%D1%87%D0%B5%D0%BC-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80-%D0%B2-python-d2e70bf85a40);
- заменять все знаки, кроме букв и подчеркиваний, из текста для будущих названий файлов -- [пример](https://stackoverflow.com/a/875978);


## Загрузка html-страниц из нескольких курсов одной командой

Использование:
```
cat urls_and_dirs.txt | bash download_several.sh
```

В текстовый файл записаны строки формата `https://.../page /home/user/dir`. URL и path разделены пробелом. Каждая ссылка ведет на главную страницу одного из курсов hexlet. [Скрипт](download_several.sh) построчно считывает входные данные, при необходимости создаются директории для загрузки html-страниц. После создания каталогов каждый URL передается на обработку 
загрузчику уроков курса (см. предыдущий раздел).

Использованные материалы:
- [bash-скрипт](download_several.sh): выборка адреса из строки -- см. [example 1](https://www.tutorialkart.com/bash-shell-scripting/bash-split-string/);
- [bash-скрипт](download_several.sh): проверка существования директории и создание, при необходимости, перед вызовом python-скрипта -- [пример](https://www.cyberciti.biz/faq/howto-check-if-a-directory-exists-in-a-bash-shellscript/) конструкции `if ...`;
