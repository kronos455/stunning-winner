# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:22:45 2017

@author: bmitchell
"""

def main():
    words = ["nudge", "nudge", "wink", "wink"]
    terms =  set(words)
    print(terms)
    words = list(terms)
    print(words)
    
    terms.add("nudge")
    terms.add("maybe")
    print(terms)
    
    terms.discard("nudge")
    print(terms)
    words = tuple(terms)
    
    print(words)
    
main()
    