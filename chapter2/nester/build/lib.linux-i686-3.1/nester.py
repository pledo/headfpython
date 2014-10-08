#!/usr/bin/env python3
"""Capitulo 2 """

def print_lol(movies, level=0):
	"""printando os itens da lista"""
	for each_item in movies:
		if isinstance(each_item, list):
			print_lol(each_item, level+1)
		else:
			for tab_stop in range(level):
				print("\t", end=' ')		
			print(each_item)		
