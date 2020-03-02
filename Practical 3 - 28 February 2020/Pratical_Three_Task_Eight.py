# Coded by Ephraim Pillar G20P0425

import turtle
import random

def hitTheBestBars(numberOfBars):
    userTurtle = turtle.Turtle()
    screen = turtle.Screen()

    userTurtle.penup()
    userTurtle.goto(-150, -50)
    userTurtle.pendown()
    
    for x in range(numberOfBars):
        height = random.randrange(1, 201)
        userTurtle.left(90)
        userTurtle.forward(height)
        userTurtle.right(90)
        userTurtle.forward(50)
        userTurtle.right(90)
        userTurtle.forward(height)
        userTurtle.left(90)
        
    userTurtle.left(180)
    userTurtle.forward(50*numberOfBars)
    userTurtle.right(180)
    screen.exitonclick()
        
userBarNumber = int(input("Number of bars?"))
hitTheBestBars(userBarNumber)


    