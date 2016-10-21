"""
Author username(s): johnsoam ; linnrc
Date: Sept. 18, 2016
Assignment/problem number: Homework 5
Assignment/problem title: Playful Polygons
"""

"""
This program contains two predominant functions with smaller functions to support them. spin_polygon draws multiple polygons around a central point, rotating between each iteration. scale_polygon draws multiple increasingly larger polygons scaling at a set rate. (You will need to comment out the appropriate function to switch tasks below.)

Parameters:
    tortoise: inputs the already created turtle.
    n_sides: the number of sides of the desired polygon.
    side_length: the length of one side of the desired polygon.
    angle: the angle to rotate the turtle between drawing iterations of polygons.
    n_copies: the number of copies to make of the desired polygon.
    scale_factor: the amount by which to multiply the polygon's side length between iterations.

Return value: 
    none

"""

import turtle
tina = turtle.Turtle()

def calc_angle(n_sides):    #calculates the angle of a polygon with n sides
    angle = 360 / n_sides
    return angle

def draw_polygon(tortoise, n_sides, side_length):  #draws a polygon with n sides
    angle = calc_angle(n_sides)
    for segment in range (n_sides):
        tortoise.forward(side_length)
        tortoise.left(angle)

def spin_polygon(tortoise, n_sides, side_length, angle, n_copies): #draws n polygons around a central point
    for segment in range (n_copies):
        draw_polygon(tortoise, n_sides, side_length)
        tortoise.right(angle)
        
def scale_polygon(tortoise, n_sides, side_length, scale_factor, n_copies): #draws increasingly larger scaling polygons 
    for segment in range(n_copies):
        draw_polygon(tortoise, n_sides, side_length)
        side_length = scale_factor * side_length
        
# spin_polygon(tina, 6, 50, 30, 8)
scale_polygon(tina, 6, 5, 2, 6)
