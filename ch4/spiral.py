import exercises as e
import turtle

def spiral(t, a, b, length):
    theta = 1
    n = b
    # for n in range(b,b + length, step=b):
    while n < length:
        r = a + ( n * theta)
        e.arc(t,r,10)
        n += b  

bob = turtle.Turtle()
turtle.delay(1)
spiral(bob, 1, 1, 100)

turtle.exitonclick()
