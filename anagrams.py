"""
anagrams.py
What anagrams can be found among 1000 common words in US English?
To find out, debug the definition of the find_anagrams function below.

In addition to fixing the code, add two comments as follows:
# BUG: Show where you found the bug and explain how you found it.
# FIX: Briefly explain in English how you fixed the bug.

Author: johnsoam ; Andrew Johnson

Main topics: Using dictionaries to solve problems; dictionaries with lists
as values; debugging
"""

def sort_letters(word):
    """ 
    Returns a string containing the letters of the given word,
    in alphabetical order.
    """
    chars = list(word)
    chars.sort()
    return ''.join(chars)
    
def find_anagrams(words):
    """
    Given a list of words, produces a list of lists.
    Each sublist contains words that are anagrams of each other.
    """
    grouped_words = {}
    #print(words)
    # Build a dictionary mapping sorted letters to lists of similar words.
    for w in words:
        wsorted = sort_letters(w)
        
        if wsorted in grouped_words:    
            grouped_words[wsorted].append(w)    #BUG: was appending to non-extent lists,
                                                #found by comparing it to mode(data) function
                                                #on pg. 378 of text book
        else:                                   #CORRECTION: if wsorted is not present
            grouped_words[wsorted] = []         #it must be created as a list first
            grouped_words[wsorted].append(w)    #and then appended
            
            
    # Return a list containing only the groups larger than 1.         
    result = []     
    for group in grouped_words.values():
        if len(group) > 1:
            result.append(group)
    return result    

def retrieve_page(url):
    """ 
    Retrieve the contents of a web page.
    The contents is converted to a string before returning it.
    """
    import urllib.request
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.read())
    my_socket.close()
    return dta    
    
def main():
    # Get list of 1000 common US English words
    url = "http://splasho.com/upgoer5/phpspellcheck/dictionaries/1000.dicin"
    words = retrieve_page(url).strip().split('\\n')
    
    # Find and print anagrams
    anagrams = find_anagrams(words)
    print("%d anagram groups found" % len(anagrams))
    for group in anagrams:
        print(group)

if __name__ == '__main__':
    main()
