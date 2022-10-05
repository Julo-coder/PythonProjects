import turtle as t
import random
t.colormode(255)

def random_color():
    r = random.randint(0, 200)
    g = random.randint(0, 200)
    b = random.randint(0, 200)
    return r, g, b

tim = t.Turtle()
my_screen = t.Screen()
tim.speed(20)
tim.width(7)
directions = [0, 90, 180, 270]
num_times = random.randint(0, 201)

for i in range(num_times):
    tim.color(random_color())
    tim.forward(10)
    tim.setheading(random.choice(directions))





