from turtle import Turtle
import random

COLOURS = ["red", "green", "orange", "purple", "blue", "yellow", "maroon", "white"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLOURS))
        self.speed("fastest")
        self.random_food()

    def random_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.color(random.choice(COLOURS))
        self.goto(x, y)


