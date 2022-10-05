import turtle
import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter the color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtle = []

for turtles in range(len(colors)):
    new_turtle = t.Turtle("turtle")
    new_turtle.color(colors[turtles])
    new_turtle.up()
    new_turtle.goto(x = -230, y = y_position[turtles])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winnig_turtle = turtle.pencolor()
            if winnig_turtle == user_bet:
                print(f"Your turtle {winnig_turtle} win.")
            else:
                print(f"You lose. The turtle which win is {turtle.pencolor()}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
