from turtle import Turtle, Screen, colormode
import random

color_list = [
              (219, 156, 91),
              (127, 166, 192),
              (55, 102, 146),
              (182, 65, 29),
              (238, 209, 96),
              (128, 178, 146),
              (229, 66, 99),
              (62, 118, 83),
              (240, 65, 36),
              (213, 126, 151),
              (10, 43, 66),
              (182, 19, 9),
              (143, 71, 98),
              (173, 147, 53),
              (80, 158, 111),
              (65, 40, 20),
              (165, 22, 35),
              (239, 157, 173),
              (158, 212, 199),
              (28, 87, 55),
              (17, 60, 129),
              (244, 166, 152),
              (20, 53, 37),
              (107, 120, 168),
              (173, 188, 217),
              (70, 42, 50)
              ]
colormode(255)

dot = Turtle()
dot.shape('circle')
dot.width(10)
dot.speed(50)
dot.up()
dot.goto(-200, -200)

screen = Screen()


def draw_line(num):
    i = 1
    for _ in range(num):
        dot.dot(20,random.choice(color_list))
        dot.up()
        if i < num:
            dot.forward(50)
        i += 1


def draw_grid(num):
    num2 = int(num/2)
    for x in range(num2):
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(0)
        draw_line(num)
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(180)
        draw_line(num)


draw_grid(10)
screen.exitonclick()
