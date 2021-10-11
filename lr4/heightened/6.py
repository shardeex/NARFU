import turtle

turtle.right(90)

for i in range(10):
    for j in range(2):
        turtle.circle(20+10*i)
        turtle.left(180)

turtle.exitonclick()
