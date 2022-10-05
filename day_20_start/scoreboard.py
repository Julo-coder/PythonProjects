from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("monospace", 15, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.h_score = int(file.read())
        print(type(self.h_score))
        self.up()
        self.color("white")
        self.ht()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.h_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.h_score:
            self.h_score = self.score
            with open("data.txt", mode="w")as file:
                file.write(str(self.h_score))
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()
