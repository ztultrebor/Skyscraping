import requests
from bs4 import BeautifulSoup



#=========================
 # functions


def get_page(url):
    """String -> String
        Takes a web address and a parser and returns the parse tree of that web page"""
    return requests.get(url).text


def parse(page, parser='html.parser'):
    """String String -> String
        Takes a web address and a parser and returns the parse tree of that web page"""    
    return BeautifulSoup(page, parser)



#=====================
# 


br_advanced_2024 = 'https://www.basketball-reference.com/leagues/NBA_2024_advanced.html'

page_parse_tree = parse(get_page(br_advanced_2024))

headers = [s.text for s in page_parse_tree.tr.find_all('th')]

print(headers)