# Coded by Ephraim Pillar G20P0425

import turtle as t

windowScreen = t.Screen()
myTurtle = t.Turtle()

for sides in range(3):
    angle = 360/ 3
    t.forward(50)
    t.left(angle)

t.up()
t.forward(100)
t.down()

for sides in range(4):
    angle = 360/ 4
    t.forward(50)
    t.left(angle)
    
t.up()
t.forward(100)
t.down()

for sides in range(5):
    angle = 360/ 5
    t.forward(50)
    t.left(angle)
    
t.up()
t.forward(100)
t.down()

for sides in range(6):
    angle = 360/ 6
    t.forward(50)
    t.left(angle)

t.exitonclick()
