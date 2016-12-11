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

def intro():
    """
    Prints intro to game, prompts to choose side
    """
    pass
    
def rules():
    """
    Prints rules
    """
    pass
    
def help():
    """
    Prints rules and options to exit or continue
    """
    pass 

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
        self.hiddenNum = ""
        self.points = 10 # -1 each turn, acts as turnclock
        
        self.currentGuess = ""
        self.guesses = [] # items: strings of 3 digits ea.
        
        self.picos = {} # key: 3-digit guess,
                        # value: number of picos in guess    
        self.fermis = {} # key: 3-digit guess,
                         # value: number of fermis in guess  
        self.bagels = "" # string of single digits not in hiddenNum
        
        self.totalPlayerPoints = 0
        self.totalCompPoints = 0
        
        
    def remindScore(self):
        """
        Prints reminder of the current score.
        """
        print("You have " + str(self.points) + " points. Don't guess wrong or lose 1 point.") 
        # Currently just for player, not comp    
        
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
        allNum = True
        for i in range(len(text)):
            if text[i] not in "0123456789":  # is char a digit?
                    allNum = False
        return len(inputString) == 3 and allNum == True
            
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
                print("Sorry, that's not a 3 digit number. Remember each digit can appear only once.")
            
    def randSetNum(self):
        """
        Sets the hidden number to a random 3-digit string
        """
        firstNumber = str(random.randint(1, 9)) # No leading zero
        self.hiddenNum += firstNumber
        while len(self.hiddenNum) <=2:  # <= 2, first digit already generated
            addNumber = str(random.randint(0,9))    # Could be a zero
            if addNumber not in self.hiddenNum:
                self.hiddenNum += addNumber
        # print(self.hiddenNum) #PRINT TEST
    
    def getResponse(self):
        """
        Reponds to the current guess (self.currentGuess) with picos, fermis, and bagels;
        updates variables
        """
        wrongDigits = 0 # if 3 wrong digits, say Bagels!
        for i in range (len(self.currentGuess)):
            if self.currentGuess[i] in self.hiddenNum and self.currentGuess[i] != self.hiddenNum[i]: # Pico
                print("Pico ")
                if self.currentGuess in self.picos:
                    self.picos[self.currentGuess] += 1
                else:
                    self.picos[self.currentGuess] = 1
            if self.currentGuess[i] == self.hiddenNum[i]:    # Fermi
                print("Fermi ")
                if self.currentGuess in self.fermis:
                    self.fermis[self.currentGuess] += 1
                else:
                    self.fermis[self.currentGuess] = 1
            if self.currentGuess[i] not in self.hiddenNum:
                wrongDigits =+ 1
        if wrongDigits >= 3:
            print("BAGELS! ")
            self.bagels += self.currentGuess         
    
    def playerTurn(self):
        """
        The player takes their turn guessing numbers and geting responses
        """
        self.points = 10 # reset to 10 points
        self.randSetNum()
        while self.currentGuess != self.hiddenNum and self.points >= 0:
            self.remindScore()
            self.currentGuess = input("Your guess: ")  # Updates self.currentGuess using text input
            self.getResponse()
            if self.currentGuess != self.hiddenNum:
                self.points -= 1
        
        if self.currentGuess == self.hiddenNum:
            print ("You got it! Relish your victory.")
            self.totalPlayerPoints += self.points
        if self.points <= 0:
            print("You have been defeated.")
            # self.continueOrQuit() # prompts to replay or quit
    
    def compTurn(self):
        """
        The AI takes a turn, guessing and number
        and the player responses
        """
        pass
    
    def continueOrQuit(self):
        """
        Prompts player to continue playing, replay, or quit
        """
        pass
        
    
def main():
    gameOne = BagelsGame(1)
    #gameOne.randSetNum()
    #gameOne.playerSetNum()
    gameOne.playerTurn()
    
    
if __name__ == "__main__":
    main()