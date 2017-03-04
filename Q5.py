# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:37:52 2017

@author: Brandon Mitchell blm150430
Assignment 1, Q5
"""
#Import the packages necessary to complete computation.
import numpy as np
import time

#function for reversing the integer
def reverse(num):
    
    sign = -1 if num < 0 else 1  #remembers if the int was signed or not.
    num *= sign      #remove sign if present
    
    num = str(num)  #convert int to str
    list1 = list(num)  # convert str to list, list('234') returns ['2', '3', '4']  
    list1.reverse()  #reverse list
    num = "".join(list1)  #puts list back in to num variable
    num = int(num)  #convert num to int
    return sign*num  # return num with sign
    
def main():
    #Menu that gives the user the option of entering a number or having one generated for them.
    choice = eval(input('Type 1 to generate a number or type 2 to enter a number: '))
    if choice == 1:
        user_number = np.random.randint(0, 999999999)
    else:
        user_number = eval(input('Enter an integer: '))
    
    #Shows the user their number
    print('Your number is: ', user_number) 
    time.sleep(3.5)# adds a pause before printing next update
    print('Your number, reversed, is: ', reverse(user_number)) #calls reverse function recursively and prints
    
main()