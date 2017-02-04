# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 19:55:34 2017

@author: bmitchell
"""

## Find the minimum, maximum, and average of a sequence of numbers.
count = 0 # Number of nonnegative numbers input
total = 0 # Sum of the nonnegative numbers input.

#Obtain numbers and determin count, min, and max.

print("(Enter -1 to terminate entering numbers.)")
num = int(input("Enter a nonnegative number: "))

min = num
max = num

while num != -1:
    count += 1
    total += num
    if num < min:
        min = num
    if num > max:
        max = num
    num = eval(input("Enter a nonnegative number: "))
if count > 0:
    print("Minimum:", min)
    print("Maximum:", max)
    print("Sum:", total)
    print("Count:", count)
    print("Average:", total / count)
else:
    print("No nonnegative numbers were entered.")