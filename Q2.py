# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:43:20 2017

@author: bmitchell
"""

"""
Write a program that reads the following information and prints a payroll 
statement:
Employee’s name (e.g., Smith)
Number of hours worked in a week (e.g., 10) 
Hourly pay rate (e.g., 9.75)
Federal tax withholding rate (e.g., 20%) 
State tax withholding rate (e.g., 9%)
"""

#Intake required information
Employee_Name = input('Input the employee name: ')
Hours_Worked = eval(input('Input number of hours worked this week: '))
Hourly_PayRate = eval(input('Input employee hourly pay rate($): '))
Fed_Tax_Withhold = eval(input('Input Federal Tax Withholding rate(%): '))
State_Tax_Withhold = eval(input('Input State Tax Withholding rate(%): '))

#Convert the rates to fractions
Fed_Tax_Withhold = Fed_Tax_Withhold / 100
State_Tax_Withhold = State_Tax_Withhold / 100

#Compute weekly earnings and amounts withheld.
earnings = Hours_Worked * Hourly_PayRate
fedwith = earnings * Fed_Tax_Withhold
statewith = earnings * State_Tax_Withhold

#Print the payroll statement
print('\n')
print('****** SUMMARY PAYROLL STATEMENT ******')
print('Employee Name: ', Employee_Name)
print('Hours Worked This Week: ', Hours_Worked)
print('Hourly Pay Rate: $', Hourly_PayRate)
print('Federal Tax Withholding Rate: ', Fed_Tax_Withhold)
print('State Tax Withholding Rate: ', State_Tax_Withhold)
print('Weekly Earnings: ${0:,.2f} '.format(earnings))
print('Federal Tax Withheld: ${0:.2f}'.format(fedwith))
print('State Taxes Withheld: ${0:.2f}'.format(statewith))