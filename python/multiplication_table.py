#!/usr/bin/env python3

""" Multiplication table.
    A simple practice every programmer should know how to do, basic stuff here.
"""

for row in range(1,11):
    for column in range(1,11):
        print(row * column, end='\t')
    print("\n")
