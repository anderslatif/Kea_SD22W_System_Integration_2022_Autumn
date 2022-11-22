import requests
from bs4 import BeautifulSoup
from database.sqlite_dml import insert_project

html = requests.get('https://en.wikipedia.org/wiki/List_of_Monty_Python_projects').content
parsed_html = BeautifulSoup(html, features="lxml")

main_page_content = parsed_html.find('div', {'class': 'mw-parser-output'})

monty_python_projects = {}
project_type = None

for tag in main_page_content:
    if tag.name == "h2":
        project_type = tag.text.replace("[edit]", "")
        monty_python_projects[project_type] = []
    elif tag.name == "ul":
        for list_item in tag.find_all("li"):
            monty_python_projects[project_type].append(list_item.text)
    elif tag.name == "table":
        pass 


del monty_python_projects['Notes']
del monty_python_projects['References']
del monty_python_projects['Further reading']

from pprint import pprint
pprint(monty_python_projects)

for project_category in monty_python_projects:
    for project_name in monty_python_projects[project_category]:
        insert_project(project_category, project_name)