# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:14:19 2015

@author: SSunshine
"""

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'