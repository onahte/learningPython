from turtle import Turtle, Screen, colormode
from random import choice, randint

colormode(255)

drawer = Turtle(shape ='circle')
drawer.color('red')
drawer.width(1)
drawer.speed(15)
screen = Screen()

def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b,)
    drawer.color(rgb)

for x in range(90):
    random_color()
    drawer.circle(100)
    drawer.left(4)

screen.exitonclick()