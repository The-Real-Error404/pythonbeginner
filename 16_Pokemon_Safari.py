from tkinter import Tk, Canvas, PhotoImage, NW
import time
import random

myTk = Tk()
canvas = Canvas(myTk, width=400, height=400)
canvas.pack()

background = PhotoImage(file="pokemon_map_v2.gif")
canvas.create_image(0, 0, anchor=NW, image=background)

moveleft = False
moveright = False
moveup = False
movedown = False
 
c = canvas.create_oval(180, 180, 220, 220, fill="blue")

totalsec = 0.0
maxsec = 60.0

found = []  #this array will hold the pokemon we find
caught = [] #this array will hold the pokemon we catch
fire = ["Charmander", "Magmar", "Vulpix"]
water = ["Squirtle", "Goldeen", "Magicarp"]
rock = ["Onix", "Sandshrew", "Geodude"]
grass = ["Weedle", "Caterpie", "Oddish"]

print("Welcome to Pokemon Safari")
print("Use arrow keys to explore the 4 different terrains")
print("There are 3 different Pokemon for every terrain")
print("Try to find and catch all 12 before time runs out!")

def spawn(terrain): #make new function accepting an array
    pokemon = random.choice(terrain) #pick random from array
    print("You found", pokemon) #print out we found the pokemon
    if(pokemon not in found): #if we haven’t found it before
        found.append(pokemon) #add pokemon to list
    coinflip = random.randint(0, 1) #heads or tails
    if(coinflip == 0): #heads means pokemon ran away
        print(pokemon, "ran away")
    else:                   #tails means we caught the pokemon
        print("You caught", pokemon)
    if(pokemon not in caught):#if we haven’t caught before
        caught.append(pokemon)                            #add pokemon to caught list

def encounter():
    encountered = False
    encounter_probability = random.randint(1, 100)
    
    if encounter_probability == 1:
        encountered = True
    pos = canvas.coords(c)
    if encountered:
        if int(pos[2]) <= 175 and int(pos[3]) <= 175:
            spawn(grass) #Do this three more times for all terrain
        if int(pos[2]) <= 175 and int(pos[1]) >= 225:
            spawn(water) 
        if int(pos[0]) >= 225 and int(pos[1]) >= 225:
            spawn(rock) 
        if int(pos[0]) >= 225 and int(pos[3]) <= 175:
            spawn(fire) 

    
def keypress(event):
    global moveleft, moveright, moveup, movedown

    if event.keysym == "Left" :
        moveleft = True
    if event.keysym == "Right" :
        moveright = True
    if event.keysym == "Up" :
        moveup = True
    if event.keysym == "Down" :
        movedown = True

def keyrelease(event):
    global moveleft, moveright, moveup, movedown

    if event.keysym == "Left" :
        moveleft = False
    if event.keysym == "Right" :
        moveright = False
    if event.keysym == "Up" :
        moveup = False
    if event.keysym == "Down" :
        movedown = False    

        
def movement():
    pos = canvas.coords(c)

    if moveleft and int(pos[0] >=3):
        canvas.move(c, -3, 0)
        encounter()
    if moveright and int(pos[2] <=397):
        canvas.move(c, 3, 0)
        encounter()
    if moveup and int(pos[1] >=3):
        canvas.move(c, 0, -3)
        encounter()
    if movedown and int(pos[3] <=397):
        canvas.move(c, 0, 3)
        encounter()

canvas.bind_all("<KeyPress>", keypress)

canvas.bind_all("<KeyRelease>", keyrelease)


while True:
    movement()
    myTk.update()
    time.sleep(0.01)

    totalsec = totalsec + 0.01
    if totalsec >= maxsec:
        print("Time’s Up! Game Over!") #Lose message
        break
    elif(len(caught) == 12): #If we caught 12 pokemon
        print("Congrats! You caught them all!") #Win Message
        break

#Print out the final count for the found/caught pokemon
print("You found " + str(len(found)) + " of the 12 pokemon")
if(len(found) > 0): #if we found at least 1 pokemon
    print ("Found pokemon are: " + str(found)) #print found list
print("You caught " + str(len(caught)) + " of the 12 pokemon")
if(len(caught) > 0): #if we caught at least 1 pokemon
    print ("Caught pokemon are: " + str(caught)) #print caught list


myTk.destroy()
