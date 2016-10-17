"""
Author username(s): bulsonjg ; johnsoam
Date: 10/16/16
Assignment/problem number: Homework 9
Assignment/problem title: Caesar Cipher
"""

def relOrdCharacter(character, bottomRangeNumber):
    """
    Finds an ordinal of a character relative to another ordinal.

    Parameters:
        character: the character to convert to a relative ordinal
        bottomRangeNumber: an ordinal to modify the character's ordinal, such that it is within a range of possible ordinals

    Returns: the difference between ordinal of the character and bottomRangeNumber (ie. the 'relative ordinal of the character')
    """
    return ord(character) - bottomRangeNumber

def encodeCharacter(targetCharacter, keyCharacter):
    """
    Encodes a single target character using a Caesar cypher.

    Parameters:
        targetCharacter: the character to be encoded
        keyCharacter: the character used to determine the ordinal to modify the ordinal of the target character.

    Returns: encoded character
    """
    bottomRangeNumber = 97 # *RangeNumber values refer to the ordinals of characters
    topRangeNumber = 122
    widthRangeNumber = topRangeNumber - bottomRangeNumber
    relOrdTargetCharacter = relOrdCharacter(targetCharacter, bottomRangeNumber)
    relOrdKeyCharacter = relOrdCharacter(keyCharacter, bottomRangeNumber)
    if ord(targetCharacter) < bottomRangeNumber or ord(targetCharacter) > topRangeNumber:
        ordEncodedCharacter = ord(targetCharacter)  # If the character is outside of the range of ordinal values to be encoded, character remains unchanged
    else:
        ordEncodedCharacter = (relOrdTargetCharacter + relOrdKeyCharacter) % (widthRangeNumber+1) + bottomRangeNumber
    return chr(ordEncodedCharacter)

def encodeString(text, keyString):
    """
    Encodes a string of text using a string as a key.

    Parameters:
        text: the text to be encoded
        keyString: the string to be used for the encoding

    Returns: a string of encoded text
    """
    encodedText = ''
    for i in range(len(text)):
        print(text[i], keyString[i%len(keyString)])
        encodedText = encodedText + encodeCharacter(text[i], keyString[i%len(keyString)])
    return encodedText

def encode(filename, key):
    """
    Encodes the contents of a plaintext file using a given key with a caesar cipher. Writes the encoded contents into a new file in the same directory with the name 'filename' + Encoded.

    Parameters:
        filename: name of the file to be encoded.
        key: key used to encode the file.

    Returns none.

    """
    textFile = open(filename, 'r') # The open(..., encoding = 'utf-8') from pg. 285 was not accepted as valid parameter, hence its omission
    inputText = textFile.read()
    textFile.close()
    encodedTextString = encodeString(inputText[:-1], key)
    outputFilename = filename + 'Encoded'
    outputFile = open(outputFilename, 'w')
    outputFile.write(encodedTextString)
    return encodedTextString

def decodeCharacter(targetCharacter, keyCharacter):
    """
    Decodes a single target character using a Caesar cypher.

    Parameters:
        targetCharacter: the character to be decoded
        keyCharacter: the character used to determine the ordinal to modify the ordinal of the target character.

    Returns: decoded character
    """
    bottomRangeNumber = 97 # *RangeNumber values refer to the ordinals of characters
    topRangeNumber = 122
    widthRangeNumber = topRangeNumber - bottomRangeNumber
    relOrdTargetCharacter = relOrdCharacter(targetCharacter, bottomRangeNumber)
    relOrdKeyCharacter = relOrdCharacter(keyCharacter, bottomRangeNumber)
    if ord(targetCharacter) < bottomRangeNumber or ord(targetCharacter) > topRangeNumber:
        ordDecodedCharacter = ord(targetCharacter)  # If the character is outside of the range of ordinal values to be decoded, character remains unchanged
    else:
        ordDecodedCharacter = (relOrdTargetCharacter - relOrdKeyCharacter) % (widthRangeNumber+1) + bottomRangeNumber
    return chr(ordDecodedCharacter)

def decodeString(text, keyString):
    """
    Decodes a string of text using a string as a key.

    Parameters:
        text: the text to be decoded
        keyString: the string to be used for the decoding

    Returns: a string of decoded text
    """
    decodedText = ''
    for i in range(len(text)):
        print(text[i], keyString[i%len(keyString)])
        decodedText = decodedText + decodeCharacter(text[i], keyString[i%len(keyString)])
    return decodedText

def decode(filename, key):
    """
    Decodes the contents of a plaintext file using a given key with a caesar cipher. Writes the decoded contents into a new file in the same directory with the name 'filename' + Decoded.

    Parameters:
        filename: name of the file to be decoded.
        key: key used to decode the file.

    Returns none.

    """
    textFile = open(filename, 'r') # The open(..., encoding = 'utf-8') from pg. 285 was not accepted as valid parameter, hence its omission
    inputText = textFile.read()
    textFile.close()
    decodedTextString = decodeString(inputText[:-1], key)
    outputFilename = filename + 'Decoded'
    outputFile = open(outputFilename, 'w')
    outputFile.write(decodedTextString)
    return decodedTextString

def main():
    """
    Asks the user whether they want to encode or decode a file, and proceeds with that process.

    Parameters: None

    Returns: None
    """
    operation = input("Would you like to [e]ncode or [d]ecode? ")
    if operation == 'e':
        encode(input('What is the name of the file you would like to encode? \n \
                Please enter in quotation marks.'), \
                input('What string would you like to encrypt the file? '))
    elif operation == 'd':
        decode(input('What is the name of the file you would like to decode? \n \
                Please enter in quotation marks'), \
                input('What string would you like to try to decrypt the file? '))
    else:
        print('Not a recognized answer. Closing.')

if __name__=='__main__':
    main()
