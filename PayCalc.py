# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 21:37:21 2017

@author: bmitchell
"""

def pay(wage, hours):
    ## Calculate weekly pay with time & half overtime
    if hours <=40:
        amount = wage * hours
    else:
        amount = (wage * 40) +((1.5) * wage * (hours - 40))
    return amount
    
## Calculate a person's weekly pay
    
hourlyWage = eval(input("Enter the hourly wage: "))
hoursWorked = eval(input("Enter the hours worked: "))
print("Earnings: ${0:,.2f}".format(pay(hourlyWage, hoursWorked)))
    