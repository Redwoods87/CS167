# 1/1 count_web_words
# 1/1 read_url
# 1/1 string_to_words
# 1.5/2 count_words
#     Bug as noted! You could remove the empty words here
# 2/2 print_descending
# 2/2 comments and style
#
# GRADE: 7.5/8
# Nice work!




import urllib.request as web

def get_input():
	input_url = input("What url do you want to use?")
	return input_url

def read_url(url):
	"""
	Reads a webpage.
	Parameters:
		url: the url of the webpage
	Returns: the text of the webpage as a string
	"""
	webpage = web.urlopen(url)
	text = webpage.read()
	text = text.decode("utf-8")
	webpage.close()
	return text


def string_to_words(big_string):	#BUG: extra spaces make empty list items
	"""
	Turns a string into a list, omitting everything but letters and spaces
	Parameters:
		big_string: a string
	Returns: a list with each item an individual word
	"""
	assert isinstance(big_string, str)	
	big_string = big_string.lower()
	simple_string = ""
	for i in range(0, len(big_string)):
		if ord("a") <= ord(big_string[i]) <= ord("z") or ord(big_string[i]) == ord(" "):
			simple_string += big_string[i]
		elif big_string[i] == "\n":
			simple_string += " "	
	word_list = simple_string.split(" ")
	return word_list


def count_words(list_words):	
	"""
	Turns a list of words into a dictionary with words as keys and word counts as values
	Parameters:
		list_words: a list of words with one word per item
	Returns: a dictionary with words and word counts
	"""
	assert isinstance(list_words, list)	
	word_counts = {}
	for word in list_words:
		if word in word_counts:
			word_counts[word] = word_counts[word] + 1
		else:
			word_counts[word] = 1
	return word_counts


def count_web_words(url):
	"""
	Takes a webpage and returns a dictionary of the individual words and word counts
	Parameters:
		url: the url of the webpage
	Return Value: a dictionary with words as keys and wordcounts as values
	"""

	assert isinstance(url, str)
	text = read_url(url)
	word_list = string_to_words(text)
	word_counts = count_words(word_list)
	return word_counts


def print_descending(word_dict):
	"""
	Prints a dictionary of individual words and their counts in descending order of wordcounts
	Parameters:
		word_dict: a dictionary of words and wordcounts
	Pre-conditions: the dictionary's keys should be individual words and the values should be wordcounts
	Post-conditions: will print each item on its own line with paired keys and items
	Return Value: None, called for its side effects 
	"""
	assert isinstance (word_dict, dict)
	values = list(word_dict.values())
	max_value = max(values)
	num = max_value
	while num > 0:
		for key in word_dict:
			if word_dict[key] == num:
				print(key, ":", word_dict[key])
		num -= 1


def main():
	url = get_input()
	dictionary = count_web_words(url)
	print_descending(dictionary)


#if __name__ == "__main__":
#	main()
if __name__=='__main__':
    print_descending(count_web_words('http://cs.whitman.edu/%7Eexleyas/course_resources/test2.txt'))
