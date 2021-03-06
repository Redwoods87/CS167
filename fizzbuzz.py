"""
fizzbuzz.py
Complete the implementation of the fizzbuzz function as documented and 
tested below.

Author: johnsoam / Andrew Johnson

Main topics: Conditionals, strings, test-driven development
"""
import sys

def fizzbuzz(n):
	"""
	If the integer n contains the digit 3, returns "Fizz"
	If the integer n contains the digit 7, returns "Buzz"
	If the integer n contains both 3 and 7, returns "FizzBuzz"
	Otherwise returns the number as a string
	"""
	yesToThree = False		#Variables to track presence of 3 and 7
	yesToSeven = False	
	
	intAsString = str(n)	#int to string

	for i in range(len(intAsString)):	#check for presence of 3 and/or 7
		if intAsString[i] == "3":
			yesToThree = True
		if intAsString[i] == "7":
			yesToSeven = True
	
	if yesToThree == True and yesToSeven == False:	#return value based on tracking variables
		return "Fizz"
	elif yesToThree == False and yesToSeven == True:
		return "Buzz"
	elif yesToThree == True and yesToSeven == True:
		return "FizzBuzz"
	else:
		return intAsString
	
def test(did_pass):
	"""  Print the result of a test.  """
	linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
	if did_pass:
		msg = "Test at line {0} passed.".format(linenum)
	else:
		msg = ("Test at line {0} FAILED.".format(linenum))
	print(msg)
			
if __name__=='__main__': 
	test(fizzbuzz(1) == '1')
	test(fizzbuzz(2) == '2')
	test(fizzbuzz(3) == 'Fizz')
	test(fizzbuzz(4) == '4')
	test(fizzbuzz(5) == '5')
	test(fizzbuzz(6) == '6')
	test(fizzbuzz(7) == 'Buzz')
	test(fizzbuzz(8) == '8')
	test(fizzbuzz(9) == '9')
	test(fizzbuzz(10) == '10')   
	test(fizzbuzz(30) == 'Fizz')  
	test(fizzbuzz(37) == 'FizzBuzz')
	test(fizzbuzz(70) == 'Buzz') 
	test(fizzbuzz(73) == 'FizzBuzz')
	test(fizzbuzz(99) == '99')
	test(fizzbuzz(100) == '100')
