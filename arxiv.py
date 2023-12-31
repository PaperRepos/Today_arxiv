import os
import requests
from datetime import date
import re
os.environ['LANG'] = 'C.UTF-8'

categories = [
    'cs.MM',
    'cs.DC',
]
each_category_max_paper_num = 100

file_name = "./today_arxiv.txt"
temp_dir = "./tmp"

def extract_url(input_str):
    # Find the start and end positions of the paper title and link
    link_start = input_str.find("https://arxiv.org/abs/")
    link_end = input_str.find(" title", link_start)
    paper_link = input_str[link_start:link_end]
    output_str = f"Paper: {paper_link}"
    return output_str

# check if the temp dir exists
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
else:
    # remove all files in the temp dir
    for file in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, file))

# check if the file exists and remove it
if os.path.exists(file_name):
    os.remove(file_name)


for category in categories:
    url = f'https://arxiv.org/list/{category}/pastweek?skip=0&show={each_category_max_paper_num}'
    response = requests.get(url)

    with open(f'{temp_dir}/{category}_raw.txt', 'w') as file:
        file.write(response.text)
    with open(f'{temp_dir}/{category}_raw.txt', 'r') as input_file, open(f'{temp_dir}/{category}.txt', 'w') as output_file:
        for line in input_file:
            if '<h3>' in line or '<span class="descriptor">Title:</span>' in line or 'href="/abs/' in line:
                output_file.write(line)
    with open(f'{temp_dir}/{category}.txt', 'r') as file:
        content = file.read()

    urls = re.findall(r'href="(\/abs\/.*?)"', content)
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if '<h3>' in line:
            lines[i] = line.replace('<h3>', '\n\n========================================\n')\
                        .replace('</h3>', '\n========================================')
        elif '<span class="descriptor">Title:</span>' in line:
            lines[i] = line.replace('<span class="descriptor">Title:</span> ', '\tTitle: ')
        elif 'href="/abs/' in line:
            if len(urls) >= 0:
                url = urls.pop(0)
                lines[i] = line.replace(f'href="{url}"', f'https://arxiv.org{url}')
                lines[i] = extract_url(lines[i])
    content = '\n'.join(lines)
    with open(f'{temp_dir}/{category}.txt', 'w') as file:
        file.write(content)

    with open(file_name, 'a') as file:
        file.write(
            "\n\n\n===============================================================================\n")
        file.write(f"\t\t\t[Category: {category}]  [" + str(date.today()) + "]\n")
        file.write("===============================================================================\n")
        with open(f'{temp_dir}/{category}.txt', 'r') as category_file:
            for line in list(category_file):
                file.write(line)

        i = i + 1

import os
os.system(f"less {file_name}")
