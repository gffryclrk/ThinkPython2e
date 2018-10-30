import math
import turtle

def to_rad(deg):
    return ( deg * math.pi / 180)

def to_deg(rad):
    return (rad * 180 / math.pi)

def draw_pie(t, radius, slices):
    """ This is my first working attempt
    It draws the pie as in the exercise but is a bit inefficient:
    every radius is drawn twice (overlap). I think
    this could be improved with a clever use of the remainder operator
    and alternating between left and right turns.
    """ 
    theta = 360 / slices
    x = radius * math.sin( to_rad(theta) / 2 )

    for i in range(0, slices):
        t.lt(theta / 2)
        t.forward(radius)
        t.rt(180 - (90 - theta / 2))
        t.forward( 2 * x)
        t.rt(180 - (90 - theta / 2))
        t.forward(radius)
        t.lt(180 - theta / 2)




bob = turtle.Turtle()
bob.speed(1)
draw_pie(bob, 100, 11)

turtle.exitonclick()
