# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 03:26:17 2017

@author: bmitchell
"""

def pyramid(rows=8):
    for i in range(rows):
        print ' '*(rows-i-1) + '*'*(2*i+1)
    
pyramid()
    