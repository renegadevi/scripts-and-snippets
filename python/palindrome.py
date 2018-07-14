#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def palindrome(value:str) -> bool:
    """ Returns true if value/string is a palindrome."""
    return str(value) == str(value)[::-1]

