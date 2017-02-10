# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:50:45 2017

@author: bmitchell
"""


def pyramid(rows=8):
    for i in range(rows):
        print(' '*(rows-i-1) + '*'*(2*i+1))
    
pyramid()