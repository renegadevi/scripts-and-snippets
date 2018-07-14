#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
import json

def csv_to_json(filename:str) -> str:
    """ Convert CSV file to JSON data """
    if filename.endswith('csv'):
        return json.dumps(list(csv.reader(open(filename))))
    raise ValueError('No CSV file specified')



def main():
    """ Example as a terminal script;

    - Print it in terminal:
    'python3 csv_to_python.py companies.csv'

    - Save it to a json file
    'python3 csv_to_python.py companies.csv >> companies.json'
    """
    try:
        print(csv_to_json(sys.argv[1]))
    except ValueError as e:
        exit(e)

if __name__ == "__main__":
    main()
