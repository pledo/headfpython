#!/usr/bin/env python3
movies = ["The Holy Grail", 1975, "Terry Jones", 91, ["Graham Chapman", ["michel", "john", "terry"]]]

def print_lol(movies):
	"""printando os itens da lista"""
	for each_item in movies:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)		
print_lol(movies)

