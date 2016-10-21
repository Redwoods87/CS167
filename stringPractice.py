

def noVowels(text):
	vowels = "aeiouAEIOU"
	wordNoVowels = ""
	for character in text:
		if character in vowels:
			continue
		else:
			wordNoVowels = wordNoVowels + character
	print (wordNoVowels) 

# noVowels("balloon's are my favorite party favor.")

def daffy(word):
	daffyWord = ""
	for character in word:
		if character == "s" or character == "S":
			daffyWord = daffyWord + "sth"
		else:
			daffyWord = daffyWord + character
	print (daffyWord)

daffy("Snacking on Sunday is something really super.")


def reverse(text):
	reversedText = ""
	for character in text:
		reversedText = character + reversedText
	print(reversedText)

reverse("apple")

def value(digit):
	print(ord(digit) - ord('0'))

value("4")


