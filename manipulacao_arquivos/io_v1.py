#!/usr/local/bin/python3
file = open('people.csv')
data = file.read()
file.close()

for record in data.splitlines():
    print('Name: {}, Age: {}'.format(*record.split(',')))
