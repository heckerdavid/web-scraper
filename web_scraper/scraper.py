import requests
from bs4 import BeautifulSoup
from requests.api import get

url = 'https://en.wikipedia.org/wiki/Fukushima_nuclear_disaster'


def get_citations_needed_count(url) -> int:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all(title='Wikipedia:Citation needed')
    total = 0

    for _ in results:
        total +=1

    return total


def get_citations_needed_report(url) -> str:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all(title='Wikipedia:Citation needed')

    parents = []
    for result in results:
        parents.append(result.parent.parent.parent.text)

    for parent in parents:
        print(parent)



print(get_citations_needed_count(url))
get_citations_needed_report(url)