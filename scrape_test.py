# A simple script to scrape a web site and get some info about todays MLB games

#import the modules we are going to need
import requests
from bs4 import BeautifulSoup

# We will start by scraping the daily matchups from http://www.baseballpress.com/lineups
# First we set our website url
url = "http://www.baseballpress.com/lineups"

# Read the source code of our webpage and create a BeautifulSoup Object so we can 
# parse it and pull the data we want
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

print(soup)
