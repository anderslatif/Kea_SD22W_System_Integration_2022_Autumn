from bs4 import BeautifulSoup
import requests
import re

WIKI_BASE_URL = "https://en.wikipedia.org"

pages = set()

def get_parsed_wiki_page(endpoint):
    if endpoint in pages:
        return

    content = requests.get(WIKI_BASE_URL + endpoint).content
    return BeautifulSoup(content, features="lxml")

def get_internal_links(parsed_content):
    if parsed_content is None:
        return

    anchor_tags = parsed_content.find('div', { "id": "bodyContent" }).find_all('a', href=re.compile("^(/wiki/)((?!:).)*$"))

    if anchor_tags is None:
        return

    for link in anchor_tags:
        if 'href' in link.attrs:
            pages.add(link.attrs['href'])

starting_page_links = get_internal_links(get_parsed_wiki_page("/wiki/Monty_Python"))


for _ in range(1000):
    for link in pages:        
        get_internal_links(get_parsed_wiki_page(link))



for page in pages:
    print(WIKI_BASE_URL + page)

print(len(pages))