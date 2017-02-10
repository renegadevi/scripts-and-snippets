#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def Fibonacci(num):
    """ Create a list from 0 to num """
    fib, values = lambda x: 1 if x <= 1 else fib(x-1) + fib(x-2), []
    for i in range(0, num):
        values.append(fib(i))
    return values

try:
    if len(sys.argv) > 1:
        print(Fibonacci(int(float(sys.argv[1]))))
except ValueError:
    exit("Use a valid number")
