# wget http://cs.whitman.edu/~davisj/cs/167/2016F/exmpls/compare.py

# Source: Jesse Havill (2016), _Discovering Computer Science_, p. 277
#         Exercise 6.4.1

def compare(word1, word2):
  index = 0
  steps = 3   # number of comparisons
  while index < len(word1) and \
        index < len(word2) and \
        word1[index] == word2[index]:  # character comparison
    steps += 3
    index += 1

  if index == len(word1) and index == len(word2):   # case 1: ==
    print(word1, 'and', word2, 'are equal.')
    steps += 2
  elif index==len(word1) and index < len(word2):    # case 2: <
    print(word1, 'comes before', word2)
    steps += 2
  elif index==len(word2) and index < len(word1):    # case 3: >
    print(word1, 'comes after', word2)
    steps += 2
  elif word1[index] < word2[index]:                  # case 4: <
    print(word1, 'comes before', word2)
    steps += 1
  else: # word2[index] < word1[index]:               #case 5: >
    print(word1, 'comes after', word2)
    steps += 1

  print('Number of comparisons =', steps)

compare('canoeing','canoe')

