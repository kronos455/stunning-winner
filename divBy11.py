# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 20:21:59 2017

@author: bmitchell
"""

## FInd integers divisible by 11.
list1 = ["one", 23, 17.5, "two", 33, 22.1, 242, "three"]
i = 0
foundFlag = False
while i < len(list1):
    x = list1[i]
    i += 1
    if not isinstance(x, int):
        continue
    if x % 11 == 0:
        foundFlag = True
        print(x, "is the first int that is divisible by 11.")
        break
    if not foundFlag:
        print("There is no int in the list that is divisible by 11.")
        
