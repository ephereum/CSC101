#Coded by Ephraim Pillar G20P0425

import turtle as t
windowScreen = t.Screen()
windowScreen.bgcolor("LightGreen")
t = t.Turtle()
t.color("Blue")
t.shape("turtle")

t.penup()

for clock in range(12):
    t.forward(200)
    t.stamp()
    t.backward(200)
    t.right(30)

t.pensize(4)

for strokes in range(12):
    t.fd(160)
    t.down()
    t.fd(20)
    t.up()
    t.bk(180)
    t.left(30)

windowScreen.exitonclick()