import turtle
from turtle import Turtle, Screen
from random import randint
turtle.colormode(255)
tim = Turtle()

num_sides = 3
while num_sides <= 10:
    tim.color (randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)
    num_sides += 1
















screen = Screen()
screen .exitonclick()
