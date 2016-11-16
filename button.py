# wget http://cs.whitman.edu/~davisj/cs/167/2016F/exmpls/button.py
from graphics import *

class Button(object):
    """Represents a button that can be clicked.
    """

    def __init__(self, location, width, height, color, text):
        """Button constructor
        Parameters:
            location, a Point
            width, an integer
            height, an integer
        """
        self.upperleft = location
        self.lowerright = Point(location.getX() + width,
                                location.getY() + height)
        self.center = Point(self.upperleft.getX()+.5*width, self.upperleft.getY()+.5*height)
        self.color = color
        self.rect = Rectangle(self.upperleft, self.lowerright)
        self.text = Text(self.center, text)

    def draw(self, window): 
        """Draw the button in the given window
        """
        self.rect.draw(window)
        self.rect.setFill(str(self.color))
        self.text.draw(window)
        
    def wasClicked(self, click):
        """Returns true if the given point is inside this button
        """
        return self.upperleft.getX() <= click.getX() <= self.lowerright.getX() \
           and self.upperleft.getY() <= click.getY() <= self.lowerright.getY()

def main():
    window = GraphWin("Buttons Test")
    quit_button = Button(Point(0,0), 100, 50, 'yellow', 'Quit')
    quit_button.draw(window)
    other_button = Button(Point(0, 50), 100, 10, 'red', '\"Hello world\"')
    other_button.draw(window)

    keep_running = True
    while keep_running:
        point = window.getMouse()
        if quit_button.wasClicked(point):
            keep_running = False
        elif other_button.wasClicked(point):
            print("Hello world!")

if __name__=='__main__':
    main()
