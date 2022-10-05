import turtle as t
import random
t.colormode(255)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = t.Turtle()
degree = 6
tim.speed(20)
num_times = int(360 / degree)
screen = t.Screen()

for _ in range(num_times):
    tim.color(change_color())
    tim.circle(60)
    tim.setheading(degree)
    degree += 6



screen.exitonclick()