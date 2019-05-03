# http://greenteapress.com/thinkpython2/html/thinkpython2006.html
# Chapter 5, Exercise 6

import turtle

def koch(t, length):
    if length < 3:
        t.fd(length)
        return

    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)
    t.rt(120)
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)

t = turtle.Turtle()
# koch(t, 125)

# Write a function called snowflake that draws three Koch curves to make the outline of a snowflake.

def snowflake(t, length):
    for i in range(0, 3):
        koch(t, length)
        t.rt( 360 / 3)

def minkowski_sausage(t, length):
    if length < 4:
        t.fd(length)
        return

    minkowski_sausage(t, length / 4)
    t.lt(90)
    minkowski_sausage(t, length / 4)
    t.rt(90)
    minkowski_sausage(t, length / 4)
    t.rt(90)
    minkowski_sausage(t, length / 4)
    minkowski_sausage(t, length / 4)
    t.lt(90)
    minkowski_sausage(t, length / 4)
    t.lt(90)
    minkowski_sausage(t, length / 4)
    t.rt(90)
    minkowski_sausage(t, length / 4)

# snowflake(t, 125)
minkowski_sausage(t, 525)
turtle.exitonclick()
