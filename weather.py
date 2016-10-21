import random

def weather ():
    chance = random.random()
    if chance < 0.66:
        print("SNOW")
    elif chance < 0.99:
        print ("SUNNY DAY")
    else:
        print("RAINS CATS AND DOGS!")
        
def loaded():
    chance = random.random()
    if chance < 0.25:
        roll = 1
    elif chance < 0.50:
        roll = 6
    elif chance < 0.625:
        roll = 2
    elif chance < 0.75:
        roll = 3
    elif chance < 0.875:
        roll = 4
    else:
        roll = 5
        
    return roll

def roll():
    chance = random.random()
    if chance < 1/6:
        roll = 1
    elif chance < 2/6:
        roll = 6
    elif chance < 3/6:
        roll = 2
    elif chance < 4/6:
        roll = 3
    elif chance < 5/6:
        roll = 4
    else:
        roll = 5
        
    return roll



def diceHistogram (trials):

    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    eleven = 0
    twelve = 0

    for i in range (trials):
        diceValue = roll() + roll()
        if diceValue == 2:
            two = two + 1
        if diceValue == 3:
            three += 1
        if diceValue == 4:
            four += 1
        if diceValue == 5:
            five += 1
        if diceValue == 6:
            six += 1
        if diceValue == 7:
            seven += 1
        if diceValue == 8:
            eight += 1
        if diceValue == 9:
            nine += 1
        if diceValue == 10:
            ten += 1
        if diceValue == 11:
            eleven += 1
        if diceValue == 12:
            twelve += 1
            
    
    
    print ("Two's:   " + "*"*two)
    print ("Three's:   " + "*"*three)
    print ("Four's:   " + "*"*four)
    print ("Five's:   " + "*"*five)
    print ("Six's:   " + "*"*six)
    print ("Seven's:   " + "*"*seven)
    print ("Eight's:   " + "*"*eight)
    print ("Nine's:   " + "*"*nine)
    print ("Ten's:   " + "*"*ten)
    print ("Eleven's:   " + "*"*eleven)
    print ("Twelve's:   " + "*"*twelve)
   
diceHistogram (300)
