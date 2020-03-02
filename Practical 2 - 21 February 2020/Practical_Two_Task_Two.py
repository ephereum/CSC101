# Coded by Ephraim Pillar G20P0425

import turtle as t

windowScreen = t.Screen()
windowScreen.bgcolor("Gray")
myTurtle = t.Turtle()

for sides in range(3):
    t.color("Red")
    angle = 360/ 3
    t.forward(50)
    t.left(angle)

t.up()
t.forward(100)
t.down()

for sides in range(4):
    t.color("Gold")
    angle = 360/ 4
    t.forward(50)
    t.left(angle)
    
t.up()
t.forward(100)
t.down()

for sides in range(5):
    t.color("Hot Pink")
    angle = 360/ 5
    t.forward(50)
    t.left(angle)
    
t.up()
t.forward(100)
t.down()

for sides in range(6):
    t.color("Maroon")
    angle = 360/ 6
    t.forward(50)
    t.left(angle)

t.exitonclick()
