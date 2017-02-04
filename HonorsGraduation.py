# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 19:15:29 2017

@author: bmitchell
"""

## Bestow graduation honors.
# Request grade point average.
gpa = eval(input("Enter your GPA: "))
#Determine if honors are warranted.
if gpa >= 3.9:
    honors = " summa cum laude."
elif gpa >= 3.6:
    honors = " magna cum laude."
elif gpa >= 3.3:
    honors = " cum laude."
else:
    honors = "."

print( "You graduated" + honors)