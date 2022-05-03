import requests
import hashlib


input_data = str(input()).split()
url = input_data[0]
downloaded_html_full_path = input_data[1]  # example: /home/user/dir/webpage.html
response = requests.get(url)
with open(downloaded_html_full_path, 'w') as file:
    file.write(response.text)
# downloaded html integrity check
md5_response = hashlib.md5(response.text.encode())
with open(downloaded_html_full_path, "rb") as f:
    md5_file = hashlib.md5()
    while chunk := f.read(8192):
        md5_file.update(chunk)
status_ok = (md5_response.hexdigest() == md5_file.hexdigest())
if status_ok:
    print(f'Downloaded {downloaded_html_full_path} -- OK')
else:
    print(f'Downloaded {downloaded_html_full_path} -- HASH ERROR')
