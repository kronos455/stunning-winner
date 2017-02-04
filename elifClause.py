# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 19:09:02 2017

@author: bmitchell
"""
##Determine the larger of two numbers.
#Obtain the two numbers from the user.
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
#Determine & display the larger value.
if num1 > num2:
    print("The larger value is", str(num1) + ".")
elif num2 > num1:
    print("The larger value is", str(num2) + ".")
else:
    print("The two values are equal.")