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
