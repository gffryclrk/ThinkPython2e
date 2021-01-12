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
        

        

if __name__ == '__main__':
    unittest.main()
