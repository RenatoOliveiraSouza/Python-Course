#!/usr/local/bin/python3

with open('people.csv') as file:
    with open('people.txt', 'w') as exit:
        for record in file:
            person = record.strip().split(',')
            print('Name: {}, Age: {}'.format(*person), file=exit)

if file.closed:
    print('FILE ALREADY CLOSE')