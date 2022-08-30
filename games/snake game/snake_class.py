from turtle import *

STARTING_POSITION = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, len(STARTING_POSITION)):
            self.add_segment(x=STARTING_POSITION[i],y=0)

    def add_segment(self,x,y):
        tim = Turtle()
        tim.shape('square')
        tim.color('white')
        tim.penup()
        tim.goto(x,y)
        self.segments.append(tim)

    def increase_length(self):
        self.add_segment(self.segments[-1].xcor(),self.segments[-1].ycor())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[i - 1].xcor()
            y_new = self.segments[i - 1].ycor()
            self.segments[i].goto(x_new, y_new)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
