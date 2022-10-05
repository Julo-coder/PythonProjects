from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.left(90)
        self.starting_pos()


    def move(self):
        self.forward(MOVE_DISTANCE)

    def starting_pos(self):
        self.goto(STARTING_POSITION)

