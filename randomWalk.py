import turtle
import random

t = turtle.Turtle ()

nLeft = 0
nRight = 0
nStraight = 0


for i in range (60):
    choice = random.random()
    if choice < 1/3:
        t.left(120)
        nLeft += 1
    elif choice < 2/3:
        t.right(120)
        nRight =+ 1
    else:
        nStraight += 1 
        
    t.forward(60)   # Always go forward
    
print ("Left:   " + "*"*nLeft)
print ("Right:   " + "*"*nRight)
print ("Straight:   " + "*"*nStraight)

    
t.screen.exitonclick()