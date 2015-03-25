#!/usr/bin/env python3


file_list = ['james.txt', 'julie.txt', 'mikey.txt', 'sarah.txt']

def sanitize(time_string):
    """ Funcao que padroniza os separadores"""
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)



def get_coach_data(filename):
    try:
        with open(filename) as namef:
            data = namef.readline()
        result = data.strip().split(',')
        clean_name = [sanitize(each_t) for each_t in result]
        return(sorted(set(clean_name))[0:3])

    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

for players in file_list:
    print(get_coach_data(players))

