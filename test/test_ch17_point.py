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

if __name__ == '__main__':
    unittest.main()
