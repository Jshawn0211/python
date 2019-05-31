#!/usr/bin/python3

import pandas as pd

##This is the actual package that you just downloaded
import DFS_NBA_Team_Builder 
from DFS_NBA_Team_Builder import DK_TeamBuilder

dfr=pd.read_csv("DKSalaries.csv")#This is the example file from GitHub

samplepercent= .20

dkteams =2

playerusage, dkupload= DFS_NBA_Team_Builder.DK_TeamBuilder.DK_TeamBuildermod(dfr,dkteams,samplepercent)


