from bs4 import BeautifulSoup
import requests
import hashlib
import time


# спарсить ссылки из index-файла по ссылке -- файл urls.txt на выходе
input_data = str(input()).split()  # https://course.com/index /home/user/download/dir
course_url = input_data[0]
course_page = requests.get(course_url)
soup = BeautifulSoup(course_page.content, 'html.parser')
a_blocks = soup.find_all('a', 'text-decoration-none link-dark me-2')
course_topics_urls = []
topics_filenames = []
link_num = 1
for link in a_blocks:
    relative_url = link.get('href')
    full_url = "".join(["https://ru.hexlet.io", relative_url])
    course_topics_urls.append(full_url)
    topic = link.get_text()  # Example: "Большая сложная тема"
    filename_for_topic = "_".join(topic.split())   # Result: "Большая_сложная_тема"
    filename_with_num = "_".join([str(link_num), filename_for_topic])
    topics_filenames.append(filename_with_num)
    link_num += 1
download_dir = input_data[1]
for url, filename in zip(course_topics_urls, topics_filenames):
    topic_page = requests.get(url)
    # saved_html_full_path example: /home/user/dir/pg.html
    saved_html_full_path = f'{download_dir}/{filename}'  
    with open(saved_html_full_path, 'w') as file:
        file.write(topic_page.text)
    # downloaded html integrity check
    md5_topic_page = hashlib.md5(topic_page.text.encode())
    with open(saved_html_full_path, "rb") as f:
        md5_file = hashlib.md5()
        while chunk := f.read(8192):
            md5_file.update(chunk)
    status_ok = (md5_topic_page.hexdigest() == md5_file.hexdigest())
    if status_ok:
        print(f'Downloaded {saved_html_full_path} -- OK')
    else:
        print(f'Downloaded {saved_html_full_path} -- HASH ERROR')
    next_request_delay_sec = 3
    print(f'Waiting for {next_request_delay_sec} seconds before next request...')
    time.sleep(next_request_delay_sec)
