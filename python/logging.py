#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple logging

Debug levels
  10 - DEBUG
  20 - INFO
  30 - WARNING
  40 - ERROR
  50 - CRITICAL
"""

#logger = logging.getLogger(__name__) # __name__ will generate the module name
logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='logging.log', mode='w')
handler.setFormatter(logging.Formatter('[%(asctime)s] [%(name)s] (%(levelname)s) %(message)s'))
logger.addHandler(handler)

# With debug on, it will output logging to terminal
if debug == True:
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter('[%(asctime)s] [%(name)s] (%(levelname)s) %(message)s')
    logger.addHandler(handler)

# example
logger.warning('my warning message')

# Then on each submodule, you can use this
# logger = logging.getLogger('mylogger')