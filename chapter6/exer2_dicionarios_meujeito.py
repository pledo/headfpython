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
		return(data.strip().split(','))

	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

sarah = get_coach_data('sarah2.txt')

athlets = {}
athlets['Name'] = sarah.pop(0)
athlets['Age'] = sarah.pop(0)
athlets['Times'] = sarah

print(athlets['Name'] + "fastest times are: " + \
      str(sorted(set([sanitize(t) for t in athlets['Times']]))[0:3]))
