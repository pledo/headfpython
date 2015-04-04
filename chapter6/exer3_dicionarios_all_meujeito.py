#!/usr/bin/env python3
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
    return({'Name': templ.pop(0)#,'DOB' : templ.pop(0),'Times' : str(sorted(set([sanitize(t) for t in templ['Times']]))[0:3])}) = data.strip().split(',')except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

files = ['james2.txt', 'julie2.txt', 'sarah2.txt', 'mikey2.txt']
athlets = {}
for file in files:
    athlets = get_coach_data(file)
    print(athlets['Name'] + "fastest times are: " + athlets['Times'])


