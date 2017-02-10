# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:52:54 2017

@author: bmitchell
"""

def pyramid(rows=8):
    for i in range(rows):
        print(' '*(rows-i+6) + '*'*(2*i+6)
        )

pyramid()