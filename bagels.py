"""
Author username(s): johnsoam
Author: Andrew Johnson
Date: 12/11/16
CS167 - C
Final Project, Fall 2016


WELCOME TO

BAGELS REVOLUTION!

THE NUMBER-GUESSING GAME
OF POLITICAL POWER

This program runs the game "Bagels Revolution."

"""

import random
import sys

def intro():
    """
    Prints intro to game, prompts to choose side
    """
    pass
    
def rules():
    """
    Prints rules
    """
    print("THESE ARE THE RULES!")
    
#def help():    #BUILT INTO checkOptions() and rules()
 #   """
#    Prints rules and options to exit or continue
   # """
    #pass

def checkOptions(inputText):
    """
    Checks to see if player has inputed help or quit
    Parameter:
        inputText: a string to check
    """
    if inputText.lower() == "quit" or inputText.lower() == "exit":
        quitResponse = input("Are you sure you want to quit? Enter Yes or No: ")
        if quitResponse.lower() == "yes":
            sys.exit("Thanks for playing.")
    if inputText.lower() == "help":
        helpResponse = input("Would you like to see the rules again? Enter Yes or No: ")
        if helpResponse.lower() == "yes":
            rules()

class BagelsGame:
    """
    A class that manages the mechanics of the game
    
    Each object is given a level of
    difficulty (1, 2, or 3)
    """
    
    def __init__(self, level):
        """
        Constructor that creates a level of the game
        Parameter:
            level: a string ("1", "2", or "3")that determines 
            the difficulty of the game
        Returns none
        """
        self.level = level
        self.hiddenNum = ""
        self.points = 10 # -1 each turn, acts as turnclock
        
        self.currentGuess = ""
        self.guesses = [] # items: strings of 3 digits ea.
        
        self.picos = {} # key: 3-digit guess,
                        # value: number of picos in guess    
        self.fermis = {} # key: 3-digit guess,
                         # value: number of fermis in guess  
        self.bagels = "" # string of single digits not in hiddenNum
        
        self.totalPlayerScore = 0
        self.totalCompScore = 0
        
        
    def remindScore(self):
        """
        Prints reminder of the current score.
        """
        print("You have " + str(self.points) + " points. Don't guess wrong or lose 1 point.") 
        # Currently just for player, not comp    
        
    def refreshVariables(self):
        self.hiddenNum = ""
        self.points = 10
        self.currentGuess = ""
        self.guesses[:] = []
        self.picos.clear()  # dict clear() function found via StackOverflow
        self.fermis.clear()
        self.bagels = ""
    
    def getHiddenNum(self):
        """
        Returns hidden number as a three digit string
        """
        return self.hiddenNum
    
    def validInput(self, text):
        """
        Checks if text is exactly three distinct digits
        Parameter:
            digits: a string to be checked
        Returns True if text is valid and False if not
        """
        checkRepeats = ""
        for i in range(len(text)):
            if text[i] not in "0123456789":  # if char not digit, return False
                    return False
            if text[i] in checkRepeats:      # if digit repeated, return False
                    return False
            checkRepeats += text[i]
        return len(text) == 3   # if len 3, return True
            
    def playerSetNum(self):
        """
        Sets hidden number by prompting user for input
        """
        finished = False    
        while finished == False:    #Repeats if input invalid
            inputString = input("Please pick a 3-digit number: ") # text generated from Story class?
            if self.validInput(inputString) == True:
                self.hiddenNum = inputString
                finished = True
            else:
                print("Sorry, that's not a 3 digit number. Enter 3 distinct digits.")
            
    def randSetNum(self):
        """
        Sets the hidden number to a random 3-digit string
        """
        firstNumber = str(random.randint(1, 9)) # no leading zero
        self.hiddenNum += firstNumber
        while len(self.hiddenNum) <=2:  # <= 2, first digit already generated
            addNumber = str(random.randint(0,9))    # could be a zero
            if addNumber not in self.hiddenNum:
                self.hiddenNum += addNumber
    
    def getResponse(self):
        """
        Reponds to the current guess (self.currentGuess) with picos, fermis, and bagels;
        updates variables
        """
        response = []   # list so it can be shuffled
        wrongDigits = 0 # if 3 wrong digits, say Bagels!
        for i in range (len(self.currentGuess)):    # iterates over 3 digits in guess
            if self.currentGuess[i] in self.hiddenNum and self.currentGuess[i] != self.hiddenNum[i]: # pico
                response.append("pico ")
                if self.currentGuess in self.picos:         # add guess:num of picos to picos dict
                    self.picos[self.currentGuess] += 1      # if first digit, create item
                else:                       
                    self.picos[self.currentGuess] = 1       # add to already-created item
                                                            # BUG: IF PLAYER GUESSES SAME GUESS REPEATEDLY, THESE COUNTS WILL GROW
            if self.currentGuess[i] == self.hiddenNum[i]:   # fermi
                response.append("fermi ")
                if self.currentGuess in self.fermis:
                    self.fermis[self.currentGuess] += 1
                else:
                    self.fermis[self.currentGuess] = 1
            if self.currentGuess[i] not in self.hiddenNum:
                wrongDigits += 1
        
        if wrongDigits >= 3:
            response.append("Bagels! ")
            self.bagels += self.currentGuess         
        
        random.shuffle(response)    # randomizes order of responses
        lineToPrint = ""            
        for i in range (len(response)):
            lineToPrint += response[i] + " "
        print(lineToPrint)
    
    def playerTurn(self):
        """
        The player takes their turn guessing numbers and geting responses
        """
        self.refreshVariables()
        self.randSetNum()
        print("Your opponent has chosen a number.")
        while self.currentGuess != self.hiddenNum and self.points >= 1: # repeat guessing
            self.remindScore()
            
            valid = False
            while valid == False:
                self.currentGuess = input("Your guess: ")  # updates self.currentGuess using text input
                checkOptions(self.currentGuess) # BUG: PRINTS INVALID IF OPTIONS ARE USED
                if self.validInput(self.currentGuess) == True:
                    valid = True
                else:
                    print("Invalid guess. Enter 3 distinct digits.")
            
            self.getResponse()
            if self.currentGuess != self.hiddenNum: # -1 point and repeat unless correct
                self.points -= 1
        
        if self.currentGuess == self.hiddenNum:
            print ("You got it! Relish your victory.")
            self.totalPlayerScore += self.points
        if self.points <= 0:
            print("You have been defeated.")
            # self.continueOrQuit() # prompts to replay or quit
    
    def randGuess(self):
        """
        Generates a string with 3 different digits
        Returns string of 3 distinct digits
        """
        randGuess = ""
        while len(randGuess) < 3:
            digit = str(random.randint(0,9))
            if digit not in randGuess:
                randGuess += digit
        return randGuess
    
    def playerResponse(self):
        """
        Player responds to AI guess, updates variables;
        CURRENTLY THE AI ONLY KNOWS WHAT PLAYER TELLS IT, PLAYER CAN LIE
        """
        confirmResponse = ""
        print("How do you respond? ie. pico's, fermi's, bagels")
        response = input("Your response: ")
        response.lower()
        responseList = response.split() # split into list to find responses
        
        while "pico" not in responseList and "fermi" not in responseList and "bagels" not in responseList:      # if reponse incorrect, try again
            response = input("Invalid response. Please try again: ")
            response.lower()
            responseList = response.split()
            
        while len(responseList) >= 1:   # if no more responses found, len set to 0
            if "pico" in responseList:
                confirmResponse += "Pico "
                if self.currentGuess in self.picos:
                    self.picos[self.currentGuess] += 1 
                else:
                    self.picos[self.currentGuess] = 1
                responseList.remove("pico")

            elif "fermi" in responseList:
                confirmResponse += "Fermi "
                if self.currentGuess in self.fermis:
                    self.fermis[self.currentGuess] += 1 
                else:
                    self.fermis[self.currentGuess] = 1
                responseList.remove("fermi")

            elif "bagels" in response:
                confirmResponse += "Bagels! "
                self.bagels += self.currentGuess
                response.remove("bagels") 

            else:
                del responseList[:] # list len set to 0
                
        print("You say: " + confirmResponse)
        
    def checkResponse(self):
        """
        Checks to see if a players reponse - pico's, fermi's, bagel's -
        are valid or if the player is cheating
        """
        pass
    
    def compGuess(self):
        """
        AI uses variables to make an educated guess
        """
    
    def compTurn(self):
        """
        The AI takes a turn, guessing and number
        and the player responses
        """
        self.refreshVariables()
        self.playerSetNum()
        while self.currentGuess != self.hiddenNum and self.points >= 1: # repeat guessing
            print("Your opponent has " + str(self.points) + " points left.")
            
            if self.currentGuess == "":
                self.currentGuess = self.randGuess()
            #INSERT INTENTIONAL GUESS
            
            print("Your opponent guesses " + self.currentGuess)
        
            if self.currentGuess == self.hiddenNum:
                print ("You got it! Relish your victory.")
                self.totalPlayerScore += self.points

            elif self.points <= 0:
                print("You have been defeated.")
                # self.continueOrQuit() # prompts to replay or quit
        
            else:
                self.points -= 1
        
            self.playerResponse()    
            
    
    def continueOrQuit(self):
        """
        Prompts player to continue playing, replay, or quit
        """
        pass
        
    
def main():
    gameOne = BagelsGame(1)
    #gameOne.randSetNum()
    #gameOne.playerSetNum()
    #gameOne.playerTurn()
    gameOne.compTurn()
    
if __name__ == "__main__":
    main()