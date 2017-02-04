# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 21:03:19 2017

@author: bmitchell
"""

## F to C
def fahrenheitToCelsius(t):
    ## Convert temp
    convertedTemp = (5/9) * (t -32)
    return convertedTemp
    
fahrenheitTemp = eval(input("Enter a temp in F: "))
celsiusTemp = fahrenheitToCelsius(fahrenheitTemp)
print("Celsius equivalent: ", celsiusTemp, "degrees.")