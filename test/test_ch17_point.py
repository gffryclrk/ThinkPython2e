"""Testing Point exercise solutions to Think Python, 2nd Ed
Chapter 17 """
import unittest
from ch17.point_exercise import Point


class TestObjectOrientedPoint(unittest.TestCase):

    def setUp(self):
        self.p = Point()

    def test_point_default_constructor(self):
        """ Test object oriented implementation of time_to_int """

        self.assertEqual(
            self.p.x, 0)
        
        self.assertEqual(
            self.p.y, 0)

    def test_point_str_method(self):
        """Exercise 17.3. Write a str method for the Point class. Create a Point object and print it"""
        self.assertEqual(self.p.__str__(), '(0, 0)')
        # TODO: Look up how to patch this test to test print without actually printing

if __name__ == '__main__':
    unittest.main()
