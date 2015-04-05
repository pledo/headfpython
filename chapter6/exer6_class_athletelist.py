#!/usr/bin/env python3

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top(self, times_run=0):
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

#Testes unitarios

vera = Athlete('Vera Vi')
vera.append('1.31')
print(vera.top(3))
vera.add_times(['2.22', '1-21', '2:22'])
print(vera.top(3))
