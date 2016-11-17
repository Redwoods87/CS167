'''
interfaces.py

Please mess around with this program, have fun with this game!

 by Andy Exley
'''

import sys
import graphics
import button 

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

        self.thrustButton = button.Button(graphics.Point(10,10), 200, 150, "Thrust!")
        self.thrustButton.draw(self.win)

    def show_info(self, lander):
        """This method currently gets the lander info then draws it.
        That's it. It doesn't actually show any information."""
        alt = lander.get_altitude()

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
        """This method waits for a user's mouse click then returns 0 thrust
            amount. You'll want to fix this to avoid catastrophic incidents."""
        self.win.getMouse()
        return 0

    def show_crash(self):
        """Crash message... change this to graphical message"""
        print("Crash! Oh noes!")

    def show_landing(self):
        """Landing message... change this to graphical message"""
        print("Hooray, the Eagle has landed!")

    def close(self):
        self.win.close()

    def create_surface(self):
        """Draws the surface of the moon"""
        rect = graphics.Rectangle(graphics.Point(5,0), graphics.Point(300,-10))
        rect.setFill("gray")
        return rect
