"""
Author username(s): pylescj ; johnsoam
Date: September 7, 2016
Assignment/problem number: Homework Assignment 2/Problem 1
Assignment/problem title: Miles Per Gallon
"""
print("Welcome to the Mileage Calculator!")
start=float(input("What was the vehicle's starting mileage? "))
finish=float(input("What was the vehicle's ending mileage? "))
gas=float(input("How many gallons of fuel were used? "))
mpg=round(((finish-start)/gas)*1000)/1000
print("Your gas mileage was "+str(mpg)+" miles per gallon.")
if mpg<25:
	print("Your gas mileage sucks!")
if mpg>=25 and mpg<35:
	print("Your gas mileage is good.")
if mpg>=35:
	print("Your gas mileage is great! Keep it up!")
