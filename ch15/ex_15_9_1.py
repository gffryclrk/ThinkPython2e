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
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self, other):
        """ Returns distance to other point"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Vector:
    """ Distance & magnitude """
    def __init__(self, pointA=Point(), pointB = Point(1,1)):
        self.pointA = pointA
        self.pointB = pointB
        self.x = pointB.x - pointA.x
        self.y = pointB.y - pointA.y

    def dot_product(self, other):
        """ Return scalar dot product of this vector with another vector"""
        return self.x * other.x + self.y * other.y

    def shortest_distance(self, pointE):
        """ Returns shortest distance from this vector (self) to point. 
        Based on https://www.geeksforgeeks.org/minimum-distance-from-a-point-to-the-line-segment-using-vectors/ """
        be = Vector(self.pointB, pointE)
        ae = Vector(self.pointA, pointE)

        if self.dot_product(be) > 0: return self.pointB.distance(pointE)
        if self.dot_product(ae) < 0: return self.pointA.distance(pointE)
        else: return distance(self.pointA, self.pointB, pointE)
        
        
class Circle:
    """ Has a radius and centre"""
    def __init__(self, centre = Point(0,0), radius=1):
        self.centre = centre
        self.radius = radius
    

class Rectangle:
    """ 4 sided figure with 4 90 degree angles """
    def __init__(self, point = Point(), width = 1, height = 1):
        self.bl = point #bottom left
        self.width = width
        self.height = height

    def vertices(self):
        """ Returns list of points in clockwise order starting with bottom left"""
        return [
            self.bl,
            Point(self.bl.x, self.bl.y + self.height),
            Point(self.bl.x + self.width, self.bl.y + self.height),
            Point(self.bl.x + self.width, self.bl.y)
            ]
            

def point_in_circle(circle, point):
    """takes a Circle and a Point
    and returns True if the Point lies in or on the boundary of the
    circle."""
    return math.sqrt((point.x - circle.centre.x)**2 + (point.y - circle.centre.y)**2) <= circle.radius

            
def rect_in_circle(circ, rect):
    """True if all of the corners of the rectangle fall inside the circle"""
    for point in rect.vertices():
        if not point_in_circle(circ, point):       
            return False

    return True

def distance(p1, p2, xy):
    """p1 & p2 are points on the same line. xy is a third point which the distance to the line containing points p1 & p2 is is being calculated and returned
    https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line"""
    numer = abs(
        (p2.x - p1.x)*(p1.y-xy.y)-(p1.x-xy.x)*(p2.y-p1.y)
        )
    denom = math.sqrt(
        (((p2.x-p1.x)**2) + ((p2.y-p1.y)**2))
         )
    return (numer / denom)


def rect_circle_overlap(circ, rect):
    """ Returns true if any part of rectangle overlaps circle
    https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line"""
    vl = rect.vertices()
    
    for a in range(len(vl)):
        p1 = vl[a]
        p2 = vl[(a + 1) % len(vl)]
        d = distance(p1, p2, circ.centre)
        if math.isclose(d, circ.radius) | circ.radius >= d:
            return True

    return False
        


    
    
if __name__ == '__main__':
    c = Circle()
    c.centre = Point() 
    c.centre.x = 150
    c.centre.y = 100
    c.radius = 75

    point_on_c = Point()
    point_on_c.x = 150
    point_on_c.y = 175

    print(f'(150, 175) in c: {point_in_circle(c, point_on_c)}')

    point_on_c.y = 225
    print(f'(150, 225) in c: {point_in_circle(c, point_on_c)}')
    
    r = Rectangle(Point(0, 0), 100, 100)

    v1 = Vector(Point(), Point(1,1))
