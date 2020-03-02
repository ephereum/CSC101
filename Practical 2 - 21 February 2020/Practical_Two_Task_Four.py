# Coded by Ephraim Pillar G20P0425

import math
import turtle as t

windowScreen = t.Screen()
graphTurtle = t.Turtle()
xAxisTurtle = t.Turtle()
yAxisturtle = t.Turtle()

xCoordinate = -180

for angle in range(-180, 181):
    yCoordinate = ((math.sin(math.radians(angle))) * 100)
    graphTurtle.goto(xCoordinate, yCoordinate)
    xCoordinate+=1

xAxisTurtle.forward(180)
yAxisturtle.left(90)
yAxisturtle.backward(100)
yAxisturtle.forward(200)
yAxisturtle.down()

t.exitonclick()