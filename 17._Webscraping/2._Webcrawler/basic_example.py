from bs4 import BeautifulSoup
import requests
import re

WIKI_BASE_URL = "https://en.wikipedia.org"
content = requests.get(WIKI_BASE_URL).content

parsed_content = BeautifulSoup(content, features="lxml")

# Rules for internal Wikipedia links:
# They reside within the div with the id set to bodyContent
# The URLs do not contain colons
# The URLs begin with /wiki/

internal_links = parsed_content.find('div', { "id": "bodyContent" }).find_all('a', href=re.compile("^(/wiki/)((?!:).)*$"))

for link in internal_links:
    print(WIKI_BASE_URL + link['href'])