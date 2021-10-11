import turtle

for i in range(10):
    turtle.penup()
    turtle.goto(-1*10*(i+1), -1*10*(i+1))
    turtle.pendown()

    for j in range(4):
        turtle.forward(2*10*(i+1))
        turtle.left(90)

turtle.mainloop()