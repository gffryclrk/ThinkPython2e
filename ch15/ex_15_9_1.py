"""Think Python, 2nd Ed.
15.9  Exercises
Exercise 1  

Write a definition for a class named Circle with attributes center and
radius, where center is a Point object and radius is a number.

Instantiate a Circle object that represents a circle with its center
at (150, 100) and radius 75.

Write a function named point_in_circle that takes a Circle and a Point
and returns True if the Point lies in or on the boundary of the
circle.

Write a function named rect_in_circle that takes a Circle and a
Rectangle and returns True if the Rectangle lies entirely in or on the
boundary of the circle.

Write a function named rect_circle_overlap that takes a Circle and a
Rectangle and returns True if any of the corners of the Rectangle fall
inside the circle. Or as a more challenging version, return True if
any part of the Rectangle falls inside the circle.

Solution: http://thinkpython2.com/code/Circle.py.

"""
import math
import pdb

class Point:
    """ ordered pair"""
    
class Circle:
    """ Has a radius and centre"""

def point_in_circle(circle, point):
    """takes a Circle and a Point
    and returns True if the Point lies in or on the boundary of the
    circle."""
    return math.sqrt((point.x - circle.centre.x)**2 + (point.y - circle.centre.y)**2) <= circle.radius
    
if __name__ == '__main__':
    c = Circle()
    c.centre = Point() # This book hasn't taught how to use constructors yet
    c.centre.x = 150
    c.centre.y = 100
    c.radius = 75

    point_on_c = Point()
    point_on_c.x = 150
    point_on_c.y = 175

    print(f'(150, 175) in c: {point_in_circle(c, point_on_c)}')

    point_on_c.y = 225
    print(f'(150, 225) in c: {point_in_circle(c, point_on_c)}')
    
