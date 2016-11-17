'''
lander.py

This is a program that allows you to play the lunar lander game.

You should be able to play the text version with the files that you 
download.

'''

import interfaces

class LunarLander:
    '''
    This class represents a lunar lander object that keeps track
    of its own altitude, velocity and fuel.
    '''

    def __init__(self, a, v, f):
        self.alt = a
        self.vel = v
        self.fuel = f

    def get_altitude(self):
        return self.alt

    def get_velocity(self):
        return self.vel

    def get_fuel(self):
        return self.fuel

    def update(self, thrust):
        '''Update the lander object's altitude, velocity and fuel
        based on firing the rockets using the given amount of fuel units.'''

        if thrust > self.fuel:
            thrust = self.fuel
        self.fuel -= thrust
        self.vel = self.vel - 2 + thrust * 4
        self.alt += self.vel
        if self.alt < 0:
            self.alt = 0

class LanderGame:
    '''This class contains the logic needed to play the lunar lander game.'''

    def __init__(self):
        '''This is the constructor for the LanderGame class. 
        To change the program to work with your graphical 
        interface, you'll need to uncomment the line
        of this constructor that refers to the GraphicLanderInterface.'''
        self.interface = interfaces.TextLanderInterface()
        self.interface = interfaces.GraphicLanderInterface()
        self.lander = LunarLander(200, 0, 30)

    def play(self):
        '''Plays the game'''
        while self.lander.get_altitude() > 0:
            self.interface.show_info(self.lander)
            amt = self.interface.get_thrust()
            self.lander.update(amt)
        if self.lander.get_velocity() < -10:
            self.interface.show_crash()
        else:
            self.interface.show_landing()
        self.interface.close()

def main():
    game = LanderGame()
    game.play()

if __name__ == '__main__':
    main()
