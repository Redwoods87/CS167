def reverse(dna):
    """Return the reverse of a DNA sequence

    Parameter:
        dna: a string representing a DNA sequence

    Return value: the reverse of the DNA sequence
    """
    revdna = ''
    for nt in dna:
        revdna = nt + revdna
    return revdna

def complementNucleotide(nt):
    """Return the complement of a single nucleotide.
    """
    if nt == 'a':
        return 't'
    elif nt == 't':
        return 'a'
    elif nt == 'c':
        return 'g'
    elif nt == 'g':
        return 'c'

def complement(dna):
    """Return the complement of a dna sequence
    Parameter:
        dna: a string representing a DNA sequence
    Return value: the complement of the DNA sequence
    """
    dna = dna.lower()
    compdna = ""
    for index in range(len(dna)):
        compdna += complementNucleotide(dna[index])
    return compdna

def reverseComplement(dna):
    """Return the reverse  complement of a dna sequence
    """
    return reverse(complement(dna))

def palindrome(dna):
    """Determines if a dna string is a palindrome
    Parameter:
        dna: a sequence of dna entered as a string
    Returns: True or False
    """
    return dna.lower() == reverseComplement(dna)

def countCodon(dna, target):
    """Return number of target codons in dna.
    Parameters:
        dna: a string object representing the dna sequence
        target: a three-letter string object representing the codon to search for
    Return value: The number of instances of the target codon in dna
    """
    numberOfCodons = 0
    for i in range (len(dna)):
        if dna[i:i+3] == target:
            numberOfCodons += 1
        else:
            continue
    return numberOfCodons

def printCodons(dna):
    """Print all codons in the dna, one codon per line.
    Parameters: dna: a dna sequence
    Return value: None
    """
    for i in range (0, len(dna), 3):
        if len(dna[i:i+3]) == 3:
            print (dna[i:i+3])
        else:
            print (dna[i:i+3] + " : incomplete codon")
    #print("")

if __name__ == "__main__": 
    # print(palindrome("gaattc"))
    # print(countCodon("aatcgatagggg", "ggg"))
    printCodons("aatcgatagggg")