from turtle import Turtle, Screen
from random import choice

drawer = Turtle(shape ='circle')
drawer.color('red')
drawer.width(3)
screen = Screen()
drawer.up()
drawer.goto(0, -200)
drawer.down()

color = ['black', 'red', 'blue', 'green', 'purple', 'orange', 'darkblue']
for x in range(3, 40):
    drawer.color(choice(color))
    angle = 360/x
    y = 0
    while y < x:
        drawer.left(angle)
        drawer.forward(50)
        y += 1