import turtle
import random

for i in range(50):
    turtle.right(random.randint(1, 180))
    turtle.forward(random.randint(1, 50))

turtle.exitonclick()
