#!/usr/bin/env python3
# -*- enconding: utf-8 -*-

import json, pprint

with open('file.json') as data:
    pprint.pprint(json.load(data))
