# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:05:11 2017

@author: Brandon Mithell blm150430
Assignment 1, Q4
"""
"""
Write a program that reads an integer and displays all its smallest factors, 
also known as prime factors. For example, if the input integer is 120, the 
output should be as follows: 2, 2, 2, 3, 5.
"""

#Import the necessary packages for computation
import numpy as np
import time 

def prime_factors(n):
    i = 2  #set the divsor
    factors = [] #create empty list
    while i * i <= n: #while loop to determine prime factors, run while divsor squared is less than the integer
        if n % i: #This increments the divsor if there n % i produces a number other than zero
            i += 1
        else: #divides by divsor, appends factor i
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n) #appends factor last n
    return factors
    
    
    
    
def main():
    #Prompt user to input a number or generate a number;
    choice = eval(input('Type 1 to generate a number or type 2 to enter a number: '))
    if choice == 1:
        user_number = np.random.randint(0, 999999999)
    else:
        user_number = eval(input('Type a number to find its Prime Factors: '))
    #Show user their number
    print('Your number is: ', user_number) 
    #Wait 3.5 seconds
    time.sleep(3.5)
    #Show user prime factors
    print(prime_factors(user_number))
    
main()