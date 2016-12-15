"""
Author username(s): johnsoam ; Andrew Johnson
Date: 12/16/16
Final Project ReadMe File
Title: Bagels Revolution
"""

Bagels Revolution implements the game "Bagels" inside a narrative of class revolution.  The player plays 3 games of bagels against progressively more challenging AI (see note about AI below).  Each game consists of the player guessing a secret number chosen by the computer, and then the computer guessing a secret number chosen by the player.  More specific rules can be found both in the text of the code and are displayed when the game is run.  At any time while playing the game, the user can also enter "help" and will be asked if they would like to read the rules again.

Running the program: 
To play the program game simply run the bagels.py (with an appropriate python interpreter.) Player will be prompted to choose a character and start playing. 

Structural Overview:
The program relies on two classes: a Narrative class and a BagelsGame class. MORE ON CLASSES HERE!

Features:
The player can enter "help" or "exit" or "quit" at any point to either access the rules or quit the program.

While guessing the secret number, the player can also enter "hidden" to unlock the answer. This "cheat code" can help the player to advance quickly through the game in order to read the narrative.  However, there is no "cheat code" to advance when the computer is choosing the secret number. (This feature could be added with future development.)

A.I.:
The A.I. for the computer responding appropriate ("pico," "fermi," or "bagels") functions properly. I ran into significant difficulties implementing an A.I. for when the computer is guessing the secret number chosen by the player. I tried to store the information the computer receives from guessing as dictionaries, but I could not find a way for the computer to be properly utilizing information from not only the most recent guess but all previous guesses. After struggling with this for many hours, I decide to work around it by having the computer simply guess randomly numbers until, after a specified number of turns, it would guess the correct number. This can hardly be called an A.I., but I was looking for a way to get the game at least up and running. I spoke with George, and he suggested I could try assigning different probabilites to potentially values in each digit-space; this sounded like a great idea and an area of possible future development.

Narrative:
Writing the narrative was a highly satisfying part of this exercise. Playing through the game to get to all the narratives takes more time than you likely have, but I would encourage you take a look at them in the code if you are curious; that are near the top of the code in the "Narrative" class.