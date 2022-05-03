#!/usr/local/bin/python3
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entry:
        print('DOWNLOADING CSV')
        data = entry.read().decode('latin1')
        print('DOWNLOADING COMPLETE')
        for cidade in csv.reader(data.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
