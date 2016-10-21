# Type this command in bash to get a copy of this file:
# wget http://cs.whitman.edu/~davisj/cs/167/2016F/exmpls/randomness.py

import random
import time

def winner(votes1, votes2):
  # Code from textbook exercise 5.1.8
  if votes1 > votes2:
    print('Candidate one wins!')
  elif votes1 < votes2:
    print('Candidate two wins!')
  else:
    print('There was a tie.')

def loaded():
  """
  Simulates a roll of a dice loaded to come up 1 or 6 half the time
  """
  r = random.random()
  if r < 0.25:
    return 1
  elif r < 0.5:
    return 6
  elif r < 0.625:
    return 2
  elif r < 0.75:
    return 3
  elif r < 0.875:
    return 4
  else:
    return 5

def printLoadedHistogram(n):
  ones = 0
  twos = 0
  threes = 0
  fours = 0
  fives = 0
  sixes = 0
  for count in range(n):
    value = loaded()
    if value is 1:
      ones += 1
    elif value is 2:
      twos += 1
    elif value is 3:
      threes += 1
    elif value is 4:
      fours += 1
    elif value is 5:
      fives += 1
    else:
      sixes += 1
  print(ones*"=")
  print(twos*"=")
  print(threes*"=")
  print(fours*"=")
  print(fives*"=")
  print(sixes*"=")
  
def lehmer(r,m,a):
  """
  r = seed or previous random number
  m = a prime number
  a = any integer between 1 and m-1
  """
  return (a*r) % m

def lehmerSequence(r,m,a,n):
  """n is the number of trials"""
  results = []		# initialization (to an empty list)
  for i in range(n):
    r = lehmer(r,m,a)
    results.append(r)	# update (appends to the list)
  return results	

def parkMillerSequence(length, seed):
  r = seed
  m = 2**31 - 1
  a = 16807
  randList = []
  for index in range(length):
    r = lehmer(r,m,a)
    randList.append(r)
  return randList

def scaledParkMillerSequence(length, seed, stop):
  r = seed
  m = 2**31 - 1
  a = 16807
  randList = []
  for index in range(length):
    r = lehmer(r,m,a)
    randList.append(r % stop)
  return randList

