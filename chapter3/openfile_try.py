#!/usr/bin/env python3
""" Script do capitulo 3"""
import os
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
		    if not each_line.find(':') == -1:
		    	(role, line_spoken) = each_line.split(':', 1)
		    	print(role, end=' ')
		    	print(' said: ', end=' ')
		    	print(line_spoken, end=' ')
		except ValueError:
			pass

	data.close()
excepti IOError:
	print('The data file is missing!')