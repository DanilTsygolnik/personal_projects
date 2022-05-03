import requests
import hashlib


def get_file_name(parameters:list) -> str:
    file_name = "parse_result.html"
    if "-o" in parameters:
        file_name = "".join([parameters[2], ".html"])
    return file_name

input_str = str(input())
parameters = input_str.split()
my_url = parameters[0]
file_name = get_file_name(parameters)
response = requests.get(my_url)
with open(file_name, 'w') as file:
    file.write(response.text)
# downloaded html integrity check
md5_response = hashlib.md5(response.text.encode())
with open(downloaded_html_full_path, "rb") as f:
    md5_file = hashlib.md5()
    while chunk := f.read(8192):
        md5_file.update(chunk)
status_ok = (md5_response.hexdigest() == md5_file.hexdigest())
if status_ok:
    print(f'Downloaded {filename} -- OK')
else:
    print(f'Downloaded {filename} -- HASH ERROR')
