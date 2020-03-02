# Coded by Ephraim Pillar G20P0425

import turtle
import random

def turtleWalkRandomly(aTurtle, walkingForward):
    for x in range(walkingForward):
        aTurtle.forward(50)
        aTurtle.right(random.randrange(1, 361)) 
        
walking = int(input("How many times to walk forward"))
userTurtle = turtle.Turtle()
turtleWalkRandomly(userTurtle, walking)