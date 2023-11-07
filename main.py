from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width = 800,height = 600)
score = ScoreBoard()
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
new_ball = Ball()
screen.listen()
screen.onkey(key="Up", fun = r_paddle.Up)
screen.onkey(key="Down", fun = r_paddle.Down)
screen.onkey(key="w", fun = l_paddle.Up)
screen.onkey(key="s", fun = l_paddle.Down)



game_is_on = True
while game_is_on:
    screen.update()
    new_ball.move()
    time.sleep(new_ball.speed_move)
    if new_ball.ycor() > 280 or new_ball.ycor() < -280 :
        new_ball.bounce()
    if new_ball.distance(r_paddle) < 50 and new_ball.xcor()>340 :
        new_ball.speed_up()
        new_ball.paddle_bounce()
    if new_ball.distance(l_paddle) < 50 and new_ball.xcor() < -340 :
        new_ball.speed_up()
        new_ball.paddle_bounce()


    if new_ball.xcor() > 350:
        new_ball.speed_move = 0.01
        new_ball.setposition(0,0)
        new_ball.paddle_bounce()
        score.left_score()

    if new_ball.xcor() < -350:
        new_ball.speed_move = 0.01
        new_ball.setposition(0, 0)
        new_ball.paddle_bounce()
        score.right_score()
screen.exitonclick()