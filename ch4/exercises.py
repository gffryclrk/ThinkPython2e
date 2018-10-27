import math
import turtle
# bob = turtle.Turtle()

def square(t, length):
  for i in range(4):
    t.forward(length)
    t.left(90)

# square(bob,500)

def polygon(t, n, length):
  angle = 360/n
  for i in range(n):
    t.forward(length)
    t.left(angle)

#polygon(bob, 100, 4)
#polygon(bob, 100, 5)
#polygon(bob, 100, 6)

#circle(bob, 100)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

def petal(t, petal_length, petal_radius):
    # http://mathworld.wolfram.com/CircularSegment.html
    c = petal_length
    R = petal_radius
    # h = r - math.sqrt(r**r - (0.25 * c**c))
    theta = 2 * math.asin(c / (2 * R))
    s = R * theta 
    theta_degrees = theta * 180 / math.pi
    # print("theta ", theta, " 4 ", c, " R ", R)
    arc(t, s, theta_degrees)
    t.lt(180 - theta_degrees)
    arc(t,s, theta_degrees)
    t.lt(180 - theta_degrees)

def flower(t, flower_radius, petal_radius, petal_quantity):
    for i in range(0, petal_quantity):
        petal(t, flower_radius, petal_radius)
        t.rt( 360 / petal_quantity)


# bob.speed(0)
# flower(bob, 140, 90, 6)
# flower(bob, 140, 90, 3)
# flower(bob, 100, 200, 6)
# flower(bob, 60, 90, 10)
# flower(bob, 200, 300, 10)

# turtle.exitonclick()
