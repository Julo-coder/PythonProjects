###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     final = (r, g, b)
#     rgb_colors.append(final)
# print(rgb_colors)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.pensize(20)
tim.speed(20)
tim.ht()
tim.up()

def painting():
    y = 50
    while y != 550:
        for dot_count in range(10):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)
            if dot_count == 9:
                tim.goto(0, y)
                print(tim.pos())
                y += 50
        if y == 550:
            tim.goto(0, 0)
            break

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
 (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
 (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
 (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

painting()




my_screen = t.Screen()
my_screen.exitonclick()