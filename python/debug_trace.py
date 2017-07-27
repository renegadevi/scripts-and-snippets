#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


def debug_trace(self, frame, event, arg, indent=[0]):
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

    return self.debug_trace

if __name__ == '__main__':
    sys.settrace(self.debug_trace)
