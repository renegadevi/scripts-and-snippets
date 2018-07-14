#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reversed_words(sentence:str) -> str:
    return ' '.join(word[::-1] for word in sentence.split())
