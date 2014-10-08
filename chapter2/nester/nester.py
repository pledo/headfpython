#!/usr/bin/env python3
"""Capitulo 2 """

def print_lol(the_list, indent=False, level=0):
	"""printando os itens da lista"""
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1)
		else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end=' ')
            print(each_item)
