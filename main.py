from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
speed = 0.1
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    # Detecting Collision with Wall, Bounce Back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
        speed *= 0.9

    # Detecting if ball misses the paddle
    if ball.xcor() > 380:
        score.l_score_increase()
        ball.reset_position()

    if ball.xcor() < -380:
        score.r_score_increase()
        ball.reset_position()



screen.exitonclick()
