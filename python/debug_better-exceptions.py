#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Pretty and more helpful exceptions in Python, automatically.
https://github.com/Qix-/better-exceptions (MIT-License)
$ pip install better_exceptions
"""


""" Code below should output this in terminal

$ python3 debug_better_exceptions.py

Traceback (most recent call last):
  File "debug_better_exceptions.py", line 26, in <module>
    shallow(bar, 15)
    │       └ 2
    └ <function shallow at 0x103e7f2f0>
  File "debug_better_exceptions.py", line 17, in shallow
    deep(a + b)
    │    │   └ 15
    │    └ 2
    └ <function deep at 0x104af5620>
  File "debug_better_exceptions.py", line 22, in deep
    assert val > 10 and foo == 60
           │            └ 52
           └ 17
AssertionError: assert val > 10 and foo == 60
"""
import better_exceptions
better_exceptions.MAX_LENGTH = None

better_exceptions.hook()
foo = 52

def shallow(a, b):
    deep(a + b)

def deep(val):
    global foo
    assert val > 10 and foo == 60

bar = foo - 50
shallow(bar, 15)
shallow(bar, 2)
