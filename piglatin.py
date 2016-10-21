

VOWELS = "aeiuo"

def piglatin(word):
	

	return word[1:] + word[0] + "ay"
	



def main():
	print(piglatin("python"))
	print(piglatin("Janet"))	
	print(piglatin("string"))
	
if __name__ == "__main__":
	main() 



