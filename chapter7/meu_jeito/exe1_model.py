#!/usr/bin/env python3
import pickle
import sys
import os
import re
#from athleteList import AthleteList

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

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

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        print('cada arquivo: ' + str(each_file))
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put_and_store): ' + str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store): ' + str(ioerr))
    return(all_athletes)

def get_filenames(filenames):
    athlete_files = []
    for any_file in filenames:
        files = re.search("(.*txt$)", any_file)
        if files:
            athlete_files.append(any_file)
    return(athlete_files)


def main():
    files_work_dir = os.listdir('/home/paulo/estudos/python/headfpython/chapter7')
    the_files = (get_filenames(files_work_dir))
    print(the_files)
    data = put_to_store(the_files)
    data_copy = get_from_store()
    for each_athlete in data_copy:
        print(data_copy[each_athlete].name)
    #print(data)


sys.exit(main())
