# Coded by Ephraim Pillar G20P0425

import turtle

def drawShape(aTurtle, size, number):    
    window = turtle.Screen()
    
    angle = 360 / (number)
    
    for x in range(number):
        aTurtle.forward(size)
        aTurtle.left(angle)
        
    window.exitonclick()

sizeOfSides = int(input("Size of the sides of the shape?"))
numberOfSides = int(input("Number of the sides of the shape?"))
userTurtle = turtle.Turtle()

drawShape(userTurtle, sizeOfSides, numberOfSides)

