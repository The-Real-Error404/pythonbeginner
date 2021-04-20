import turtle

T = turtle.Turtle()

screen = T.getscreen()
screen.bgpic("goal.gif")

T.shape("turtle")
T.speed(1)

T.rt(30)
T.fd(100)
T.lt(30)
T.fd(100)
T.lt(30)
T.fd(100)


turtle.done()
