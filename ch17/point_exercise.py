class Point:
    """ Point class to hold x & y co-ordinates """

    def __init__(self, x=0, y=0):
        """Exercise 17.2. Write an init method for the Point class that takes x and y as optional parameters
and assigns them to the corresponding attributes"""

        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


