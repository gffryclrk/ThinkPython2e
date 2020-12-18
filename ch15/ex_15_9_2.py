"""Think Python, 2nd Ed.
Chapter 15, Exercise 2

Write a function called draw_rect that takes a Turtle object and a
Rectangle and uses the Turtle to draw the Rectangle. See Chapter 4 for
examples using Turtle objects.

Write a function called draw_circle that takes a Turtle and a Circle
and draws the Circle."""

import turtle

import sys
sys.path.append('ch15/')
sys.path.append('ch4/')
import rectangle
from exercises import circle

class Circle():
    """ Round geometrical figure """

    
class Point():
    """ Ordered pair """

def draw_rect(t, r):
    """Uses turtle to draw rectangle"""
    for a in range(2):
        t.fd(r.height)
        t.lt(90)
        t.fd(r.width)
        t.lt(90)

def draw_circle(t, c):
    """Use turtle to draw circle using chapter 4 exercise solution"""
    circle(t, c.radius)
    
    
if __name__ == '__main__':
    t = turtle.Turtle()

    box = rectangle.Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    draw_rect(t, box)

    c = Circle()
    c.radius = 100

    draw_circle(t, c)
    turtle.exitonclick()
