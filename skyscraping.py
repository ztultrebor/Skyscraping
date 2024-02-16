import requests
from bs4 import BeautifulSoup



#=========================
 # functions


def get_page(url):
    """String -> String
        Takes a web address and returns the page data of that web page"""
    return requests.get(url).text


def parse(page, parser='html.parser'):
    """String String -> String
        Takes a web page data string and a parser and
        returns the parse tree of that web page"""
    return BeautifulSoup(page, parser)


def get_headers(tree):
    """String -> [ListOf String]
        Takes a parse tree for a basketball-reference advanced player stats page 
        and returns a list of column headers for that page"""
    return [s.text for s in tree.tr.find_all('th')]



#=====================
# action!


br_advanced_2024 = 'https://www.basketball-reference.com/leagues/NBA_2024_advanced.html'

page_parse_tree = parse(get_page(br_advanced_2024))

headers = get_headers(page_parse_tree)

print(headers)