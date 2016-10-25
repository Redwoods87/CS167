"""
Author username(s): johnsoam
Date: 10/24/16
Assignment/problem number: Exam 2
Assignment/problem title: Programming
"""

def grep (searchstring, filename):
    """
    Prints lines of a text file containing a specified substring.
    
    Parameters:
        searchstring: a string to be found in the given text file
        filename: the name of a file to search in
    
    Returns: None
    
    Preconditions: searchstring must be a string of characters; filename must be a string of the name of a text file in the same directory, including the file extension.
    
    Postconditions: will print each line of the file containing the searchstring as a string; each line will be printed only once, even if it contains the searchstring multiple times.
    """
    
    textFile = open(filename, "r", encoding = "utf-8")
   
    for line in textFile:
        lineAlreadyPrinted = False 
        for i in range(len(line) - len(searchstring) + 1):
            if line[i:i+len(searchstring)] == searchstring and lineAlreadyPrinted == False:
                print(line)
                lineAlreadyPrinted = True     
                
    textFile.close()        
                
if __name__ == "__main__":
    grep ("prefer not to", "bartleby.txt")  
    
    # Current test uses Herman Melville's "Bartleby, The Scrivener" at "http://www.gutenberg.org/cache/epub/11231/pg11231.txt".
