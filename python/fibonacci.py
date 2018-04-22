#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fibonacci = lambda x : 1 if x <= 1 else fibonacci(x-1) + fibonacci(x-2)
for i in range(0, 10):
    print(fibonacci(i))
