#!/usr/bin/python3

from pydfs_lineup_optimizer import Site, Sport, get_optimizer

optimizer = get_optimizer(Site.DRAFTKINGS, Sport.BASEBALL)
optimizer.load_players_from_csv("DKSalaries.csv")
for lineup in optimizer.optimize(2):
    print(lineup)
