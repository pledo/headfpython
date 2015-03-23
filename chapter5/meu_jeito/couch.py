#!/usr/bin/env python3

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


file_list = ['james.txt', 'julie.txt', 'mikey.txt', 'sarah.txt']
name_list = []
list_result = []
for each_file in file_list:
    clean_name = []
    (name, extension) = each_file.split('.')
    name_list.append(name)
    with open(each_file) as namef:
        data = namef.readline()
    result = data.strip().split(',')
    for each_t in result:
        clean_name.append(sanitize(each_t))
    print(name, end='')
    print(sorted(clean_name))


