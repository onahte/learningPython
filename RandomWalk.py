from turtle import Turtle, Screen
from random import choice, randint

drawer = Turtle(shape ='circle')
drawer.color('red')
drawer.width(10)
drawer.speed(15)
screen = Screen()

color = ['cornsilk', 'aquamarine2', 'firebrick2', 'DodgerBlue4', 'green3', 'DeepPink4', 'orange', 'DeepSkyBlue4', 'gold1']
for x in range(3000):
    drawer.color(choice(color))
    drawer.left(90 * randint(1, 5))
    drawer.forward(20)