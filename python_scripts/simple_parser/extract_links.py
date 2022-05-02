from bs4 import BeautifulSoup


src_html_file = str(input())
urls_list = []
with open(src_html_file) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    a_blocks = soup.find_all('a', 'text-decoration-none link-dark me-2')
    for link in a_blocks:
        relative_url = link.get('href')
        full_url = "".join(["https://ru.hexlet.io", relative_url])
        urls_list.append(full_url)
