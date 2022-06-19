import pdb

class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
    
    Exercise 17.6 Change the attributes of Time to be a single integer representing seconds since mid-
    night. Then modify the methods (and the function int_to_time) to work with the new implemen-
    tation.
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.seconds = hour * 3600 + minute * 60 + second


    def __eq__(self, other):
        return self.seconds == other.seconds

    def time_to_int(self):
        """Exercise 17.1. Rewrite time_to_int (from Section 16.4) as a method. 
        Implementation here:
        Returns integer of Time converted to seconds

        It is probably not appropriate to rewrite int_to_time as a method; what object you would invoke it on?
        Answer: The int class. See `help(int)` """

        return self.seconds

    def int_to_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return Time(hours, minutes, seconds)
