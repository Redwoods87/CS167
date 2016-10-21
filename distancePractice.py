import math

def distance (x1, y1, x2, y2):
    
    """
    this fuction finds the distance between two points
    
    Parameters:
        
    """
    
    distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return distance

print(distance(0, 0, 4, 0))


def tri_perimeter(x1, y1, x2, y2, x3, y3):
    side1 = distance (x1, y1, x2, y2)
    side2 = distance (x2, y2, x3, y3)
    side3 = distance (x1, y1, x3, y3)
    perim = side1 + side2 + side3
    
    return perim

print (tri_perimeter(2, 1, 5, 5, 5, 1))