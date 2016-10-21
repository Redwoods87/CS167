"""
Author username(s): johnsoam
Date: Sept. 26, 2016
CS 167 Exam 1 Take-Home Problem 2: Programming
"""

#filename: sumdigits.py

def sumDigits (number, numDigits):
    """
    Finds the sum of the individual digits in a number (ie. 123 = 1 + 2 + 3 = 6).
    
    Parameters:
        number: the number whose digits you want to add together.
        numDigits: the number of digits in the above number.
        
    Returns: the sum of the individual digits in the number.
        
    """
    sum = 0
    for i in range (numDigits):
        sum = sum + ((number // (10**i)) % 10)
    return sum
    
print (sumDigits (1234, 4))
        
        
        