data = [1,2,3,4,5,6,7,8]
data2 = ['Tris', 'Tobias', 'Caleb']

"""
print(len(data))

print(data[2])

print(data[-1])

print(data[-3:])

print(data[:4])

print(data[1:4])
"""


def sumList(data):
    listLength = len(data)
    sum = 0
    for item in range (listLength):
        sum = sum + data[item] 
    return sum

print(sumList(data))

def sumOdds(data):
    listLength = len(data)
    sum = 0
    for item in range (listLength):
        if data[item]%2 == 1:
            sum = sum + data[item]
        else:
            sum = sum
    return sum

print (sumOdds(data))

def countOdds(data):
    listLength = len(data)
    count = 0
    for item in range (listLength):
        if data[item]%2 == 1:
            count = count + 1
    return count

print (countOdds(data))

def search (data, target):
    listLength = len(data)
    for item in range (listLength):
        if data[item] == target:
            return True
        else:
            return False
        
#print (search(data2, "Tris"))
#print (search(data2, "Peter"))

def search2 (data, target):
    listLength = len(data)
    for item in range (listLength):
        if data[item] == target:
            return item
    return -1
    
# print (search2(data2, "Peter"))

def percentile(data, value):
    listLength = len(data)
    lesserValues = 0
    for item in range (listLength):
        if data[item] <= value:
            lesserValues = lesserValues + 1
        else: 
            lesserValues = lesserValues
    percentile = lesserValues / listLength * 100
    return percentile

print (percentile(data, 5))

def meanSquares(data):
    listLength = len(data)
    sum = 0
    for item in range (listLength):
        sum = sum + (data[item] ** 2)
    mean = sum / listLength
    return mean

print (meanSquares(data))

def mean(data):
    listLength = len(data)
    sum = 0
    for item in range (listLength):
        sum = sum + data[item]
    mean = sum / listLength
    return mean

def variance (data):
    