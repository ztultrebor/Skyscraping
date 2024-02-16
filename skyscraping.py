import requests
from bs4 import BeautifulSoup


def get_page(url, parser):
    """String String -> String
        Takes a web address and a parser and returns the parse tree of that web page"""
    content = requests.get(url).text
    return BeautifulSoup(content, parser)



br_advanced_2024 = 'https://www.basketball-reference.com/leagues/NBA_2024_advanced.html'

print(get_page(br_advanced_2024, "html.parser"))