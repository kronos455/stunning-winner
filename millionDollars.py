# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 20:16:41 2017

@author: bmitchell
"""

numberOfYears = 0
balance = eval(input("Enter initial deposit: "))
while balance < 10000000:
    balance += .04 * balance
    numberOfYears +=1
print("In", numberOfYears, "years you will have a million dollars.")