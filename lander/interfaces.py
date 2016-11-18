"""
Author username(s): johnsoam
Date: 11/17/16
Assignment/problem number: Homework 15
Assignment/problem title: Lunar Lander
"""

'''
modified from:

interfaces.py

Please mess around with this program, have fun with this game!

by Andy Exley
'''

"""
Note: I included the Button class in this file.
I modified the Button class from the one used in class as it was incomplete.
"""

import sys
import graphics


class Button(object):
    """Represents a button that can be clicked.
    """

    def __init__(self, location, width, height, text):
        """Button constructor
        Parameters:
            location, a Point
            width, an integer
            height, an integer
        """
        self.upperleft = location
        self.lowerright = graphics.Point(location.getX() + width,
                                location.getY() + height)
        self.rect = graphics.Rectangle(self.upperleft, self.lowerright)
        self.center = self.rect.getCenter()
        self.text = graphics.Text(self.center, text)

    def draw(self, window): 
        """Draw the button in the given window
        """
        self.rect.draw(window)
        self.text.draw(window)

    def wasClicked(self, click):
        """Returns true if the given point is inside this button
        """
        return self.upperleft.getX() <= click.getX() <= self.lowerright.getX() \
           and self.upperleft.getY() <= click.getY() <= self.lowerright.getY()



class TextLanderInterface:
    """Text-based interface for lander game. Use this one for testing"""

    def show_info(self, lander):
        """Display lander's status to user"""
        print ("Lander Status: Altitude %d, Velocity %d, Fuel %d" % 
            (lander.get_altitude(), lander.get_velocity(), lander.get_fuel()))

    def get_thrust(self):
        """Get thrust amount from user"""
        amtstr = input("Thrust amount?")
        return int(amtstr)

    def show_crash(self):
        """Display to user that we crashed"""
        print("Crash! Oh noes!")

    def show_landing(self):
        """Display to user that we landed safely"""
        print("Hooray, the Eagle has landed!")

    def close(self):
        """Close the interface"""
        print("Goodbye")



class GraphicLanderInterface:
    """GraphicLanderInterface class is a graphical interface 
        for your lunar lander game"""

    def __init__(self):
        """Constructor that initializes the graphics window
        and shapes that we will use for drawing things"""

        # initialize window
        self.win = graphics.GraphWin("Lunar Lander Game", 300, 500)
        # transform coordinates
        self.win.setCoords(0, -10, 300, 600)

        self.surface_polygon = self.create_surface()
        self.surface_polygon.draw(self.win)

        self.lander_polygon = None
        self.statusText = None

        #self.statusText = graphics.Text(graphics.Point (150, 570), "Status:" )
        #self.statusText.draw(self.win)    # This object is in show_info method

        self.thrustButton = Button(graphics.Point(110, 450), 80, 50, "Thrust!")
        self.thrustButton.draw(self.win)

        self.noThrustButton = Button(graphics.Point(90, 350), 120, 50, "No Thrust")
        self.noThrustButton.draw(self.win)

    def show_info(self, lander):
        """This method currently gets the lander info then draws it.
        That's it. It doesn't actually show any information."""
        alt = lander.get_altitude()
        vel = lander.get_velocity()
        fuel = lander.get_fuel()        
        
        if self.statusText: 
            self.statusText.undraw()
        self.statusText = graphics.Text(graphics.Point (150, 570), "Status: Alt: " + str(alt) + "; Vel: " + str(vel) + "; Fuel: " + str(fuel))
        self.statusText.draw(self.win)
        
        # if lander polygon is drawn, undraw it
        if self.lander_polygon:
            self.lander_polygon.undraw()
        self.lander_polygon = graphics.Polygon(graphics.Point(self.win.width / 2 - 10, alt),
                graphics.Point(self.win.width/2 - 3, alt + 10),
                graphics.Point(self.win.width/2 + 3, alt + 10),
                graphics.Point(self.win.width/2 + 10, alt))
        self.lander_polygon.setFill("blue")
        self.lander_polygon.draw(self.win)

    def get_thrust(self):
        """This method waits for a user's to click a button. 
        Returns 1 if thrust button is click.
        Returns 0 if the noThrust button is click.
        Clicking NOT on a button does nothing."""
    
        self.noButton = True        
        while self.noButton == True:
            clicked = self.win.getMouse()        
            if self.thrustButton.wasClicked(clicked) == True:
                return 1
            if self.noThrustButton.wasClicked(clicked) == True:
                return 0
             
    def show_crash(self):
        """Moves the lander to the ground and displays a crash message and fiery dots."""
        
        print("Crash! Oh noes!")
        
        self.crashText = graphics.Text(graphics.Point(150, 150), "CRASHED!")
        self.crashText.setStyle("bold italic")
        self.crashText.draw(self.win)
        
        #Draws colored circles for "explosion" effect
        self.boomOne = graphics.Circle(graphics.Point(30, 200), 20)
        self.boomOne.setFill("yellow")
        self.boomOne.draw(self.win)        
    
        self.boomTwo = graphics.Circle(graphics.Point(50, 100), 20)
        self.boomTwo.setFill("red")
        self.boomTwo.draw(self.win)  

        self.boomThree = graphics.Circle(graphics.Point(150, 250), 20)
        self.boomThree.setFill("red")
        self.boomThree.draw(self.win)  
        
        self.boomFour = graphics.Circle(graphics.Point(220, 100), 20)
        self.boomFour.setFill("red")
        self.boomFour.draw(self.win)  
        
        self.boomFive = graphics.Circle(graphics.Point(250, 200), 20)
        self.boomFive.setFill("yellow")
        self.boomFive.draw(self.win)  
        
        alt = 0
        # if lander polygon is drawn, undraw it
        if self.lander_polygon:
            self.lander_polygon.undraw()
        self.lander_polygon = graphics.Polygon(graphics.Point(self.win.width / 2 - 10, alt),
                graphics.Point(self.win.width/2 - 3, alt + 10),
                graphics.Point(self.win.width/2 + 3, alt + 10),
                graphics.Point(self.win.width/2 + 10, alt))
        self.lander_polygon.setFill("blue")
        self.lander_polygon.draw(self.win)        
        
        self.win.getMouse()

    def show_landing(self):
        """Moves the lander to the ground and displays a success message and celebratory dots."""
        
        print("Hooray, the Eagle has landed!")
        
        self.landText = graphics.Text(graphics.Point(150, 150), "SUCCESS!")
        self.landText.setStyle("bold italic")        
        self.landText.draw(self.win)
        
        #Draws colored circles for "success" effect
        self.successOne = graphics.Circle(graphics.Point(30, 200), 20)
        self.successOne.setFill("green")
        self.successOne.draw(self.win)        
    
        self.successTwo = graphics.Circle(graphics.Point(50, 100), 20)
        self.successTwo.setFill("blue")
        self.successTwo.draw(self.win)  

        self.successThree = graphics.Circle(graphics.Point(150, 250), 20)
        self.successThree.setFill("blue")
        self.successThree.draw(self.win)  
        
        self.successFour = graphics.Circle(graphics.Point(220, 100), 20)
        self.successFour.setFill("blue")
        self.successFour.draw(self.win)  
        
        self.successFive = graphics.Circle(graphics.Point(250, 200), 20)
        self.successFive.setFill("green")
        self.successFive.draw(self.win)          
        
        alt = 0
        # if lander polygon is drawn, undraw it
        if self.lander_polygon:
            self.lander_polygon.undraw()
        self.lander_polygon = graphics.Polygon(graphics.Point(self.win.width / 2 - 10, alt),
                graphics.Point(self.win.width/2 - 3, alt + 10),
                graphics.Point(self.win.width/2 + 3, alt + 10),
                graphics.Point(self.win.width/2 + 10, alt))
        self.lander_polygon.setFill("blue")
        self.lander_polygon.draw(self.win)          
        
        self.win.getMouse()

    def close(self):
        self.win.close()

    def create_surface(self):
        """Draws the surface of the moon"""
        rect = graphics.Rectangle(graphics.Point(5,0), graphics.Point(300,-10))
        rect.setFill("gray")
        return rect
