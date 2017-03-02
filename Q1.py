# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:14:15 2017
@author: Brandon Mitchell

Assignment 1, Q1
"""

"""
Body mass index (BMI) is a measure of health based on weight. It can be 
calculated by taking your weight in kilograms and dividing it by the square of 
your height in meters. Write a program that prompts the user to enter a weight 
in pounds and height in inches and displays the BMI. Note that one pound is 
0.45359237 kilograms and one inch is 0.0254 meters.
"""

weight_conv = 0.45359237
height_conv = 0.0254

#Print statements to guide user.
print('This program will measure your BMI.')
print('\n')
print('Body mass index (BMI) is measure of health based on weight.')
print('\n')
print('It can be calculated by taking your weight in kilograms and dividing it')
print('by the square of your height in meters.')
print('\n')


#Directions for user.
wgt_lbs = eval(input('Input your weight in pounds. Conversions occur automatically: '))
hgt_inch = eval(input('Input your height in inches. Conversions occur automatically: '))
print('\n')

#Convert user input units into metric
wgt_kg = weight_conv*wgt_lbs
hgt_mtr = height_conv*hgt_inch

#Compute user BMI
bmi = wgt_kg / (hgt_mtr ** 2)

#Display user BMI
print('Your BMI is: {0:.2f}'.format(bmi))


