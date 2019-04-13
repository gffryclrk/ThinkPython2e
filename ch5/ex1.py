# The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
# 
# >>> import time
# >>> time.time()
# 1437746094.5735958
# 
# Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

import time

seconds = time.time()
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
years = days / 365.25

print("Years: ", years, " days: ", days, "\n")

# Time now (with some error due to float precision)

now_days = (years % 1) * 365.25
now_hours = (now_days % 1) * 24
now_minutes = (now_hours % 1) * 60
now_seconds = (now_minutes % 1) * 60

print((years // 1), " years, ", now_days, " days, ", now_hours, " hours, ", now_minutes, " minutes, ", now_seconds, " seconds.\n")

# Above output is wrong. Perhaps due to leap years, leap seconds, days in a month, that kind of thing? Hm.
print( time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()) )
