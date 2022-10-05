from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.bk(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)

def clear_screen():
    tim.reset()

screen.listen()
screen.onkey("w", move_forwards)
screen.onkey("s", move_backwards)
screen.onkey("a", turn_left)
screen.onkey("d", turn_right)
screen.onkey("c", clear_screen)
screen.exitonclick()