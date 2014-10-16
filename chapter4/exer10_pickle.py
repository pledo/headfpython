#!/usr/sbin/env python3
from nester import print_lol
import pickle
"""Essa funcao pickle esta sendo usada prq no
	exercicio anterior nos gravamos as listar other e man
	nos arquivos, mas a aparencia ficou de lista
	o que he bem incoveniente para o caso
	entao usamos o pickle, pois ele mantem
	uma aparencia de texto mesmo
"""
man = []
other = []

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
