#!/usr/bin/python3

from sportsreference.nba.teams import Teams

teams = Teams()
for team in teams:
    print(team.name, team.abbreviation)

print("-------------------------------")

from datetime import datetime
from sportsreference.mlb.boxscore import Boxscores

games_today = Boxscores(datetime.today())
print(games_today.games)  # Prints a dictionary of all matchups for today

print("-------------------------------------")

from sportsreference.mlb.roster import Roster

dodgers = Roster('LAD')
for player in dodgers.players:
    # Prints the name of all players who played for the Dodgers in the most
    # recent season.
    print(player.name)
