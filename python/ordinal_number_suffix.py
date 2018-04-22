#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Function solution
Originally by Winston Ewert, Modified by Philip Andersen.
https://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers
"""
def ordinal_suffix(num):
    suffixes = {1:'st',2:'nd',3:'rd'}
    return 'th' if 10 <= num % 100 <= 20 else suffixes.get(num % 10, 'th')


# Example
for x in range(51):
    print(str(x) + " " + str(ordinal_suffix(x)))



""" Lambda solution based upon the function above """
ordinal = lambda num: str(num) + {1: 'st', 2: 'nd', 3: 'rd'}.get(10 <= num % 100 <= 20 and num or num % 10, 'th')
print([ordinal(num) for num in range(51)])
