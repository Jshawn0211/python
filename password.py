#!/usr/bin/python3

import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
numofpas = input('Number of password?')
numofpas = int(numofpas)

length = input('Password length?')
length = int(length)

for p in range(numofpas):
	password = ' '
	for c in range(length):
		password  += random.choice(chars)

	print(password)

