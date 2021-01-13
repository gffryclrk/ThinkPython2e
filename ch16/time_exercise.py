"""Think Python, 2nd Ed."""

class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
    """

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
    """Write a function called mul_time that takes a Time object and a
number and returns a new Time object that contains the product of the
original Time and the number."""
    assert valid_time(t1)
    seconds = time_to_int(t1) * multiplier
    return int_to_time(seconds)

def increment(time, seconds):
    """As an exercise, write a “pure” version of increment that creates
and returns a new Time object rather than modifying the parameter. """

    
    return int_to_time(time_to_int(time) + seconds)
