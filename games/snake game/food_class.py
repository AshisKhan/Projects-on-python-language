import random
from turtle import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.creation_food()

    def creation_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.speed('fastest')
        self.penup()
        self.goto(x, y)
