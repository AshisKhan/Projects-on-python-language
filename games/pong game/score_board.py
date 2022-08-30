from turtle import *
class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('red')
        self.penup()
        self.goto(x,y)



    def score_board(self):
        self.write(f"{self.score}", font=10)


    def update_score(self):
        self.score += 1
        self.clear()
        self.score_board()

    def bonus_score(self):
        self.score += 7
        self.clear()
        self.score_board()




