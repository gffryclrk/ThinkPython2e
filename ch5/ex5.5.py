# http://greenteapress.com/thinkpython2/html/thinkpython2006.html

import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


t = turtle.Turtle()
draw(t, 10, 15)

