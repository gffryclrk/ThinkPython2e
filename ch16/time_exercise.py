"""Think Python, 2nd Ed."""

class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
    """

def print_time(time):
    """ prints the time in hour:minute:second format """

    print(f'{time.hour}:{time.minute}:{time.second}')

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
        
    return sum

def increment(time, seconds):
    """As an exercise, write a “pure” version of increment that creates
and returns a new Time object rather than modifying the parameter. """

    t = Time()
    t.second = ( time.second + seconds ) % 60
    s_carry = ( time.second + seconds ) // 60
    t.minute = ( time.minute + s_carry ) % 60
    m_carry = ( time.minute + s_carry ) // 60
    t.hour = ( time.hour + m_carry ) % 60
    # For simplicity we're not carrying hours anywhere :) 
    return t
