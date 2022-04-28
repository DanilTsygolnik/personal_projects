import requests


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
