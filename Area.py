# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 19:48:31 2017

@author: bmitchell
"""

def main():
    areasAsStrings = extractField("UN.txt", 4)
    areas = [eval(num) for num in areasAsStrings]
    displaySomeStatistics(areas)
    
def extractField(fileName, n):
    infile = open(fileName, 'r')
    return [line.rstrip().split(',')[n-1] for line in infile]

def displaySomeStatistics(listOfNumbers)
    average = sum(listOfNumbers)/len(listOfNumbers)
    median = caluculateMedian(listOfNumbers)
    standardDeviation = calculateStandardDeviation(listOfNumbers, average)
    print("Average area: {0:,.2f} square miles".format(average) )
    print("Median area: {0:,d} squarre miles".format(median))
    print("Standard deviation: {0:,.2f} square miles".format(standardDeviation))
    
def calculateMedia(listOfNumbers):
    listOfNumbers.sort()
    if len(listOfNumbers) % 2 == 1:
        median = listOfNumbers[int(len(listOfNumbers) / 2)]
    else:
        m = int(len(listOfNumbers)/2)
        median = (listOfNumbers[m] + listOfNumbers[m + 1])
    return median
    
def calculateStandardDeviation(listOfNumbers, average):
    m = average
    n = len(listOfNumbers)
    listOfSquaresOfDeviations = [0] * n
    