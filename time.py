"""
Author username(s): pylescj ; johnsoam
Date: September 7, 2016
Assignment/problem number: Homework Assignment 2/Problem 2
Assignment/problem title: Time Conversion
"""
print("Welcome to Time Converter.")
originalTime=float(input("Please enter the time in milliseconds: "))
secondsTens=int(originalTime//10000%6)
secondsOnes=int(originalTime%10000)/1000
minutes=int((originalTime//60000))
print("Time: "+str(minutes)+":"+str(secondsTens)+str(secondsOnes))
