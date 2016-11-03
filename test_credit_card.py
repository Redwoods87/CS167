"""
Author username(s): pylescj ; johnsoam
Date: 11/2/16
Assignment/problem number: Homework 12
Assignment/problem title: Checking Credit Cards
"""

from credit_card import *

FakeCard = [1,2,3,4,5,4,3,2,1,2,3,4,5,4,3]
AmExCard1 = [3,4,1,1,1,1,1,1,1,1,1,1,1,1,1]
AmExCard2 = [3,7,1,1,1,1,1,1,1,1,1,1,1,1,1]
LongAmEx = [3,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Discover1 = [6,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Discover2 = [6,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1]
Discover3 = [6,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
LongDiscover = [6,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
MasterCard1 = [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
MasterCard2 = [5,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
LongMaster = [5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Visa1 = [4,1,1,1,1,1,1,1,1,1,1,1,1]
Visa2 = [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
LongVisa = [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# def isAssertionError(singleInput): #Unused
	# pass


def test():
	#Common Case
	assert isAmEx(AmExCard1) == True
	assert isAmEx(AmExCard2) == True
	assert isDiscover(Discover1) == True
	assert isDiscover(Discover2) == True
	assert isDiscover(Discover3) == True
	assert isMasterCard(MasterCard1) == True
	assert isMasterCard(MasterCard2) == True
	assert isVisa(Visa1) == True
	assert isVisa(Visa2) == True
	assert stringToList("12345") == [1,2,3,4,5]
	assert is_checksum_valid("378282246310005") == True
	assert is_checksum_valid("378282246310000") == False # Changed check digit 
	assert is_checksum_valid("379282246310005") == False # Changed undoubled digit
	assert is_checksum_valid("378582246310005") == False # Changed doubled digit
	assert is_checksum_valid("738282246310005") == False # Transposed two digits
	assert is_checksum_valid("6011000990139424") == True
	assert is_checksum_valid("5394129105482350") == True
	assert is_checksum_valid("2000000000000006") == True
	assert is_checksum_valid("7000000000000005") == True
	assert is_checksum_valid("240") == True
	assert is_checksum_valid("345") == False
	assert is_checksum_valid("1010101010") == True
	assert is_checksum_valid("2010101010") == False
	assert is_checksum_valid("4222222222222") == True
	assert is_checksum_valid("4111111111119") == True
	assert is_checksum_valid("5555555555554444") == True
	assert is_checksum_valid("5555555555550101") == False
	assert is_checksum_valid("6011111111111117") == True
	assert is_checksum_valid("6011111111111110") == False
	assert stringToList("123") == [1,2,3]
	assert stringToList("4321432143214321") == [4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1]
	assert stringToList("1apple23") == [1,2,3]
	assert cardTypeTest("4111111111119") == "Visa"

	#Boundary Case 
	assert isAmEx(Visa1) == False
	assert isVisa(MasterCard1) == False
	assert isDiscover(AmExCard1) == False
	assert isMasterCard(Discover1) == False
	assert stringToList("apple") == []
	assert stringToList("411-111-111") == [4, 1, 1, 1, 1, 1, 1, 1, 1]

	#Corner Case
	assert isAmEx(LongAmEx) == False
	assert isAmEx(FakeCard) == False
	assert isDiscover(LongDiscover) == False
	assert isDiscover(FakeCard) == False
	assert isMasterCard(LongMaster) == False
	assert isMasterCard(FakeCard) == False
	assert isVisa(LongVisa) == False
	assert isVisa(FakeCard) == False
	assert stringToList("I went to the store") == []
	assert stringToList("1   3   apple, ! door floor bored") == [1, 3]



	print("Passed all tests!")

test()

# is_checksum_valid("371449635398431")

