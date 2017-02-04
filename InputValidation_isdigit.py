# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 19:20:58 2017

@author: bmitchell
"""

##Request two numbers and find their sum. 
##Validate the input.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

#Display sum if entries are valid. Otherwise, inform
#the user where invalid entries were made.

if num1.isdigit() and num2.isdigit():
    print("The sum is", str(eval(num1) + eval(num2)) + ".")
elif not num1.isdigit():
    if not num2.isdigit():
        print("Neither entry was a proper number.")
    else:
        print("The first entry was not a proper number.")
elif not num2.isdigit():
        print("The 2nd entry was not a proper number.")
else:
    print("Follow the directions.")