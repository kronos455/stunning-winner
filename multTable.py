# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 20:46:44 2017

@author: bmitchell
"""

## Display a multiplication table for the numbers from 1 through 5.
for m in range(1,6):
    for n in range(1,6):
        print(m, 'x', n, '=', m*n, "\t", end="")
    print()
    