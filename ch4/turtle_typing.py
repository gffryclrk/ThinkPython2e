import turtle
# from letters import draw_a
import letters

bob = turtle.Turtle()
bob.speed(1)

# draw_a(bob, 100)
# draw_a(bob, 200)

letters.draw_a(bob, 100)
letters.draw_b(bob, 100)
letters.draw_b(bob, 100)
letters.draw_a(bob, 100)

turtle.exitonclick()

