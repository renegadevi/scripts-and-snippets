#!/usr/bin/env python
# -*- encoding: utf-8 -*-

def hex_to_rgb(value):
    """ Converts Hex color value #000000 into rgb(0, 0, 0)"""
    return tuple(int(str(value.lstrip('#'))[i:i+2], 16) for i in (0, 2, 4))