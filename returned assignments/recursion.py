# palindrome
# 1/1 Correctness: Ignores spaces
# 1/1 Correctness: Ignores punctuation
# 1/1 Correctness: Matches capital and lower-case letters
# 0/1 Approach:    Uses a purely recursive approach (no iteration)
# 
# licensePlates
# 3/3 Correctness: Produces all combinations of letters before numbers
# 1/1 Approach:    Uses passwords function as a pattern and/or helper
# 
# 1/1 Style and comments 
# 
# GRADE: 8/8
"""
Author username(s): johnsoam
Date: 11/29/16
Assignment/problem number: Homework 16
Assignment/problem title: Recursion
"""

    
def palindrome(a_string):
    """
    Determines if a string is a palindrome.  (Adapted from Jessen Havill's "Discovering Computer Science" pg. 493.) Excludes non-letter characters and spaces.
    
    Parameters:
        a_string: a string 
    
    Returns: Boolean True or False, will evaluate only the characters that are letters in the string.
    """
     
    if len(a_string) <= 1:
        return True
    
    frontIndex = 0
    backIndex = -1
    
        
    while not ord("a") <= ord(a_string[frontIndex]) <= ord("z") and not ord("A") <= ord(a_string[frontIndex]) <= ord("Z"):
        frontIndex += 1         #if not a letter, skip index
     
    while not ord("a") <= ord(a_string[backIndex]) <= ord("z") and not ord("A") <= ord(a_string[backIndex]) <= ord("Z"):
        backIndex -= 1          #if not a letter, skip index

            
    frontChar = a_string[frontIndex]
    backChar = a_string[backIndex]

    ordDifference = ord("a") - ord("A")     #for making chars all lowercase

    if ord("A") <= ord(frontChar) <= ord("Z"):      #if front upper, maker lower
        frontChar = chr(ord(frontChar) + ordDifference)
        
    if ord("A") <= ord(backChar) <= ord("Z"):       #if back upper, make lower
        backChar = chr(ord(backChar) + ordDifference)    
    
    return frontChar == backChar and palindrome(a_string[frontIndex+1:backIndex])

def licensePlates(length, letters, numbers):
    """
    Generates a list of all possible license plates beginning with a series of letters followed by an equal number of numbers.
    
    Parameters:
        length: the number of letters and the number of numbers in each plate, an integer
        letters: the possible letters as a string
        numbers: the possible numbers as a string
    
    Returns a list containing all possible license plates as individual strings.
    """  
    if length == 0:
        return [""]
    
    shorter = licensePlates(length - 1, letters, numbers)
    
    platesList = []
    for shorterPlate in shorter:
        for letter in letters:
            for number in numbers:
                platesList.append(letter + shorterPlate + number)
    return platesList

def test():
    """
    Tests palindrom and stringToLetters functions.
    
    Returns None.
    """
    #common
    assert stringToLetters("i am now going") == "iamnowgoing"
    assert palindrome("Was it a car or a cat I saw?") == True
    assert palindrome("Rise to vote, sir!") == True
    assert palindrome("A man, a plan, a canal -- Panama!") == True
    assert palindrome("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.") == True
    assert palindrome("apple") == False
    assert palindrome("tacocat") == True
    #corner
    assert palindrome("i am sam") == False
    assert palindrome("123taco987cat") == True
    #edge
    assert palindrome("") == True
    assert palindrome("1234ABA1234") == True
    
    print("All tests have passed!")

def main():
    test()
    print (licensePlates(2, "XY", "12"))
        
#if __name__ == "__main__":
#     main()
    
    
    
    
"""
Unused code from first turn-in:

def stringToLetters(string):
    Creates a new string with only the letters and converting all letters to lower-case.
    
    Parameters:
        string: a string to convert
    
    Returns a new string with only lower case letters and no spaces.
    
    newString = ""
    for i in range (len(string)):
        char = string[i]
        if 97 <= ord(char) and ord(char) <= 122:    # if lowercase add to newString
            newString = newString + char
        elif 65 <= ord(char) and ord(char) <= 90:   # if uppercase make lowercase
            lowerChar = chr(ord(char) + 32)         
            newString = newString + lowerChar
    return newString                                # and if other char, disregard

"""

import sys
import linecache

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.\n\t".format(linenum))
        msg += linecache.getline(__file__, linenum)

    print(msg)

test( palindrome("hannah") )
test( palindrome("HaNnAh") )
test( not palindrome("hannah banana") )
test( palindrome("was it a car or a cat i saw") )
test( palindrome("hannah!") )
test( palindrome("Hannah!") )
test( palindrome("Was it a car or a cat I saw?") )
test( palindrome("Rise to vote, sir!") )
test( palindrome("A man, a plan, a canal -- Panama!") )
test( palindrome("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.") )
test( not palindrome("Hello world!") )
test( not palindrome("Hello H!") )
input('Press ENTER to continue')

lp = licensePlates(2, 'AT', '10') 
print(lp)
test(len(lp) == 2**4)
input('Press ENTER to continue')

lp = licensePlates(2, 'ABC', '123') 
print(lp)
test(len(lp) == 3**4)
input('Press ENTER to continue')

lp = licensePlates(3, 'ABC', '123') 
print(lp)
test(len(lp) == 3**6)
