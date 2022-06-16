"""Testing Time exercise solutions to Think Python, 2nd Ed
Chapter 17 """
import unittest
from ch17.time_exercise import Time


class TestObjectOrientedTime(unittest.TestCase):

    def setUp(self):
        self.t = Time(1, 0, 0)

    def test_oo_time_to_int(self):
        """ Test object oriented implementation of time_to_int """

        self.assertEqual(
            self.t.time_to_int(), 3600)

    def test_int_to_time_method(self):
        """ Confirm Time.int_to_time works as expected """

        self.assertEqual(self.t, Time.int_to_time(3600))

        
if __name__ == '__main__':
    unittest.main()
