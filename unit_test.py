"""
Author username(s): fitzhult ; johnsoam
Date: 10/27/16
Assignment/problem number: Homework 11
Assignment/problem title: Design by Contract & Unit Testing
"""

def find(text, target):
    """
    Finds the starting index of a target substring within a larger string.
    
    Parameters:
        text: a string to search in
        target: a string to search for in the text
    
    Returns: the starting index of the target or -1 if the target is not found
    
    Preconditions: length of text >= length of target; both text and target must be strings
    
    Postconditions: will return a positive integer signifying the starting index of the target substring, if found; will return -1 if the target is not found
    """
    
    assert isinstance(text, str), "text must be a string"
    assert isinstance(target, str), "target must be a string"
    assert len(text) >= len(target), "target length must be shorter than or equal to the length of text"
    
    for index in range(len(text) - len(target) + 1):
        if text[index:index + len(target)] == target:
            return index
    return -1

def gotAssertionError(text, target):
    """
    Code courtesy of Professor Janet Davis, Whitman College.
    """
    try:
        find(text, target)
    except AssertionError:
        return True
    return False

def test_find():
    #commmon cases
    assert find("bananas taste good", "taste") == 8
    assert find("artichoke", "tic") == 2
    #boundry cases
    assert find("taste", "taste") == 0
    assert find("artichoke", "art") == 0
    assert find("artichoke", "choke") == 4
    assert find("apple", "e") == 4
    assert find("people", "p") == 0
    #corner cases
    assert gotAssertionError("love", "lovely") == True
    assert gotAssertionError(1234,"1234") == True
    assert find("0", "0") == 0
    assert gotAssertionError(1234, 3) == True
    assert gotAssertionError("1234", 1234) == True
    assert find("-3_apple", "apple") == 3
    print("find passed all tests!")

def power(base, exp):
    """
    power calculates b to the power of exp without using the math module or the ** operator, and returns the result.
    This function adheres to the interpretation that 0 to the 0 power is 1.
    
    Preconditions:
        base is an integer
        exp is a non-negative integer
    
    Postconditions:
        returns an integer that is the calculation of base to the exp power
    """
    
    assert isinstance(base, int)
    assert isinstance(exp, int)
    assert exp >= 0
    
    result = base
    if exp == 0:
        return 1
    else:
        for i in range(exp - 1):
            result *= base
    return result

def gotPowerError(base, exp):
    """
    Code courtesy of Professor Janet Davis, Whitman College.
    """
    try:
        power(base, exp)
    except AssertionError:
        return True
    return False

def test_power():
    #common cases
    assert power(2,4) == 16
    assert power(6, 12) == 2176782336
    assert power(-3, 3) == -27
    #boundary cases
    assert power(2, 0) == 1
    assert power(0, 0) == 1
    assert power(12345, 3) == 1881365963625
    #edge cases
    assert gotPowerError(4, -4) == True
    assert gotPowerError("apple", 10) == True
    assert gotPowerError(10, "apple") == True
    assert gotPowerError(2, 2.5) == True
    assert gotPowerError(3.5, 3) == True
    assert gotPowerError(-1, -1) == True
    print("power passed all tests!")
    
if __name__=="__main__":
    test_find()
    test_power()