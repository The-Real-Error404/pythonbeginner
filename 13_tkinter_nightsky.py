from tkinter import *
import random
import time

myTk = Tk()
canvas = Canvas(myTk, width=400, height=400, bg="black")
canvas.pack()

starcolor = ["yellow", "gray30", "gray50", "gray70", "gray90", "gray95", "white", "red", "blue", "green", "chocolate1", "chocolate2", "chocolate3", "orange", "pink1"]

def drawcircle(cx, cy, radius, color):
    x1 = cx - radius
    x2 = cx + radius
    y1 = cy - radius
    y2 = cy + radius
    canvas.create_oval(x1, y1, x2, y2, fill=color)

while True:
    canvas.delete("all")
    canvas.create_polygon(0, 400, 100, 350, 200, 400, fill="gray30")
    
    c = random.choice(starcolor)
    drawcircle(200, 200, 4, c)

    c = random.choice(starcolor)
    drawcircle(50, 50, 4, c)

    c = random.choice(starcolor)
    drawcircle(150, 100, 4, c)

    c = random.choice(starcolor)
    drawcircle(300, 150, 4, c)

    c = random.choice(starcolor)
    drawcircle(350, 100, 4, c)

    c = random.choice(starcolor)
    drawcircle(100, 2040, 4, c)

    c = random.choice(starcolor)
    drawcircle(100, 250, 4, c)

    c = random.choice(starcolor)
    drawcircle(230, 240, 4, c)

    c = random.choice(starcolor)
    drawcircle(100, 100, 4, c)

    c = random.choice(starcolor)
    drawcircle(300, 300, 4, c)

    c = random.choice(starcolor)
    drawcircle(200, 100, 4, c)

    c = random.choice(starcolor)
    drawcircle(250, 300, 4, c)
    
    myTk.update()
    time.sleep(0.05)

myTk.destroy()
