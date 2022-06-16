"""Testing exercise solutions to Think Python, 2nd Ed
Chapter 16 """
import unittest
from unittest.mock import patch, call
# import sys
# sys.path.append('./ch16/')
from ch16.time_exercise import *
# from ch16.time_exercise import Time

import datetime
from freezegun import freeze_time
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
        

    def test_time_per_distance(self):
        """ Test time_per_distance function """
        t = Time()
        t.hour = 10

        d = 2

        tpd = time_per_distance(t, d)
        assert(tpd.hour == 5)
        assert(tpd.minute == 0)
        assert(tpd.second == 0)

    @patch('builtins.print')
    @freeze_time('2021-12-04')
    def test_print_day_of_week(self, mock_print):
        print_day_of_week()
        mock_print.assert_called_with('Saturday')
        
    @freeze_time('2021-12-25')
    def test_time_until_next_bday_next_year(self):
        """ Return expected datetime.timedelta when bday this year is past"""

        bday = datetime.date(2000,2,14)
        countdown = time_until_next_bday(bday)

        self.assertEqual(
                countdown,
                datetime.timedelta(days=51)
                )

    @freeze_time('2021-01-20')
    def test_time_until_next_bday_this_year(self):
        """ Return expected datetime.timedelta when bday this year is not past"""

        bday = datetime.date(2000,2,14)
        countdown = time_until_next_bday(bday)

        self.assertEqual(
                countdown,
                datetime.timedelta(days=25)
                )

    def test_double_day_legal_values(self):
        """ Test double day with expected input"""

        bday1 = date(year=2000, month=1, day=1)
        bday2 = date(year=2010, month=1, day=1)

        self.assertEqual(
            get_double_day(bday1, bday2),
            datetime.date(2020, 1, 2)
            )
    
    @unittest.expectedFailure
    def test_double_day_illegal_values(self):
        """ A test that should fail because you can't have a double day with two people born on the same day (I don't think...) """

        bday1 = date(year=2000, month=1, day=1)
        self.assertEqual(
            get_double_day(bday1, bday1),
            datetime.date(2020, 1, 2)
            )


if __name__ == '__main__':
    unittest.main()
