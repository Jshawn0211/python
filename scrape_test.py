#!/usr/bin/python3

# A simple script to scrape a web site and get some info about todays MLB games

#import the modules we are going to need
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.rotowire.com/baseball/daily-lineups.php')

print(response.text)
print(response.headers)
