# Coded by Ephraim Pillar G20P0425

import math
import turtle as t

windowScreen = t.Screen()
graphTurtle = t.Turtle()
xAxisTurtle = t.Turtle()
yAxisTurtle = t.Turtle()

xCoordinate = -180

for angle in range(-180, 181):
    yCoordinate = ((math.sin(math.radians(angle))) * 100)
    graphTurtle.goto(xCoordinate, yCoordinate)
    xCoordinate+=1

xAxisTurtle.up()
xAxisTurtle.forward(-90)
xAxisTurtle.write("-90")
xAxisTurtle.forward(-90)
xAxisTurtle.write("-180")


xAxisTurtle.forward(180)
xAxisTurtle.down()
xAxisTurtle.forward(90)
xAxisTurtle.write("90")
xAxisTurtle.forward(90)
xAxisTurtle.write("180")

yAxisTurtle.left(90)
yAxisTurtle.backward(50)
yAxisTurtle.write("-0.5")
yAxisTurtle.backward(50)
yAxisTurtle.write("-1.0")

yAxisTurtle.forward(150)
yAxisTurtle.write("0.5")
yAxisTurtle.forward(50)
yAxisTurtle.write("1.0")
yAxisTurtle.down()

t.exitonclick()