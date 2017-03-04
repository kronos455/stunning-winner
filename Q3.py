# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:09:45 2017

@author: Brandon Mitchell blm150430
Assignment 1, Q3
"""

"""
Write a program that generates two integers under 100 and prompts the user 
to enter the sum of these two integers. The program then reports true if the 
answer is correct, false otherwise.
"""
#Import packages for computations
import numpy as np

first_no = np.random.randint(0, 99) #Create a variable with a random int
second_no = np.random.randint(0, 99) #Create a second variable with a random int
both = first_no + second_no #Add both variables to compare with user.
user_guess = 0


while user_guess != both: #loop to give user the chance to correct any mistake
    print('Type the answer: ', first_no, '+', second_no, '=') #Show user the problem
    user_guess = eval(input()) #solicit user input

    if user_guess == both:
        print('Not bad.') #Reward user for getting it right.
    else:
        print('Oooops! Try again.') #Encourage user to try again.
    
        
