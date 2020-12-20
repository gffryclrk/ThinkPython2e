"""Unit tests for shape objects created for Chapter 15 Exercise 1"""

import unittest
import sys
sys.path.append('ch15/')
#import ex_15_9_1 as gm
from ex_15_9_1 import Rectangle, Point

class TestGeometry(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(Point(0, 0), 100, 100)

    
    def test_rectangle_has_4_corners(self):
        """created rectangle has 4 points"""
        self.assertTrue(len(self.rectangle.points()) == 4)


if __name__ == '__main__':
    unittest.main()
