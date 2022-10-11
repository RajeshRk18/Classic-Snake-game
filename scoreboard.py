from turtle import Turtle

ALIGNMENT = ['center', 'left']
FONT = ('Arial', 10, 'bold')


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            try:
                self.high_score = int(data.read())
            except ValueError:
                self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE = {self.score} HIGHEST SCORE = {self.high_score}", align=ALIGNMENT[0], font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../OneDrive/Desktop/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
