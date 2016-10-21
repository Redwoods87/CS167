import turtle
import random 

def lehmer(r,m,a):
  """
  r = seed or previous random number
  m = a prime number
  a = any integer between 1 and m-1
  """
  return (a*r) % m

def testRandom(seed, n):
    """
    DOCSTRING    
    """
    tortoise = turtle.Turtle()
    screen = tortoise.getscreen()
    screen.setworldcoordinates(0, 0, 1, 1)
    screen.tracer(100)   #only draw every 100 updates
    tortoise.up()
    tortoise.speed(0)
    r = seed
    m = 2**31 - 1
    a = 16807
    for i in range(n):
        r = lehmer(r,m,a)
        x = (lehmer(r,m,a))/m
        r = lehmer(r,m,a)
        y = (lehmer(r,m,a))/m
        tortoise.goto(x, y)
        tortoise.dot()
        
    
    screen.update()   #ensure all updates are drawn
    screen.exitonclick()
    
testRandom(3,2**30)
    