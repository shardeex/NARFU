import turtle

turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

for i in range(4):
    turtle.forward(200)
    turtle.left(90)

turtle.exitonclick()