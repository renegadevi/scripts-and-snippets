#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Python Fire

    Automatically generating command line interfaces (CLIs) from absolutely any
    Python object.

    https://github.com/google/python-fire
    Apache License, Version 2.0
"""

"""
$ ./example.py hello
Hello world!

$ ./example.py hello David
Hello David!

$ ./example.py hello --name=Google
Hello Google!
"""

import fire

class Example(object):
  def hello(self, name='world'):
    """Says hello to the specified name."""
    return 'Hello {name}!'.format(name=name)

def main():
  fire.Fire(Example)

if __name__ == '__main__':
  main()


