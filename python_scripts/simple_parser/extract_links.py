from bs4 import BeautifulSoup


src_html_file = str(input())
urls_list = []
topics_filenames_list = []
with open(src_html_file) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    a_blocks = soup.find_all('a', 'text-decoration-none link-dark me-2')
    link_num = 1
    for link in a_blocks:
        relative_url = link.get('href')
        full_url = "".join(["https://ru.hexlet.io", relative_url])
        urls_list.append(full_url)
        topic = link.get_text()  # Example: "Большая сложная тема"
        filename_for_topic = "_".join(topic.split())   # Result: "Большая_сложная_тема"
        filename_with_num = "_".join([str(link_num), filename_for_topic])
        topics_filenames_list.append(filename_with_num)
        link_num += 1
