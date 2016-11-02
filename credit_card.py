# remove spaces and hyphens from card numbers
# add assertions to enforce preconditions
# write our names
# I think we could have left it as a list?
# Main needs a full doc string




def isAmEx(cardNum):
	"""Checks to see if the card number is a valid American Express card number.

	Parameters:
		cardNum: A list with each item in the list representing one integer in the card number.
	
	Preconditions: cardNum is a valid list

	Postconditions: Returns a boolean True/False value.
		
	Returns:
		True if the card is a valid American Express card
		False if it is not.		
	"""
	return (cardNum[0:2] == [3,4] or cardNum[0:2] == [3,7]) and len(cardNum) == 15
	
    
def isDiscover(cardNum):
	"""Checks to see if the card number is a valid Discover card number.

	Parameters:
		cardNum: A list with each item in the list representing one integer in the card number.
	
	Preconditions: cardNum is a valid list

	Postconditions: Returns a boolean True/False value.
		
	Returns:
		True if the card is a valid Discover card
		False if it is not.		
	"""
	return (cardNum[0:4] == [6,0,1,1] or cardNum[0:3] == [6,4,4] or cardNum[0:2] == [6,5]) \
and len(cardNum) == 16


def isMasterCard(cardNum):
	"""Checks to see if the card number is a valid MasterCard card number.

	Parameters:
		cardNum: A list with each item in the list representing one integer in the card number.
	
	Preconditions: cardNum is a valid list

	Postconditions: Returns a boolean True/False value.
		
	Returns:
		True if the card is a valid MasterCard card
		False if it is not.		
	"""
	return cardNum[0:2] in [[5,1],[5,2],[5,3],[5,4],[5,5]] and len(cardNum) == 16


def isVisa(cardNum):
	"""Checks to see if the card number is a valid Visa card number.

	Parameters:
		cardNum: A list with each item in the list representing one integer in the card number.
	
	Preconditions: cardNum is a valid list

	Postconditions: Returns a boolean True/False value.
		
	Returns:
		True if the card is a valid Visa card
		False if it is not.		
	"""
	return cardNum[0] == 4 and (len(cardNum) == 13 or len(cardNum) == 16)


def stringToList(string):
	"""Turns a given string of numbers into a list where each item in the list represents each number in the string.
	
	Parameters:
		string: The string to be converted.
	
	Preconditions: String is a valid string of only integers.
	
	Postconditions: Returns a valid list.
	
	Returns:
		A list where each item in the list corresponds to each number in the given string	
	"""
	stringList = []
	for character in string:
		stringList.append(int(character))
	return stringList


def is_type_accepted(card_number):
	"""Checks if the given card is of an accepted type.

	Parameter: A string representing a 15- or 16-digit credit card number.

	Returns:
		True if the number is an American Express, Discover, MasterCard, or Visa number;
				  False otherwise.
	"""
	cardList = stringToList(card_number)
	return (isAmEx(cardList) or isDiscover(cardList) or isMasterCard(cardList) or isVisa(cardList))


def is_checksum_valid(card_number):
	"""Checks if a credit card number is valid.

	Parameter: A string representing an integer.

	Returns:
		True if the number passes the Luhn checksum algorithm;
				  False if it does not.
	"""
	checkSum = 0
	cardList = stringToList(card_number)
	for i in range(-1,-len(cardList)-1,-2): #Sum of integers on odd, negative indices		
		checkSum += cardList[i]
	for i in range(-2,-len(cardList)-1,-2): #Sum of doubled integers on even, negative indices		
		temp = cardList[i] * 2
		if temp >= 10:
			temp -= 9 #Subtracting 9 from a 2-digit integer less than 20 is the same as adding the digits
		checkSum += temp
	return checkSum % 10 == 0 #True if it ends in 0


def invalidCard():
	"""Prints a message for when your card is invalid.	
	"""
	print("We're sorry, the card number you have entered is invalid.")

    
def cardTypeTest(card_number):
	"""Returns the name of the credit card brand of the given number.
	
	Parameters:
		card_number: The number of the credit card.
	
	Preconditions: card_number is a valid string with only integers and no spaces.

	Postconditions: Returns a string based the kind of card the number represents.
	
	Returns:
		The brand name of the credit card as a string.
		An error message if the input is not one of the credit card brand numbers.
	"""
	if isAmEx(card_number) == True:
		return "American Express"
	elif isDiscover(card_number) == True:
		return "Discover"
	elif isMasterCard(card_number) == True:
		return "MasterCard"
	elif isVisa(card_number) == True:
		return "Visa"
	else:
		return " [[[ ERROR: This message should not display. If it does, contact programmer. ]]] "

    
def main():
	"""Asks the user for a credit card number. Reports whether the number is accepted and valid.
	"""
	cardNumber=str(input("Please enter your credit card number with no spaces or hyphens: "))
	if is_type_accepted(cardNumber) == False:
		invalidCard()
	else:
		if is_checksum_valid(cardNumber) == False:
			invalidCard()
		else:
			cardType = cardTypeTest(cardNumber)
			print("Thank you, you have entered a valid" ,cardType, "number.")


if __name__ == "__main__":
	main()
