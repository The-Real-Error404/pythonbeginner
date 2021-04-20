import turtle
T = turtle.Turtle()

T.speed(1)
T.pencolor("red")
T.penup()
T.goto(-150, 100)
T.pendown()

T.forward(100)
T.right(90)
T.forward(100)
T.right(90)
T.forward(100)
T.right(90)
T.forward(100)
T.right(90)

T.penup()
T.fillcolor("green")
T.goto(150, 0)
T.pendown()

T.begin_fill()
T.lt(120)
T.fd(100)
T.lt(120)
T.fd(100)
T.lt(120)
T.fd(100)
T.end_fill()

T.penup()
T.color("blue")
T.goto(0, -50)
T.pendown()
T.color("blue")

T.begin_fill()
for i in range(36):
   
    T.fd(10)
    T.right(10)

T.end_fill()



turtle.done()
