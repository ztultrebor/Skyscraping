"""
This script extracts player data from basketball-reference. 
It works for any player data page for any season, such as totals, advanced, etc.
Data is returned in CSV tabular format.
User selects the URL and target filename.
"""


import requests
from bs4 import BeautifulSoup
import csv



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
        Takes a parse tree from any basketball-reference player stats page 
        and returns a list of column headers for that page"""
    return get_row(tree.tr.find_all('th'))


def get_all_player_data(tree):
    """String -> [ListOf String]
        Takes a parse tree for any basketball-reference player stats page 
        and returns a table of player data for every player listed on that page.
        One row per player. If a player has played for multiple teams, the TOT 
        entry is returned"""  
    players_tree = [player for player in tree.find_all('tr')[1:] if player['class']==['full_table']]
    return [get_row(p) for p in players_tree]


def get_row(row_tree):
    """String -> [ListOf String]
        Takes a parse tree for an individual row (inc. the header row) of 
        an html/xml table in which the interesting data is stored as text entries, 
        and returns those text entries as a list"""    
    return [el.text for el in row_tree]


def export(url, filename='player_data.csv'):
    """String String -> None
        Takes a URL for any basketball-reference player stats page
        and generates a CSV file containing a table of player data 
        saved to the provided filename in the enclosing folder"""
    if filename[-4:] != '.csv':
        filename += '.csv'
    page_parse_tree = parse(get_page(url))
    headers = get_headers(page_parse_tree)
    data = get_all_player_data(page_parse_tree)
    with open(filename, 'w', newline='') as csvfile:
        transcription = csv.writer(csvfile, delimiter=',')
        transcription.writerow(headers)
        for row in data:
            transcription.writerow(row)



#=====================
# action!

bb_totals_2024 = 'https://www.basketball-reference.com/leagues/NBA_2024_totals.html'
bb_advanced_2024 = 'https://www.basketball-reference.com/leagues/NBA_2024_advanced.html'

export(bb_advanced_2024, "bb_advanced.csv")
export(bb_totals_2024, "bb_totals")