#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import environ
print(''.join(["%30s : %s\n" % (key,environ[key]) for key in environ.keys()]))
