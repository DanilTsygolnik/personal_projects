from bs4 import BeautifulSoup
import requests
import hashlib


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
download_dir_full_path = input_data[1]
with open('urls.txt', 'w', encoding='utf-8') as file:
    for url, filename in zip(course_topics_urls, topics_filenames):
        formatted_string = f'{url} {download_dir_full_path}/{filename}\n'
        file.write(formatted_string)
