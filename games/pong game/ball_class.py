from turtle import *
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.x_update=10
        self.y_update=10



    def move(self):
       x_new=self.xcor()+self.x_update
       y_new=self.ycor()+self.y_update
       self.penup()
       self.goto(x_new,y_new)

    def bounce_paddle(self):
       self.x_update=-1*self.x_update

    def bounce_wall(self):
        self.y_update=-1*self.y_update