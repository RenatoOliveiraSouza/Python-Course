#!/usr/local/bin/python3
file = open('people.csv')
for record in file:
    print('Name: {}, Age: {}'.format(*record.split(',')))
file.close()
