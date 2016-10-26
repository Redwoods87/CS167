# wget http://cs.whitman.edu/~davisj/cs/167/2016F/exmpls/testing.py

def digit2String(digit):
  """Convert a digit to its corresponding string representation.
  Parameter:     digit, an integer
  Produces:      the string representation of digit
  Precondition:  digit is between 0 and 9
  Postcondition: returns None if digit is not an integer between 0 and 9
  Provenance:    From Havill (2016), _Discovering Computer Science, p. 332-3
  """
  if not isinstance(digit, int) or (digit < 0) or (digit > 9):
    return None
  return chr(ord('0') + digit

# From Havill (2016), _Discovering Computer Science, p. 333-4
def int2String(value):
  """Convert an integer to its corresponding string representation.
  Parameter:     value, an integer
  Produces:      the string representation of value
  Precondition:  
  Postcondition: 
  Provenance:    From Havill (2016), _Discovering Computer Science, p. 333-4
  """
  intString = ''
  while value > 0:
    digit = value % 10
    value = value // 10
    digitString = digit2String(digit)
    if digitStr != None:
      intString = digit2Str + intString
    else:
      return None
  return intString

 
