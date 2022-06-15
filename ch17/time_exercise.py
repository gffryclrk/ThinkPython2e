class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
    
    Copied from Chapter 16: ../ch16/time_exercise.py
    """
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def time_to_int(self):
        """Exercise 17.1. Rewrite time_to_int (from Section 16.4) as a method. 
        Implementation here:
        Returns integer of Time converted to seconds

        It is probably not appropriate to rewrite int_to_time as a method; what object you would invoke it on?
        Answer: The int class. See `help(int)`



"""

        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
