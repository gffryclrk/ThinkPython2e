"""Think Python, 2nd Ed
Examples from Chapter 15
"""
import copy

class Rectangle:
    """Represents a rectangle
    Attributes: width, height, corner """

class Point:
    """Represents a point in 2-D space."""

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect, dx, dy):
    rect_copy = copy.deepcopy(rect)
    rect_copy.corner.x += dx
    rect_copy.corner.y += dy
    return rect_copy

if __name__ == '__main__':
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

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
    box_copy = move_rectangle(box, 5, 5)
    print(f'box_copy corner x, y after move_rectangle: {box_copy.corner.x}, {box_copy.corner.y}')
    
