"""Testing Time exercise solutions to Think Python, 2nd Ed
Chapter 17 """
import unittest
from ch17.time_exercise import Time


class TestObjectOrientedTime(unittest.TestCase):

    def setUp(self):
        self.t = Time()
        self.t.hour = 1
        self.t.minute = 0 
        self.t.second = 0

    def test_oo_time_to_int(self):
        """ Test object oriented implementation of time_to_int """

        self.assertEqual(
            self.t.time_to_int(), 3600)
        
if __name__ == '__main__':
    unittest.main()
