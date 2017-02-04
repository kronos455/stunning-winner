# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:14:57 2017

@author: bmitchell
"""
names = ["Dennis Ritchie", "Alan Kay", "John Backus", "James Gosling"]
names.sort(key=lambda name: name.split()[0])
nameString = ", ".join(names)
print(nameString)
