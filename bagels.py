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


TO DO: 
Write continueOrQuit()
write confirmResponse()
write narratives()
add print hiddenNum if successful for confirmation - DONE
remove print tests from pico responses - DONE
print total score between turns - DONE
how to pass total scores between rounds -DONE
write credits? (include Emma Lazarus, "The New Colossus" referenced in protestors story)
WRITE SECRET BACKDOOR TO GET HIDDENNUM
"""

import random
import sys


class Narrative:
    """
    A class that provides the narrative content of a game of Bagels Revolution.
    """
    
    def __init__(self, storyline):
        """
        Initializes a Narrative object
        Parameters:
            storyline: a single integer (1 or 2) determines object storyline;
                [1] : A Billionaire Mucky-Muck
                [2] : A Swarm of Angry Protestors
        Returns None
        """
        self.storyline = storyline
        
    def openingText(self):
        """
        Prints the opening to the chosen storyline
        """
        if self.storyline == 1: # billionaire
            print("\nYou are $$$ Billionaire Damien Fascistman $$$. You have mountains of money \
from exploiting other countries and manipulating the fossil fuel industry.\n\n\
But money is not enough. You crave power. You set off on your quest for global domination.\n\n\
Your first opponent is the MASS MEDIA.  Round One: Fight!\n\n\
---------------------------")
            
        elif self.storyline == 2: # protestors
            print("\nYou are: !!!The Tired, The Poor, The Huddled Masses!!! Zounds of you \
fill the street across the country. Frustrated with the polical system and the rich \
bastards that run the country, you begin to organize yourselves. \n\n\
Your first opponent is the MASS MEDIA.  Round One: Fight!\n\n\
---------------------------")
            
    
    def firstWin(self):
        """
        Prints the transition text after winning level 1       
        """
        if self.storyline == 1: # billionaire
            print("\nYour expertise in cat videos and skill in trolling the internet\
allows you to get more views on MySpace than anyone in years. The mainstream media\
cannot keep up with your onslaught of tweeters is unstoppable. You are the master twit!\n\n\
With communications under your control, you face your next opponent:\n\n\
A MORASS OF ENTRENCHED POLITICIANS -- Round Two: Fight!\n\n")
            
        elif self.storyline == 2: # protestors
            print("")        
        
    def firstLoss(self):
        """
        Prints the transition text after losing level 1      
        """        
        if self.storyline == 1: # billionaire
            print("The Mass Media drowns out your elitist jabberings. Everyone blocks \
you on Facebook and you retreat into the tunnels and caves under you mountain of gold.")
            
        elif self.storyline == 2: # protestors
            print("")
       
       
    def secondWin(self):
        """
        Prints the transition text after winning level 2       
        """
        if self.storyline == 1: # billionaire
            print("")
            
        elif self.storyline == 2: # protestors
            print("")
        
    def secondLoss(self):
        """
        Prints the transition text after losing level 2  
        """
        if self.storyline == 1: # billionaire
            print("")
            
        elif self.storyline == 2: # protestors
            print("")


    def thirdWin(self):
        """
        Prints the final text after winning level 3       
        """
        if self.storyline == 1: # billionaire
            print("")
            
        elif self.storyline == 2: # protestors
            print("")
        
    def thirdLoss(self):
        """
        Prints the final text after losing level 3   
        """
        if self.storyline == 1: # billionaire
            print("")
            
        elif self.storyline == 2: # protestors
            print("")



class BagelsGame:
    """
    A class that manages the mechanics of the game
    
    Each object is given a level of
    difficulty (1, 2, or 3)
    """
    
    def __init__(self, level, startingScores):
        """
        Constructor that creates a level of the game
        Parameter:
            level:  a string ("1", "2", or "3")that determines 
                    the difficulty of the game
            startingScores: takes a tuple with 2 items as integers
                            (playerScore, compScore)        
        Returns None
        """
        self.level = level
        self.hiddenNum = ""
        self.points = 10 # -1 each turn, acts as turnclock
        
        self.currentGuess = ""
        self.guesses = [] # items: strings of 3 digits ea.
        
        self.picosList = [] # list of single digits in guesses with picos   
        self.fermis = {} # key: 3-digit guess,
                         # value: number of fermis in guess  
        self.availableDigits = "0123456789" # string digits not eliminated by "bagels"
        self.compTurnCount = 9 - level # turns until comp guesses correctly
        
        self.totalPlayerScore = startingScores[0] #1st tuple value  # level 1 gets 8 turns, 2 gets 7, and 3 gets 6
        self.totalCompScore = startingScores[1] #2nd tuple value
        
    def getTotalScores(self):
        """
        Accesses the total scores of both the player and the computer
        Returns a tuple (totalPlayerScore, totalCompScore), each an integer
        """
        return (self.totalPlayerScore, self.totalCompScore)
    
    def getHiddenNum(self):
        """
        Returns hidden number as a three digit string
        """
        return self.hiddenNum    
    
    def remindScore(self):
        """
        Prints reminder of the current score.
        """
        print("\nYou have " + str(self.points) + " points. Don't guess wrong or lose 1 point.") 
        # Currently just for player, not comp    
        
    def refreshVariables(self):
        self.hiddenNum = ""
        self.points = 10
        self.currentGuess = ""
        self.guesses[:] = []
        self.picosList[:] = []
        self.fermis.clear()
        self.availableDigits = "0123456789"
        self.compTurnCount = 9 - self.level
        
    def setTotalScores(self, scoresTuple):
        """
        Resets the total scores for an already created game object
        Parameter:
            scoresTuple: a tuple of two integers denoting the scores (playerScore, compScore)
        """
        self.totalPlayersScore = scoresTuple[0]
        self.totalCompScore = scoresTuple[1]
    
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
            inputString = input("Pick a 3-digit number for your opponent to guess: ") # text generated from Story class?
            checkOptions(inputString)            
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
                response.append("Pico ")
                for i in range(len(self.currentGuess)):
                    if self.currentGuess[i] not in self.picosList:
                        self.picosList.append(self.currentGuess[i])

            elif self.currentGuess[i] == self.hiddenNum[i]:   # fermi
                response.append("Fermi ")
                if self.currentGuess in self.fermis:
                    self.fermis[self.currentGuess] += 1
                else:
                    self.fermis[self.currentGuess] = 1
            
            elif self.currentGuess[i] not in self.hiddenNum:
                wrongDigits += 1
        
        if wrongDigits >= 3:
            response.append("Bagels! ")
            for i in range (len(self.currentGuess)):
                if self.currentGuess[i] in self.availableDigits:
                    self.availableDigits.replace(self.currentGuess[i], "")
            #self.avi += self.currentGuess         
        
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
        print("\nIt's your turn.\n\nYour opponent has chosen a secret number.")
 
        while self.currentGuess != self.hiddenNum and self.points >= 1: # repeat guessing
            self.remindScore()
            
            valid = False
            while valid == False:
                self.currentGuess = input("Your guess: ")  # updates self.currentGuess using text input
                checkOptions(self.currentGuess) # BUG: PRINTS INVALID IF OPTIONS ARE USED
                if self.validInput(self.currentGuess) == True:
                    valid = True
                else:
                    print("\nInvalid guess. Enter 3 distinct digits.\n")
            
            self.getResponse()
            if self.currentGuess != self.hiddenNum: # -1 point and repeat unless correct
                self.points -= 1
        
        if self.currentGuess == self.hiddenNum:
            print ("\nYou got it! The hidden number was: " + self.hiddenNum + ". Relish your victory.\n")
            print (str(self.points) + " points have been added to your total score")
            print ("Your total score: " + str(self.totalPlayerScore))
            self.totalPlayerScore += self.points
        
        if self.points <= 0:
            print("\nYou have been defeated. The secret number was " + self.hiddenNum + ".")
            print ("Your total score: " + str(self.totalPlayerScore) + "\n")
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
        checkOptions(response)        
        responseList = response.split() # split into list to find responses
        
        while "pico" not in responseList and "fermi" not in responseList and "bagels" not in responseList:      # if reponse incorrect, try again
            response = input("Invalid response. Please try again: ")
            response.lower()
            checkOptions(response)
            responseList = response.split()
            
        while len(responseList) >= 1:   # if no more responses found, len set to 0
            if "pico" in responseList:
                confirmResponse += "Pico "
                for i in range(len(self.currentGuess)):
                    if self.currentGuess[i] not in self.picosList:
                        self.picosList.append(self.currentGuess[i])
                    
                """
                if self.currentGuess in self.picos:
                    self.picos[self.currentGuess] += 1 
                else:
                    self.picos[self.currentGuess] = 1
                """
                
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
                for i in range(len(self.currentGuess)):
                    if self.currentGuess[i] in self.availableDigits:
                        self.availableDigits.replace(self.currentGuess[i], "")
                responseList.remove("bagels") 

            else:
                del responseList[:] # list len set to 0
                
        print("You say: " + confirmResponse)

        
    def confirmResponse(self):
        """
        Checks to see if a players reponse - pico's, fermi's, bagel's -
        is valid or if the player is cheating
        """
        pass
    
    def compGuess(self):
        """
        AI uses variables to make an educated guess
        Returns guess as a 3-character string
        FIXED BUG: COMP WAS GENERATING 0's AS FIRST DIGIT
        """
        nextGuess = ["x", "x", "x"]     # will be used to generate next guess
        openIndices = [0, 1, 2]

        
        if len(self.fermis) > 0:
            for i in range(self.fermis[self.currentGuess]): # first use fermis, repeat for fermi in guess
                pickedIndex = random.choice(openIndices)    # pick random index to keep fermi
                openIndices.remove(pickedIndex)             # remove the index remaining unchanged
                nextGuess[pickedIndex] = self.currentGuess[pickedIndex]

        for i in range (len(openIndices)):
            guessedDigit = "x"
            while nextGuess[openIndices[i]] == "x":
                guessedDigit = random.choice(self.availableDigits)
                repeated = False                
                for x in range(len(nextGuess)): # x not i becuase we have multiple for loops
                    if nextGuess[x] == guessedDigit:    # checks for repeats
                        repeated = True
                if repeated == False:
                    nextGuess[openIndices[i]] = guessedDigit
     
        while nextGuess[0] == "0":
            nextGuess[0] = random.choice(self.availableDigits)
            
        return "".join(nextGuess)
    
        
        """ COULDN'T GET A FUNCTIONAL PICO ALGORITHM
        tempPicosList = self.picosList  # then address picos, tempList so we can modify locally
        for i in range (len(openIndices)):   # use the remaining indices of nextGuess

            while nextGuess[openIndices[i]] == "x": #and first digit not 0 and no repeats?
                if len(tempPicosList) > 0:
                    guessedDigit = random.choice(tempPicosList)
                    tempPicosList.remove(guessedDigit)

                else:
                    guessedDigit = random.choice(self.availableDigits)
            
                nextGuess[openIndices[i]] = guessedDigit
        """


    def compTurn(self):
        """
        The AI takes a turn, guessing and number
        and the player responses
        """
        self.refreshVariables()
        self.playerSetNum()
        while self.currentGuess != self.hiddenNum and self.points >= 1: # repeat guessing
            print("\nIt's your opponent's turn.\n\nYour opponent has " + str(self.points) + " points left.\n")
            
            if self.currentGuess == "":
                self.currentGuess = self.randGuess()
            elif self.compTurnCount <= 0:
                self.currentGuess = self.hiddenNum
            else:
                self.currentGuess = self.compGuess()
            
            print("Your opponent guesses " + self.currentGuess + "\n")
    
            if self.currentGuess == self.hiddenNum:
                print ("Your opponent guessed correctly.")
                print ("\n" + str(self.points) + " points have been added to their total score.")
                print ("Opponent's total score: " + str(self.totalCompScore))
                self.totalCompScore += self.points
            
            elif self.points <= 0:  # currently AI will not fail
                print("Your opponent has failed.\n")
                # self.continueOrQuit() # prompts to replay or quit
           
            else:
                self.points -= 1
                self.compTurnCount -= 1
                self.playerResponse()    
        
    def __del__(self):
        """
        Destorys the game object
        """
    
def rules():
    """
    Prints rules
    """
    print("\n\nHOW TO PLAY BAGELS (modified from armoredpenguin.com): \n\n \
1. There are two opponents, the player and the computer. One picks a number, and the other \
tries to guess the number. The opponent picking the number must \
give accurate responses to the guesses. \n\n \
2. The opponent picking a number chooses a three digit number. (In this \
version, there may be no leading zeros, and digits may not be repeated.)\n\n \
3. The opponent guessing the number gives a three digit number. \n\n \
4. The opponent who picked the number answers: \n\n \
- Fermi : One of the digits in the guess matches one of the digits in the \
answer, and it is in the correct position. \n\n \
- Pico : One of the digits in the guess matches one of the digits in the answer, \
but the digit is not in the correct place. \n\n \
- Bagels : None of the digits in the guess match any of the digits in the answer. \n\n \
Multiple answers may come out of a single guess. For example, the person answering \
might say, 'Pico Pico,' 'Pico Pico Pico,' or 'Fermi Fermi Pico,' in no particular \
order. \n\n \
5. Opponents take turns holding each role. The opponent guessing has up to \
10 guesses before they lose and can win up to 10 points depending on how \
many guesses before they guess correctly. If their first guess is correct, they \
receive 10 points added to their total score. They will receive 1 less point for \
each turn it takes them until they answer correctly. \n\n")
        

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
    
def intro():
    """
    Prints intro to game, prompts to choose side
    Returns: an integer (1 or 2) determining while storyline to use
    """
    print("\n\nBAGELS REVOLUTION \n\nTHE NUMBER-GUESSING GAME\nOF POLITICAL POWER \n")
    rules()
    play = input("Would you like to play? : ")
    if play.lower() == "no" or play.lower() == "n":
        sys.exit("\nGoodbye for now.")
    else:
        print("\nGreat, let's get started.")
        
    charChoice = 0

    while charChoice != "1" and charChoice != "2":    
        charChoice = input("\nPlease choose a character to play: \n\n\
Enter [1] for 'A Billionaire Mucky-Muck' \
\n                 or \nEnter [2] for 'A Swarm of Angry Protestors' \n\nChoice: ")
        checkOptions(charChoice)
    
    return int(charChoice)


def playRound(gameRound, story):
    """
    Plays a round of bagels, player and computer each get a turn, player first
    Parameters:
        bagelsGame: an object of the BagelsGame class
        story: an object of the Narrative class
    Returns True if player wins and False if player loses
    """   
    gameRound.playerTurn()
    gameRound.compTurn()
    scores = gameRound.getTotalScores() # scores is a tuple (player scores, comp scores)
    print ("\nFinal points from round: \nYou got " + str(scores[0]) + " points.\n\
Your opponent got " + str(scores[1]) + " points.\n")     
    if scores[0] > scores[1]:
        print ("You won the round!")        
        return True
    elif scores[0] < scores[1]:
        print ("You lost the round.")        
        return False
    else:
        print("You tie, but that's not good enough. You lose.")
        return False
        
    """
def continueOrQuit(currentRound, previousScore):
    
    Prompts player to continue playing, replay, or quit
    Parameters: 
        currentRound: a BagelsGame object to be played
        previousScore: a tuple of two integers (playersScore, CompScore)
    
    print("Unfortunately your rise to power has been quashed.\n\n")
    continueOrExit = input("Would you like to try this level again? (Yes or No) : ")
    if continueOrExit.lower() == "yes" or continueOrExit.lower() == "y":
        currentRound.setTotalScores() # PROBLEM RESETTING SCORES, LEAVE FOR NOW
    """
    
def main():
    storyChoice = intro() # intro() returns 1 or 2, determines storyline
    story = Narrative(storyChoice)
    story.openingText()    
    
    roundOne = BagelsGame(1, (0,0)) # starting scores start at 0   
    firstOutcome = playRound(roundOne, story)
    if firstOutcome == True:
        roundTwo = BagelsGame(2, roundOne.getTotalScores())
        secondOutcome = playRound(roundTwo, story)
        if secondOutcome == True:
            roundThree = BagelsGame(3, roundTwo.getTotalScores())
            thirdOutcome = playRound(roundThree, story)
            if thirdOutcome == True:
                story.thirdWin()
            else:
                story.thirdLoss()
        else:
            story.secondLoss()
    else:
        story.firstLoss()

    
if __name__ == "__main__":
    main()