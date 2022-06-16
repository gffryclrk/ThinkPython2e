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

    def test_eq_methods(self):

        self.assertEqual(Point(0,0), Point(0,0))

    def test_point_add_method(self):
        """ Exercise 17.4. Write an add method for the Point class. """

        p2 = Point(1,1)

        # TODO: Look up a way to overload equals and use equality to check expected return instead
        self.assertEqual(self.p + p2, Point(1,1))
        

    def test_point_radd_tuple(self):

        """ Exercise 17.5 Test: adding a Point and Tuple """

        self.assertEqual(
            Point(0,0) + (1,1),
            (1,1) + Point(0,0),
            msg="Positive radd case"
        )

        self.assertNotEqual(
            Point(0,0) + (1,1),
            Point(1,2),
            msg="Negative radd case"
        )

if __name__ == '__main__':
    unittest.main()
