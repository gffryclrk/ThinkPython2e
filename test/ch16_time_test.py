"""Testing exercise solutions to Think Python, 2nd Ed
Chapter 16 """

import unittest
from unittest.mock import patch, call
import sys
sys.path.append('ch16/')
from time_exercise import Time, print_time
import pdb

class TestTime(unittest.TestCase):

    @patch('builtins.print')
    def test_print_again(self, mock_print):
        t = Time()
        t.hour = 11
        t.minute = 59
        t.second = 30

        print_time(t)

        mock_print.assert_called_with('11:59:30')


if __name__ == '__main__':
    unittest.main()
