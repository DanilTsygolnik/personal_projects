import os

def table_from_strings(src_file, cols=1):
    
    table_rows = []
    with open(src_file, 'r') as file:
        for line in file.readlines():
            table_rows.append("".join(["    <tr>\n", "".join([8*" ", "<td>", line[:-1], "</td>\n"]), "    </tr>\n"]))
    with open("table.txt", 'w') as file:
        file.write("<table>\n")
        for i in table_rows:
            file.write(i)
        file.write("</table>\n")

script_path = os.path.realpath(__file__)
dir_path = os.path.split(script_path)[0]
table_from_strings(os.path.join(dir_path, "table_template.txt"))

# for manual src_file choosing
#src_file_path = os.path.join(dir_path, str(input()))
#table_from_strings(src_file_path)
