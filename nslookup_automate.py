#!/usr/bin/env python3

# This will be used to run nslookup on multiple IPs and return hostnames and pipe to a text file

import csv
import socket

f=open('ip_addresses.csv','r')
c=f.readlines()
for i in c :
     print (i)
f.close()
