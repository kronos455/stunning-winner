# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:06:06 2017

@author: bmitchell
"""

x = 0 

def main():
    print(str(x) + ": function main")
    trivial ()
    print (str(x) + ": function main")
    
def trivial():
    global x
    x += 7 
    print(str(x) + ": function trivial")
    
main() 