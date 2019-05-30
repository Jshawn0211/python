#!/usr/bin/python3

import requests

r = requests.get('http://www.espn.com/mlb/stats/batting/_/year/2018/seasontype/2')
print(r.content)
