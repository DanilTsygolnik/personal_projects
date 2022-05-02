## Скрипт-парсер

Использованные материалы:
- https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
- https://docs.python-guide.org/scenarios/scrape/

Парсинг веб-страницы - [файл](html_parser.py)

Варианты:
- только URL, тогда веб-страница будет сохранена в файл "parse_result.html" (название по умолчанию);
- строка вида `<url> -o <custom_name>`, тогда веб-страница будет сохранена в файл "custom_name.html";

Если в название файла включить путь к существующей директории, файл будет создан в ней.

## Bash-скрипт

Bash-скрипт написал по материалам:
- запись stdin в переменную -- по [статье](https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php); 
- итерация по строкам текстового файла -- по [статье](https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/);
- вызов python-скрипта внутри bash-скрипта --[ветка](https://stackoverflow.com/questions/4377109/shell-script-execute-a-python-program-from-within-a-shell-script) 

Запуск осуществляется из директории со скриптами (bash и python):
`cat urls.txt | bash parse_addresses.sh`

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
