# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:31:18 2017

@author: bmitchell
"""

def main():
    infile = open("File1.txt", 'r')
    firstSet = {line.rstrip() + "\n" for line in infile}
    infile.close()
    infile = open("File2.txt", 'r')
    secondSet = {line.rstrip() + "\n" for line in infile}
    infile.close()
    
    outfile = open("Union.txt", 'w')
    outfile.writelines(firstSet.union(secondSet))
    outfile.close()
    outfile = open("Intersection.txt", 'w')
    outfile.writelines(firstSet.intersection(secondSet))
    outfile.close()
    outfile = open("Difference.txt", 'w')
    outfile.writelines(firstSet.difference(secondSet))
    outfile.close()
    
main()