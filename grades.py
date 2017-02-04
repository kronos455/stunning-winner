# -*- coding: utf-8 -*-
"""
Spyder Editor

Brandon Mitchell
Grades Program
"""

##Calculate average of grades
grades = [] #Create the variable grades and asssign it the empty list.
num = float(input("Enter the first grade: "))
grades.append(num)
num = float(input("Enter the second grade: "))
grades.append(num)
num = float(input("Enter the third grade: "))
grades.append(num)
num = float(input("Enter the fourth grade: "))
grades.append(num)
num = float(input("Enter the fifth grade: "))
grades.append(num)
minGrades = min(grades)
grades.remove(minGrades)
averageGrades = sum(grades) / len(grades)
print("Average Grade: {0:.2f}".format(averageGrades))




