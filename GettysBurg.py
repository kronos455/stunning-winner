# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:52:00 2017

@author: bmitchell
"""

def main():
    listOfWords = formListOfWords("Gettysburg.txt")
    freq = createFrequencyDictionary(listOfWords)
    displayWordCount(listOfWords, freq)
    displayMostCommonWords(freq)
    
def formListOfWords(filename):
    infile = open(filename)
    originalLine = infile.readline().lower()
    line = ""
    for ch in originalLine:
        if('a' <= ch <= 'z') or (ch == " "):
            line += ch
            
    listOfWords = line.split()
    return listOfWords
    
def createFrequencyDictionary(listOfWords):
    freq = {}
    for word in listOfWords:
        freq[word] = 0
    for word in listOfWords:
        freq[word] = freq[word] + 1
    return freq
    
def displayWordCount (listOfWords, freq):
    print("The Gettysburg Address contains ", len(listOfWords), "words.")
    print("the Gettysburg Address contains ", len(freq), "different words.")

def displayMostCommonWords(freq):
    print("The most common words and their frequencies are: ")
    listOfMostCommonWords = []
    for word in freq.keys():
        if freq[word] >= 6:
            listOfMostCommonWords.append((word, freq[word]))
        listOfMostCommonWords.sort(key=lambda x: x[1], reverse=True)
        for item in listOfMostCommonWords:
            print("   ", item[0] + ':', item[1])
            
main()