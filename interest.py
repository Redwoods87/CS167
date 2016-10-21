"""
Author username(s): Andrew Johnson & Stuart Ashford
Date: September 11th 2016
Assignment/problem number: 3.1
Assignment/problem title: Compound Interest
"""

import math

print("Welcome to your Compound Interest Calculator!")
	
p = float(input ("Please enter the principal amount (initial investment): "))
r = float(input ("Please enter the annual nominal interest (as a decimal): "))

cont = input("Will you be compounding continuously? [Y/N]")

if cont == str("N") or cont == str("n"):

	n = float(input ("Please enter the number of times the interest is compounded per year: "))
	t = float(input ("Please enter the number of years since initial investment: "))

	finalBalance = p * ((1 + (r / n)) ** (n * t))

else:

	t = float(input ("Please enter the number of years since initial investment: "))

	finalBalance = p * (math.e ** (r * t))

finalBalance = finalBalance * 100
finalBalance = round(finalBalance)
finalBalance = finalBalance / 100

print("Your final balance with interest is $" + str(finalBalance))


