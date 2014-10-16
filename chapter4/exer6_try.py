#!/usr/sbin/env python3

try:
	with open('its.txt', "w") as data:
		print(data.readline(),end='')

except IOError as err:
	print('File error: ' + str(err))

