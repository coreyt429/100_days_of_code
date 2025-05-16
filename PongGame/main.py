from os import environ
from pathlib import Path
from sys import base_prefix

from paddle import Paddle
from pong_screen import  PongScreen
from time import  sleep
from ball import Ball
from scoreboard import Scoreboard

environ["TCL_LIBRARY"] = str(Path(base_prefix) / "tcl" / "tcl8.6")
environ["TK_LIBRARY"] = str(Path(base_prefix) / "tcl" / "tk8.6")

def quit_game():
    global game_on
    game_on = False

# init screen
screen = PongScreen()
# init paddles
left = Paddle("left")
right = Paddle("right")
# init ball
ball = Ball()
# init scoreboard
scoreboard = Scoreboard()

# redraw center line, this was needed to correct an arrow point
# that was being left on the line
screen.draw_center_line()
# update screen
screen.update()
screen.screen.onkey(fun=quit_game, key="q")

# game loop
game_on = True
while game_on:
    sleep(ball.ball_speed)
    for item in [left, right, ball]:
        item.move()
    hit_wall = ball.hit_wall()
    hit_paddle = ball.hit_paddle([left, right])
    if hit_paddle:
        ball.bounce(0)
        ball.speed_up()
    elif hit_wall == 1:
        ball.bounce(1)
    elif hit_wall == 0:
        if ball.xcor() < 0:
            scoreboard.scores['r'] += 1
        else:
            scoreboard.scores['l'] += 1
        scoreboard.show_score()
        ball.reset_position()
        # point scored based on ball position
    screen.update()

screen.exitonclick()