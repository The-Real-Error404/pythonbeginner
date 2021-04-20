from tkinter import *
import random

myTk = Tk()
canvas = Canvas(myTk, height=400, width=400)
canvas.pack()
colorlist = ["red", "green", "blue", "yellow"]

def drawline():
    x = random.randint(0, 400) 
    y = random.randint(0, 400)
    color = random.choice(colorlist)
    canvas.create_line(200, 200, x, y, fill = color)
    
while True:
    drawline()
    myTk.update()

myTk.destroy()

