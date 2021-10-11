import turtle
import math

for i in range(100):
    t = i/math.pi
    x = t*math.cos(t)
    y = t*math.sin(t)
    turtle.goto(x, y)

turtle.exitonclick()