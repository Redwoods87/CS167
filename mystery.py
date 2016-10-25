"""
Author username(s): johnsoam
Date: 10/24/16
Assignment/problem number: Exam 2
Assignment/problem title: Decoding code
"""

def commonChars (stringOne, stringTwo):
    """
    Finds the common characters at the beginnings of two strings.
    
    Parameters:
        stringOne: a string 
        stringTwo: a second string
    
    Returns: a string of characters identical to the matching characters at the beginnings of stringOne and stringTwo
    
    Preconditions: both parameters must be strings
    
    Postconditions: will return a single string, shorter than or equal to the length of the shorter input string, consisting of characters that appear at the beginnings of both strings    
    """
    
    endIndex = 0        # the index following the final matching character
    shortLen = min(len(stringOne), len(stringTwo))
    while endIndex < shortLen and stringOne[endIndex] == stringTwo[endIndex]:
        endIndex = endIndex + 1
    return stringOne[:endIndex]

if __name__ == "__main__":
    print(commonChars("apple","application"))