from turtle import *


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('red')
        self.penup()
        self.goto(x=0, y=270)
        self.score_board()

    def score_board(self):
        self.write(f"score:{self.score}", font=10)

    def update_score(self):
        self.score += 1
        self.clear()
        self.score_board()

    def game_over(self):

        self.hideturtle()
        self.penup()
        self.goto(-35, 0)
        self.write("GAME OVER  😩 😭", font = 20)
