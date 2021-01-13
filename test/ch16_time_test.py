"""Testing exercise solutions to Think Python, 2nd Ed
Chapter 16 """

import unittest
from unittest.mock import patch, call
import sys
sys.path.append('ch16/')
from time_exercise import *
import pdb

class TestTime(unittest.TestCase):

    def setUp(self):
        self.t = Time()
        self.t.hour = 11
        self.t.minute = 59
        self.t.second = 30
        
    @patch('builtins.print')
    def test_print_again(self, mock_print):
        t = Time()
        t.hour = 11
        t.minute = 59
        t.second = 30

        print_time(t)

        mock_print.assert_called_with('11:59:30')

    def test_add_time(self):
        # I'm surprised constructors haven't yet been covered in this book
        start = Time()
        start.hour = 9
        start.minute = 45
        start.second = 0

        duration = Time()
        duration.hour = 1
        duration.minute = 35
        duration.second = 0

        done = add_time(start, duration)

        assert(done.hour == 11)
        assert(done.minute == 20)
        assert(done.second == 0)

    def test_increment(self):
        t = self.t

        more_seconds = 30

        i = increment(t, more_seconds)
        assert(i.second == (t.second + more_seconds) % 60)
        

    def test_int_to_time_time_to_int(self):
        """(from text) You might have to think a bit, and run some tests, to
convince yourself that these functions are correct. One way to test
them is to check that time_to_int(int_to_time(x)) == x for many values
of x. This is an example of a consistency check."""

        x = 100
        assert(time_to_int(int_to_time(x)) == x)

        x = 1000
        assert(time_to_int(int_to_time(x)) == x)

        x = 99
        assert(time_to_int(int_to_time(x)) == x)

        x = 0
        assert(time_to_int(int_to_time(x)) == x)

    def test_mul_time(self):
        t = self.t

        assert(
            time_to_int(
                add_time(t, t)
                ) ==
            time_to_int(
                mul_time(t, 2)
                )
            )
        

if __name__ == '__main__':
    unittest.main()
