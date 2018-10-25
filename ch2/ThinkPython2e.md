2.10 Exercises

Exercise 1

- 42 = n throws a syntax error: cannot assign to a literal
- x = y = 1 is legal (woohoo!)
- I believe the semi-colon is legal but unnecessary and I imagine frowned upon. In the example I used, the above expression x = y = 1. changed the type of x & y from an int (1) to a float (1.0).
- xy would be a variable name (in this case undefined). x y throws a syntax error (invalid syntax).

Exercise 2

1. 
r = 5
(4/3)*3.14*(r**3) # ~= 523.33

2. 
p = 24.95
v = 60
s = 3 + (0.75 * ( v - 1))
wc = (v * p) + s # 1544.25

3. 
s = 652 # start time
# Both examples of mile times, 8:15 & 7:12 are rational so I'm not going to worry about separating the seconds with the remainder operator, etc. I'm just going to use floats.
m = ( 1 * 8.25) + ( 3 * 7.2) + ( 1 * 8.25) # mile minutes
f = (int(s / 100)*100) + int(((s % 100) + m) / 60) * 100 + ((s % 100) + m) % 60 
# final mintutes: hours from start time (int(s/100)*100) plus all minutes, converted to hours (int(((s % 100) + m) / 60), plus all minutes left over ((s % 100) + m) % 60. This answer is a bit sloppy looking and far from ideal. In practice I would most likely use a date type, or helper functions, to simplify all of this (even if it means implementing it myself, which would be redundant).  



