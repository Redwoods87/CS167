"""
Author username(s): johnsoam ; temell
Date: Oct. 2, 2016
Assignment/problem number: Homework 7
Assignment/problem title: "Monte Carlo and Friends"
"""

import random

def pi_est(n):
    """
    Function estimates the digits of pi by creating random points and seeing how many fall within a given area.
    
    Parameters:
        n: number of random points (more points will estimate pi more accurately).
        
    Returns estimation of pi.
    """
    hit=0
    for i in range(n):
        x=random.random()
        y=random.random()
        if (x**2+y**2)<1:
            hit+=1
    return (hit*4)/n


def flip():
    """
    Function simulates a fair coin flip.

    Parameters: None
    
    Returns 1 for heads and 0 for tails.
    """
    coin=random.random()
    if coin>.5:         #Possibility of getting heads is 50%.
        return 1
    return 0
  

def six_heads():
    """
    Function simulates flipping a coin until 6 heads in a row are achieved.
    
    Parameters: None
    
    Returns number of total flips to get 6 heads in a row.
    """
    flips=0
    heads=0
    while heads<6: #Repeats until six consecutive heads are achieved.
        if flip()==1:
            heads+=1
        else:
            heads=0
        flips+=1
    return flips


def average_six(n):
    """
    Function calculates the average number of flips to get six consecutive heads.
    
    Parameters:
        n: Number of times to calculate the average of the results.
        
    Returns average number of flips required to get six consecutive heads.
    """
    total=0
    for i in range(n):
        total=total+(six_heads())
    return (total/n)

        
def hhh():
    """ 
    Funtion calculates the number of flips to get "heads, heads, heads" in a row. 

    Parameters: None

    Returns number of flips.
    """
    heads=0
    flips=0
    while heads < 3:    #Counts flips until three heads in a row.
        if flip()==1:
            heads+=1
        else:
            heads=0
        flips+=1
    return flips


def hht():
    """ 
    Funtion calculates the number of flips to get "heads, heads, tails" in a row. 

    Parameters: None

    Returns number of flips.
    """
    heads=0
    flips=0
    tails=0
    while tails<1:          #Repeats until return is triggered.
        while heads<2:      #Counts flips until two heads in a row.
            if flip()==1:
                heads+=1
            else:
                heads=0
            flips+=1
        if flip()==0:       #If tails after two heads returns flips.
            flips+=1
            return flips
        else:               #If heads after two heads goes back to the while loop.
            flips+=1
    
    
def simulate_flips(n):
    """
    Funtion calculates the average number of coin flips for "heads, heads, heads" and "heads, heads, tails."  Prints the averages for each.
    
    Parameters: 
        n: numbers of flips used to check the averages of each.
        
    Returns: None.
    """
    totalhhh=0
    totalhht=0
    for i in range(n):      #Calculates number of flips for each iternation of "n."
        totalhhh=totalhhh+(hhh())
        totalhht=totalhht+(hht())
    print ("HHH average: " + str(totalhhh/n) + "   HHT average: " + str(totalhht/n))
    
    
def main():
    print("pi_est: "+str(pi_est(1000)))
    print("flip: "+str(flip()))
    print("six_heads: "+str(six_heads()))
    print("average_six: "+str(average_six(1000)))
    print("hhh: "+str(hhh()))
    print("hht: "+str(hht()))
    simulate_flips(1000)
    
main()
