"""
Practice Functions for Exam 2
Oct. 23, 2016
"""

def countACG(dna):
	dna = dna.upper()
	print(dna)
	total = 1 
	countNotT = 0
	for i in range (len(dna)):
		if dna[i] == "T":
			total += 1
		if dna[i] == "A" or dna[i] == "C" or dna[i] == "G":
			countNotT += 1
			total += 1
	fractionNotT = countNotT / total
	return fractionNotT	

dnaFile = open("eco536-1k.txt", "r", encoding="utf-8")
dna = dnaFile.read()
dnaFile.close()

#print(countACG(dna))

def count(text, target):
	count = 0
	for i in range (len(text)):
		if text[i:len(target)+1] == target:
			count += 1
	return count

text1 = "I went to the store yesterday."
target1 = "the"

print (count(text1, target1))





