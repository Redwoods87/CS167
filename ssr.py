"""
Author username(s): watsonjr ; johnsoam
Date: 10/20/16
Assignment/problem number: Homework 10
Assignment/problem title: Above & Beyond: Microsatellites
"""

def firstSSR(dna, repeat):
    """Finds the number of repetitions of the first SSR in a dna string.

    Parameters:
    dna: a dna string
    repeat: a string of single-lettered nucleotides

    Returns: the number of repeats in the first SSR found
    """
    startIndex = dna.find(repeat)
    ssrCount = 0
    while dna[startIndex:startIndex + len(repeat)] == repeat:
        ssrCount += 1
        startIndex += len(repeat)
    return ssrCount
        
def longestSSR(dna, repeat):
    """Finds the longest space of SSR's in a dna string.

    Parameters:
    dna: a dna string
    repeat: a string of single-lettered nucleotides

    Returns: the number of repeats in the longest SSR found
    """
    ssr = repeat
    longestSsr = 0
    while firstSSR(dna, repeat) > 0:
        longestSsr += 1   
        repeat = repeat + ssr
    return longestSsr

def longestDinucleotideSSR(dna):
    """Finds the dinucleotide of the most repeated SSR in a dna string. 

    Parameters:
    dna: a dna string
    
    Returns: the dinuleotide of the longest repeated SSR; if two are tied for longest, it will return the first of the two to occur in the string 
    """
    count = 0
    for i in range(0, len(dna)-1):
        if longestSSR(dna, dna[i:i+2]) > count:
            count = longestSSR(dna, dna[i:i+2])
            longestDinuc = dna[i:i+2]
    return longestDinuc
    
    
if __name__=="__main__":
    inputFile = open('eco536-500.txt', 'r')
    testSequence = inputFile.read()
    print(testSequence)
    print("First 'caga' SSR:", firstSSR(testSequence, "caga"))
    print("Longest 't' SSR:", longestSSR(testSequence, "t"))
    print("The most repeated dinucleotide is", longestDinucleotideSSR(testSequence))
