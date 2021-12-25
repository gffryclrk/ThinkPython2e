"""Think Python, 2nd Ed."""
import calendar
from datetime import *

class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
    """
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True
    
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def print_time(time):
    """ prints the time in hour:minute:second format """

    print(f'{time.hour}:{time.minute}:{time.second}')

def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def mul_time(t1, multiplier):
    """ Chapter 16.7 Exercise 6
    Write a function called mul_time that takes a Time object and a
    number and returns a new Time object that contains the product of the
    original Time and the number."""
    
    assert valid_time(t1)
    seconds = time_to_int(t1) * multiplier
    return int_to_time(seconds)

def increment(time, seconds):
    """As an exercise, write a “pure” version of increment that creates
and returns a new Time object rather than modifying the parameter. """
    
    return int_to_time(time_to_int(time) + seconds)


def time_per_distance(t, distance):
    """ Chapter 16.7 Exercise 6: 
    Uses mul_time to return average time per distance

    Args:
        t: time
        distance: distance travelled

    Returns:
        Time object of average distance travelled (time per mile)
    """

    seconds = time_to_int(t)
    seconds_per_distance = seconds / distance
    return int_to_time(seconds_per_distance)

def print_day_of_week():
    """Chapter 16.7 Exercise 1 Use the datetime module to write a program
    that gets the current date and prints the day of the week."""
    
    today = datetime.now()
    day_of_week = calendar.weekday(today.year, today.month, today.day)
    name_of_today = calendar.day_name[day_of_week]
    print(name_of_today)

def time_until_next_bday(bday):
    """Chapter 16.7
    Exercise 7.2
    Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday.

    Notes:
    - I'm not going to print it but return it instead
    - This exercise is pretty much solved in the datetime.date documentation: https://docs.python.org/3/library/datetime.html

    Parameters
    ----------
    bday: datetime.date
        Date of birth

    Returns
    ----------
    time_until_bday: number of days until next bday
        datetime.timedelta
    """

    return timedelta(days=0)
