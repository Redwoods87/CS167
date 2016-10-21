"""
Author username(s): johnsoam
Date: Sept. 26, 2016
CS 167 Exam 1 Take-Home Problem 1: Debugging
"""

#filename: tempconvert.py

degreesF = input("What is the temperature in degrees Fahrenheit? ")
degreesC = round((float(degreesF) - 32) * (5/9)) 
# degreesF must be converted to a float, otherwise "input" defines it as a string. 
# 5//9 should be 5/9; 5//9 always equals 0, which forces all outputs to be 0.

print("It is " + str(degreesC) + " degrees Celsius.")   
#degreesC needs to be converted to a string to work in a print function.
