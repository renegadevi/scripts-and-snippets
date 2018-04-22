#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def debug_trace(frame, event, arg, indent=[0]):
    """ Debug trace """

    # Terminal colors
    green, red, clear = '\033[92m', '\033[91m', '\033[0m'

    # Calling function
    if event == "call":
        indent[0] += 2
        print(green + "->", " " * indent[0], frame.f_code.co_name, clear)

    # Exiting function
    elif event == "return":
        print(red + "<-", " " * indent[0], frame.f_code.co_name, clear)
        indent[0] -= 2

    return debug_trace

if __name__ == '__main__':
    sys.settrace(debug_trace)
