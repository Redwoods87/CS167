"""
Author username(s): johnsoam
Date: 11/28/16
Assignment/problem number: Homework 16
Assignment/problem title: Recursion
"""

def stringToLetters(string):
    """
    Creates a new string with only the letters and converting all letters to lower-case.
    
    Parameters:
        string: a string to convert
    
    Returns a new string with only lower case letters and no spaces.
    """
    
    newString = ""
    for i in range (len(string)):
        char = string[i]
        # print(ord(string[i]))
        if 97 <= ord(char) and ord(char) <= 122:
            newString = newString + char
        elif 65 <= ord(char) and ord(char) <= 90:
            lowerChar = chr(ord(char) + 32)
            # print(lowerChar)
            newString = newString + lowerChar
    return newString
        
def palindrome(a_string):
    """
    Determines if a string is a palindrome.  (Adapted from Jessen Havill's "Discovering Computer Science" pg. 493.) Excludes non-letter characters and spaces.
    
    Parameters:
        a_string: a string 
    
    Returns: Boolean True or False, will evaluate only the characters that are letters in the string.
    """
    modString = stringToLetters(a_string)    
    if len(modString) <= 1:
        return True
    return modString[0] == modString[-1] and palindrome (modString[1:-1])

def licensePlates(length, letters, numbers):
    """
    Generates a list of all possible license plates within certain parameters.
    
    Parameters:
        length: 
    
    """  
    
    if length == 0:
        return [""]
    
    shorter = licensePlates(length - 1, letters, numbers)
    
    platesList = []
    for letter in letters:
        for shorterPlate in shorter:
            platesList.append(letter + shorterPlate + number)

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
        
if __name__ == "__main__":
    main()


    
""" TRYING RECURSION
    if len(string) <= 0:
        newString = ""
        return newString
    char = string[0]
    newString = ""
    if 97 <= ord(char) <= 122:
        newString += char
    elif 65 <= ord(char) <= 90:
        lowerChar = chr(ord(char) + 26)
        newString += lowerChar
    newString += stringToLetters(string[1:])

"""