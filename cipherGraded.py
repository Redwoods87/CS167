# encrypt
# 1/1 Reads text from a file
# 1/1 Returns an obfuscated output
# 1/1 Correctly encrypts the given example: 'helloyou' + 'dog' -> 'ksroceri'
# 1/1 Handles keywords of different lengths
# 1/1 Characters other than lower-case letters are copied without encryption
# 
# decrypt
# 1/1 Reads encrypted text from a file
# 2/2 Returns some attempt at decrypting the text
# 1/1 Correctly decrypts given example
# 0.5/1 Correctly decrypts other messages encrypted by your program
#     Consistently loses the last character of messages encrypted by your 
#     program.
# 
# main
# 1/1 User input as specified
# 1/1 Calls functions and outputs result as specified
# 
# Including spaces and newlines
# 1/1 Attempted
# 1/1 Correct per specification
# 
# 1/2 Style, comments, following instructions
#     See long note below
#
# +1 Above & beyond
# 
# GRADE: 15.5/16
# I'm not sure whether to be annoyed at you or proud of you.  You have indeed
# created a much more general algorithm.  However, you didn't follow the 
# specification, which made your code much harder to test and use.
# You'll see above that I graded accordingly.

"""
Author username(s): bulsonjg ; johnsoam
Date: 10/17/16
Assignment/problem number: Homework 9
Assignment/problem title: Caesar Cipher

Note: the "range numbers" set in encodeCharacter and decodeCharacter refer to the ordinal scale of the ASCII characters (see Figure 6.2 on page 264). These are currently set to 32 and 126, which covers the range of spaces, punctuation characters, digits, lower case letters, and upper case letters, such that any character might be encoded to any other character within the range, as determined by the key string. 
#DAVISJ: Please provide a version of your program that is as specified.
#DAVISJ: You've made this quite difficult for me to test.

To limit this range to encode only lower case letters, the range should be set to 97 and 122.

Note: part 4 of the assignment ("including space"), including functions "encode_space" and "decode_space" have been intentionally omitted. Their functionality has been built into the program's ability to define the character ordinal range (pg. 264), such that by setting the range to 32 and 126, all non-control characters are encoded and decoded, including spaces.

Note: the encode and decode functions have commented out sections that, if re-inserted, would create a new encoded or decoded file in addition to returning a string.

Bug: files created using the commented out sections of encode and decoded add the "Encoded" or "Decoded" to the filename after the ".txt"; fix so that "Encoded" or "Decoded" comes before the file extension.
"""
#DAVISJ: My code here to make it possible to test your code
bottomRangeNumber = 97 
topRangeNumber = 122

def expand_range():
    global bottomRangeNumber, topRangeNumber
    bottomRangeNumber = 32 
    topRangeNumber = 126

def contract_range():
    global bottomRangeNumber, topRangeNumber
    bottomRangeNumber = 97 
    topRangeNumber = 122

def encode_space(filename, key):
    expand_range()
    text = encode(filename, key)
    contract_range()
    return text

def decode_space(filename, key):
    expand_range()
    text = decode(filename, key)
    contract_range()
    return text

def relOrdCharacter(character, bottomRangeNumber):
    """Finds the ordinal of a character and sets it relative to bottom ordinal within a range (see header).
    Parameters:
        character: the character to convert to a relative ordinal
        bottomRangeNumber: an ordinal to modify the character's ordinal, such that it is within a range of possible ordinals
    Returns: the difference between ordinal of the character and bottomRangeNumber (ie. the 'relative ordinal of the character')
    """
    return ord(character) - bottomRangeNumber



def encodeCharacter(targetCharacter, keyCharacter):
    """Encodes a target character based on a key character.
    Parameters:
        targetCharacter: the character to be encoded
        keyCharacter: the character used to modify the target
    Returns: encoded character
    """
    #DAVISJ: I'm making these global variables to give me some hope of
    #DAVISJ: testing your code.  This is an appropriate use of globals,
    #DAVISJ: especially since it's super important that the same definitions
    #DAVISJ: are used in both functions.
    #bottomRangeNumber = 32 # RangeNumber values refer to the ordinals of characters; see note in header
    #topRangeNumber = 126
    widthRangeNumber = topRangeNumber - bottomRangeNumber
    relOrdTargetCharacter = relOrdCharacter(targetCharacter, bottomRangeNumber)
    relOrdKeyCharacter = relOrdCharacter(keyCharacter, bottomRangeNumber)
    if ord(targetCharacter) < bottomRangeNumber or ord(targetCharacter) > topRangeNumber:   # If outside range, character remains unchanged
        ordEncodedCharacter = ord(targetCharacter)  
    else:
        ordEncodedCharacter = (relOrdTargetCharacter + relOrdKeyCharacter) % (widthRangeNumber+1) + bottomRangeNumber   # "%" used to wrap 
    return chr(ordEncodedCharacter)



def encodeString(text, keyString):
    """Encodes a string of text using a string as a key.
    Parameters:
        text: the text to be encoded
        keyString: the string to be used for the encoding
    Returns: a string of encoded text
    """
    encodedText = ""
    for i in range(len(text)):
        # print(text[i], keyString[i%len(keyString)])   # Print original and encoded text as a test
        encodedText = encodedText + encodeCharacter(text[i], keyString[i % len(keyString)]) # "%" used to repeat key characters
    return encodedText



def encode(filename, key):
    """Encodes the contents of a plaintext file using a key string. (The commented out section Writes the encoded contents into a new file in the same directory with the name 'filename' + Encoded.)
    Parameters:
        filename: name of the file to be encoded
        key: key used to encode the file
    Returns: encoded message as a string
    
    Note: If the file is missing a \n at the end, the function will erroneously omit the final character.
    """
    textFile = open(filename, 'r') # The open(..., encoding = 'utf-8') from pg. 285 was not accepted as valid parameter, hence its omission
    inputText = textFile.read()
    textFile.close()
    encodedTextString = encodeString(inputText[:-1], key)
    #   outputFilename = filename + "Encoded"
    #   outputFile = open(outputFilename, 'w')
    #   outputFile.write(encodedTextString) # Does this need a \n at end, or auto inserted?
    return encodedTextString



def decodeCharacter(targetCharacter, keyCharacter):
    """Decodes a target character based on a key character.
    Parameters:
        targetCharacter: the character to be decoded
        keyCharacter: the character used to decode the target
    Returns: decoded character
    """
    #bottomRangeNumber = 32 # RangeNumber values refer to the ordinals of characters; see note in header
    #topRangeNumber = 126
    widthRangeNumber = topRangeNumber - bottomRangeNumber
    relOrdTargetCharacter = relOrdCharacter(targetCharacter, bottomRangeNumber)
    relOrdKeyCharacter = relOrdCharacter(keyCharacter, bottomRangeNumber)
    if ord(targetCharacter) < bottomRangeNumber or ord(targetCharacter) > topRangeNumber:
        ordDecodedCharacter = ord(targetCharacter)  # If outside range, character remains unchanged
    else:
        ordDecodedCharacter = (relOrdTargetCharacter - relOrdKeyCharacter) % (widthRangeNumber+1) + bottomRangeNumber   # "%" used to wrap 
    return chr(ordDecodedCharacter)



def decodeString(text, keyString):
    """Decodes a string of text using a string as a key.
    Parameters:
        text: the text to be decoded
        keyString: the string to be used for the decoding
    Returns: a string of decoded text
    """
    decodedText = ""
    for i in range(len(text)):
        # print(text[i], keyString[i%len(keyString)]) # Print original and encoded text as a test
        decodedText = decodedText + decodeCharacter(text[i], keyString[i%len(keyString)])   # "%" used to repeat key characters
    return decodedText



def decode(filename, key):
    """Decodes the contents of a plaintext file using a key string. (The commented out section writes the decoded contents into a new file in the same directory with the name 'filename' + Decoded.)
    Parameters:
        filename: name of the file to be decoded
        key: key used to decode the file
    Returns: decoded message as a string
    
    Note: If the file is missing a \n at the end, the function will erroneously omit the final character.
    """
    textFile = open(filename, 'r') # The "open(..., encoding = 'utf-8')" from pg. 285 was not accepted as valid parameter, hence its omission
    inputText = textFile.read()
    textFile.close()
    decodedTextString = decodeString(inputText[:-1], key)
    #   outputFilename = filename + 'Decoded'
    #   outputFile = open(outputFilename, 'w')
    #   outputFile.write(decodedTextString) # Does this need a \n at end, or auto inserted?
    return decodedTextString



def main():
    """Prints the encoded or decoded message from a file.
    Parameters: None
    Returns: None
    """
    operation = input("Would you like to [e]ncode or [d]ecode? ")
    if operation == "e":
        filename = input("What file you would like to encode? (Please include file extension.) ")
        key = input("What encryption key should be used? ")
        print (encode(filename, key)) 
    elif operation == "d":
        filename = input("What file you would like to decode? (Please include file extension.) ")
        key = input("What is this file's key? ")
        print (decode(filename, key)) 
    else:
        print('Not a recognized response. Closing program.')

        
        
if __name__=='__main__':
    main()    
    # print(decodeString("ksroceri", "dog"))
    # print(encode("helloyou.txt", "dog"))
    # print(decode("toDecode.txt", "dog"))
