#Made by Samuel Lin, October 25th, 2016, All Rights Reserved
#
#Turtle drawing game
import turtle
import math
import random


#Set up screen
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.tracer(1)

#Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.speed(100)
mypen.setposition(-600, -600)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(1200)
    mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("darkblue")
player.shape("turtle")
player.speed(0)
player.penup()

#Set speed variable
speed = 1

#Set PenSize variable
pensize = 1

#Define functions

#Changing colors
def red():
    player.color("red")
def darkred():
    player.color("darkred")
def blue():
    player.color("blue")
def darkblue():
    player.color("darkblue")
def lightblue():
    player.color("lightblue")
def orange():
    player.color("orange")
def green():
    player.color("green")
def lightgreen():
    player.color("lightgreen")
def darkgreen():
    player.color("darkgreen")
def yellow():
    player.color("yellow")
    
#Movement
def turnleft():
    player.left(90)

def turnright():
    player.right(90)

def increasespeed():
    global speed
    speed += 1
    if speed > 20:
        speed = 20
def decreasespeed():
    global speed
    speed += -1
    if speed < -20:
        speed = -20

#Drawing
def PenUp():
    player.penup()
def PenDown():
    player.pendown()
def Thick():
    global pensize
    pensize += 1
def Thin():
    global pensize
    pensize += -1
    if pensize < 1:
        pensize = 1

#Collision test 
def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False
    
#Set controls
turtle.listen()
#WASD to Move
turtle.onkey(turnleft, "a")

turtle.onkey(turnright, "d")

turtle.onkey(increasespeed, "w")

turtle.onkey(decreasespeed, "s")

# OP[] to Draw
turtle.onkey(PenUp, "o")

turtle.onkey(PenDown, "p")

turtle.onkey(Thick, "[")

turtle.onkey(Thin, "]")

# Numbers to Change color
turtle.onkey(red, "1")

turtle.onkey(darkred, "2")

turtle.onkey(darkgreen, "3")

turtle.onkey(blue, "4")

turtle.onkey(lightblue, "5")

turtle.onkey(darkblue, "6")

turtle.onkey(orange, "7")

turtle.onkey(yellow, "8")

turtle.onkey(green, "9")

turtle.onkey(lightgreen, "0")
             
while True:
    player.forward(speed)
    player.pensize(pensize)
    #Boundary check
    if player.xcor() > 600 or player.xcor() < -600:
        player.right(180)

    elif player.ycor() > 600 or player.ycor() < -600:
        player.right(180)

            

delay = raw_input("Press Enter to finish.")

