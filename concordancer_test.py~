"""
Author username(s): crowlema ; johnsoam
Date: 11/6/16
Assignment/problem number: Homework 13
Assignment/problem title: Concordancer
"""

from concordancer import *

def test():
	# Common Cases	
	assert read_url("http://cs.whitman.edu/~exleyas/course_resources/test1.txt") == "simple test case\n"
	assert read_url("http://cs.whitman.edu/~exleyas/course_resources/test2.txt") == "i do not like green eggs and ham\ni do not like them sam-I-am\ni will not eat them in a box\ni will not eat them with a fox\n"
	assert string_to_words("fox") == ["fox"]
	assert string_to_words("fox in box") == ["fox", "in", "box"]
	

	# Boundary Cases
	assert string_to_words("fox1987!!!!!") == ["fox"]
	assert string_to_words("") == [""]
	

	# Corner Cases
	assert string_to_words("!") == [""]
	assert string_to_words("0a0") == ["a"]

	print("Passed all tests!")

def test_count_words():
	list = ["apples", "pears", "grapes"]
	assert "apples" in count_words(list)

	print("Passed all tests!")

if __name__ == "__main__":
	test()
	test_count_words()
