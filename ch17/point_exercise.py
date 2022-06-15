class Point:
    """ Point class to hold x & y co-ordinates """

    def __init__(self, x=0, y=0):
        """Exercise 17.2. Write an init method for the Point class that takes x and y as optional parameters
and assigns them to the corresponding attributes"""

        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        """ Two points are equal if their x & y coordinates are equal """
        return (self.x == other.x) & (self.y == other.y)
        

    def __add__(self, other):
        """Exercise 17.5. Write an add method for Points that works with either a Point object or a tuple:
            - If the second operand is a Point, the method should return a new Point whose x coordinate is
              the sum of the x coordinates of the operands, and likewise for the y coordinates.
            - If the second operand is a tuple, the method should add the first element of the tuple to the x
              coordinate and the second element to the y coordinate, and return a new Point with the result.
        """
        
        if isinstance(other, tuple): 
            return Point(self.x + other[0], self.y + other[1])

        return Point(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        """See Exercise 17.5 note above"""
        return self + other
        

