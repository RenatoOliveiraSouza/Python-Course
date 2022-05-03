#!/usr/local/bin/python3

with open('people.csv') as file:
    for record in file:
        print('Name: {}, Age: {}'.format(*record.strip().split(',')))

if file.closed:
    print('FILE ALREADY CLOSE')
