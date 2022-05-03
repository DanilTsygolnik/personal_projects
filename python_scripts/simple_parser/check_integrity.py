import hashlib
import sys
import requests


url = sys.argv[1]
downloaded_html_full_path = sys.argv[2]  # example: /home/user/dir/webpage.html
response = requests.get(url)
md5_response = hashlib.md5(response.text)
with open(downloaded_html_full_path, 'w') as f:
    f.write(response.text)
with open(downloaded_html_full_path, "rb") as f:
    md5_file = hashlib.md5()
    while chunk := f.read(8192):
        md5_file.update(chunk)
print(md5_response)
print(md5_file)
print(md5_response.hexdigest())
print(md5_file.hexdigest())
print(md5_response.hexdigest() == md5_file.hexdigest())
