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


def get_all_player_data(tree):
    """String -> [ListOf String]
        Takes a parse tree for a basketball-reference advanced player stats page 
        and returns a table of player data for every player listed on that page"""
    players_tree = [player for player in tree.find_all('tr')[1:] if player['class']==['full_table']]
    return [get_player_data(p) for p in players_tree]


def get_player_data(player_tree):
    """String -> [ListOf String]
        Takes a parse tree for a specific player's entry in the basketball-reference 
        advanced player stats page and returns a list of data for that player.
        One frow per player. If a player has played for multiple teams, the TOT 
        entry is returned"""    
    return [p.text for p in player_tree]



#=====================
# action!


br_advanced_2024 = 'https://www.basketball-reference.com/leagues/NBA_2024_advanced.html'

page_parse_tree = parse(get_page(br_advanced_2024))

headers = get_headers(page_parse_tree)

data = get_all_player_data(page_parse_tree)

print(data)