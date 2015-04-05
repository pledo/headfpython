#!/usr/bin/env python3
import os
import re

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top(self, times_run=0):
        return(sorted(set([sanitize(t) for t in self.times]))[0:times_run])

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, list_of_times):
        self.times.extend(list_of_times)


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
vera.add_time('1.31')
print(vera.top())
vera.add_times(['2.22', '1-21', '2:22'])
print(vera.top(3))
