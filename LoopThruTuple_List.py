# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 20:52:36 2017

@author: bmitchell
"""

##Display months containing the letter 'r'.

months = ("January", "February", "March", "April", "May", 
          "June", "July", "August", "September", "October", 
          "November", "December")
          
for month in months:
    if 'r' in month.lower():
        print(month)