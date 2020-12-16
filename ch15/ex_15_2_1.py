"""Think Python, 2nd Ed
Chapter 15.2

As an exercise, write a function called distance_between_points that takes two Points as arguments and returns the distance between them."""

import math

class Point:
    """Represents a point in 2-D space."""

blank = Point()
blank.x = 3.0
blank.y = 4.0

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def distance_between_points(pointA, pointB):
    return math.sqrt( (pointA.x - pointB.x) ** 2 + (pointA.y - pointB.y) ** 2 )

    
if __name__ == '__main__':
    
    p1 = Point()
    p1.x = 3
    p1.y = 3
    p2 = Point()
    p2.x = 5
    p2.y = 5

    print(f'distance between p1 & p2: {distance_between_points(p1, p2)}')

    # 15.2
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print_point(center)

    #15.5
    print(f'box corner x, y before move_rectangle: {box.corner.x}, {box.corner.y}')
    move_rectangle(box, 5, 5)
    print(f'box corner x, y after move_rectangle: {box.corner.x}, {box.corner.y}')
    
