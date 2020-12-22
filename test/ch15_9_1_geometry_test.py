"""Unit tests for shape objects created for Chapter 15 Exercise 1"""
import math
import unittest
import sys
sys.path.append('ch15/')
from ex_15_9_1 import Point, Rectangle, Circle, rect_in_circle, distance

class TestGeometry(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(Point(0, 0), 100, 100)

    def test_point_distance(self):
        """Helper method behaves as expected"""
        pointa = Point(0,0)
        pointb = Point(3,4)
        self.assertTrue(pointa.distance(pointb) == 5)
    
    def test_rectangle_has_4_corners(self):
        """created rectangle has 4 points"""
        self.assertTrue(len(self.rectangle.vertices()) == 4)

    def test_rectangle_diagonals(self):
        """ Assert lengths of two diagonals in rectangle are equal """
        vl = self.rectangle.vertices()
        d1 = math.sqrt((vl[0].x - vl[2].x)**2 + (vl[0].y - vl[2].y)**2)
        d2 = math.sqrt((vl[1].x - vl[3].x)**2 + (vl[1].y - vl[3].y)**2)
        self.assertTrue(d1 == d2)

    def test_rect_in_circle(self):
        """ Test rect_in_circle returns correct result """
        r1 = Rectangle(Point(0,0), width = 5, height = 3)
        c1 = Circle(Point(0, 0), radius = 6)

        self.assertTrue(rect_in_circle(c1, r1))
        r1.bl = Point(3, 0) # TODO: Create a shift method that moves shapes
        self.assertFalse(rect_in_circle(c1, r1))
        
        

    def test_distance(self):
        """ Test distance from point to line using known values"""
        p1 = Point(0,0)
        p2 = Point(1,1)
        xy = Point(0,2.5)

        half_hypoteneuse = math.sqrt((2.5 ** 2) + (2.5) ** 2) / 2

        # Using math.isclose because of precision with floats
        self.assertTrue(
            math.isclose(
                distance(p1, p2, xy), half_hypoteneuse
            )
        )
        
if __name__ == '__main__':
    unittest.main()
