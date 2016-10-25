"""
Author username(s): johnsoam
Date: 10/24/16
Assignment/problem number: Exam 2
Assignment/problem title: Prgoramming
"""

def grep (searchstring, filename):
    
    textFile = open(filename, "r", encoding = "utf-8")
   
    for line in textFile:
        linePrinted = False 
        for i in range(len(line) - len(searchstring) + 1):
            if line[i:i+len(searchstring)] == searchstring and linePrinted == False:
                print(line)
                linePrinted = True     
                
    textFile.close()        
                
if __name__ == "__main__":
    grep ("prefer not to", "bartleby.txt")
    
    
    
    #text = textFile.read()
    #textFile.close()