from turtle import *
import ball_class

class Paddle(Turtle):
    def __init__(tim,x,y):
        super().__init__()
        tim .shape('square')
        tim.color('white')
        tim.shapesize(stretch_len=1, stretch_wid=5)
        tim.penup()
        tim.goto(x,y)



    def up(tim):
        y_new = tim.ycor() + 20
        tim.goto(tim.xcor(), y_new)

    def down(tim):
        y_new = tim.ycor() - 20
        tim.goto(tim.xcor(), y_new)


