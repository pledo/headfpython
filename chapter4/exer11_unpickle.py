#!/usr/sbin/env python3
from nester import print_lol
import pickle
"""
Aqui iremos ver como visualizar
,recuperar as informacoes que foram
pickladas
"""
man = []
other = []
new_man = []

try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()

except IOError:
	print('The datafile is missing!')

try:
	with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
		pickle.dump(man, man_file)
		pickle.dump(other, other_file)
	
except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))

try:
	with open('man_data.txt', 'rb') as man_file:#, open('other_data.txt', 'wb') as other_file:
		new_man = pickle.load(man_file)
#		pickle.dump(other, other_file)
	
except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))

print_lol(new_man)
