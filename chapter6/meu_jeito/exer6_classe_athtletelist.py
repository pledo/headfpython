#!/usr/bin/env python3
import os
import re

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top(self, times_run):
        return(sorted(set([sanitize(t) for t in self]))[0:times_run])

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'

    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

def get_filenames(filenames):
    athlete_files = []
    for any_file in filenames:
        files = re.search("(.*txt$)", any_file)
        if files:
            athlete_files.append(any_file)
    return(athlete_files)

def get_athlet_name(lista_arquivos_atletas):
    nomes_atletas = []
    for names in lista_arquivos_atletas:
        (name, extension) = names.split('.')
        nomes_atletas.append(name.strip('2'))
    return(nomes_atletas)

files_work_dir = os.listdir('/home/paulo/estudos/python/headfpython/chapter6')
athlet_name_files = (get_filenames(files_work_dir))
athlete_name = get_athlet_name(athlet_name_files)

for nomo, arquivo in zip(athlete_name, athlet_name_files):
    nomo = get_coach_data(arquivo)
    print(nomo.name + "'s fastest times are: " + str(nomo.top(3)))
