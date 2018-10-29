import exercises
import math

def to_rad(deg):
    return ( deg * math.pi / 180)

def to_deg(rad):
    return (rad * 180 / math.pi)

def draw_a(t, height):
    theta = 75
    crossbar = 0.5
    theta_rad = theta * math.pi / 180
    h = height / math.sin(theta_rad) 
    
    t.lt(theta)
    t.forward(h)
    t.rt(180 - 2*(90 - theta))
    t.forward(h * crossbar)

    # o = crossbar * (h * math.sin(to_rad(0.5*(90-theta)))) 
    o = h * crossbar * math.sin(to_rad(90 - theta))

    # t.rt(180 - (90 - (90-theta)))
    t.rt(180 - theta)
    t.forward(2 * o)
    t.pu()
    t.rt(180)
    t.forward(2 * o)
    t.pd()

    t.rt(theta)
    t.forward(h * (1 - crossbar))
    t.lt(theta)

def draw_b(t, height):
    cb_ratio = 0.25
    curve_radius = 0.25 * height

    # t.lt(90)
    # t.forward(height)
    # t.rt(90)
    # t.forward(h * cb_ratio)
    
    # theta = 2 * math.asin(c / (2 * R))
    
    # arc_theta = 2 * math.asin(0.5 * height / ( 2 * curve_radius)) 
    # arc_length =  curve_radius * arc_theta

    t.forward(cb_ratio * height)
    # exercises.arc(t, arc_length, to_deg(arc_theta)) 
    # exercises.arc(t, (math.pi * curve_radius), 180) 
    exercises.arc(t, curve_radius, 180)
    
    # t.forward(cb_ratio * height*0.90)
    # t.pu()
    # t.rt(180)
    # t.forward(cb_ratio*height*0.90)
    # t.pd()
    # t.forward(cb_ratio * height * 0.2)

    t.rt(180)
    exercises.arc(t, curve_radius, 180)
    t.forward(cb_ratio * height)
    t.lt(90)
    t.forward(height)

    t.pu()
    t.lt(90)
    t.forward(cb_ratio * height + curve_radius)
    t.pd()

def draw_c(t, height):
    # exercises.arc(t, height/2, 360*0.7)
    c_ratio = 0.8
    R = height / 2
    circumference = math.pi * 2 * R
    s = (1 - c_ratio) * 2 * math.pi * R
    theta = s / R
    r = R * math.cos(theta / 2)
    a = 2 * R * math.sin( theta / 2)
    yd = (height - a) / 2

    t.pu()
    t.forward(R)
    t.pd()
    exercises.arc(t, R, (1 - c_ratio) * 0.5 *360) 
    t.pu()
    exercises.arc(t, R, 180 -  (1 - c_ratio) *360)
    t.pd()
    exercises.arc(t, R, (1 - c_ratio) * 0.5 *360) 
    exercises.arc(t, R, 0.5 * 360)
    t.pu()
    t.forward(R)
    t.pd()

    # t.pu()
    # t.forward(R + r)
    # t.lt(90)
    # t.forward(yd + a)
    # t.lt(60)
    # t.pd()

    # exercises.arc(t, height/2, 2 * math.pi * R * c_ratio)
    # t.setheading(270)
    # t.pu()
    # t.forward(yd)
    # t.lt(90)
    # t.forward(R - r)
    
