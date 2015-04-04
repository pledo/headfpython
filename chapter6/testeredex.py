#!/usr/bin/env python3
import re
import os

lista = os.listdir('/home/paulo/estudos/python/headfpython/chapter6')
#os.chdir(work_dir)

##lista = ['exer3_dicionarios_all_meujeito.py', \
#         'meu_jeito_exer4_class.py', 'james2.txt', \
#         'mikey2.txt', 'testeredex.py', 'sarah2.txt',\
#         'exer1_rearrangemagnets.py', 'julie2.txt', 'exer2_dicionarios_meujeito.py', 'exer4_class.py']
###
def get_filenames(filename):
    lista_files = []
    for item in lista:
        m = re.search("(.*txt$)", item)
        if m:
            lista_files.append(item)
    print(lista_files)

get_filenames(os.listdir('/home/paulo/estudos/python/headfpython/chapter6'))
