#!/usr/local/bin/python3

try:
    file = open('people.csv')

    for record in file:
        print('Name: {}, Age: {}'.format(*record.strip().split(',')))
except IndexError:
    pass
finally:
    print('FINALLY')
    file.close()

if file.closed:
    print('FILE ALREADY CLOSE')
