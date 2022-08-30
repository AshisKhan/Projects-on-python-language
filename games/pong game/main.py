from turtle import *
import paddle_class
import ball_class
import time
import score_board

screen=Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('pong game')
screen.tracer(0)


right_pad=paddle_class.Paddle(350,0)
left_pad=paddle_class.Paddle(-350,0)

screen.listen()
screen.onkey(right_pad.up, "Up")
screen.onkey(right_pad.down, "Down")
screen.onkey(left_pad.down, "s")
screen.onkey(left_pad.up, "w")

tim=Turtle()
l_score=score_board.Score(-50,250)
r_score=score_board.Score(50,250)
ball=ball_class.Ball()

is_on = True
result=0
right=[]
left=[]
while is_on:
   
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()==280 or ball.ycor()==-280:
        ball.bounce_wall()
    if ball.distance(right_pad)<50 and ball.xcor()>330:
        ball.bounce_paddle()
        r_score.update_score()

    elif ball.distance(left_pad)<50and ball.xcor()<-330:
        ball.bounce_paddle()
        l_score.update_score()


    elif ball.distance(right_pad)>=50 and ball.xcor()>400:

        ball.goto(0,0)
        ball.move()
        left.append(l_score.bonus_score())
        result+=1
    elif ball.distance(left_pad)>=50and ball.xcor()<-400:
        ball.goto(0, 0)
        ball.move()
        right.append(r_score.bonus_score())
        result+=1
        
    if result==10:
        is_on=False
        tim.color("red")
        tim.goto(-50,0)
        tim.write("GAME OVER")
       
        
        





screen.exitonclick()

