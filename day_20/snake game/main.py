from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
score = ScoreBoard()
snake = Snake(screen)
food = Food()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.distance(*food.pos()) < 15:
        print(f"nom nom")
        food.refresh()
        score.increase_score()
        snake.extend()

    # detect collision with wall
    for val in snake.head.xcor(), snake.head.ycor():
        if val > 280 or val < -280:
            print(f"collided.wall at {val}")
            score.game_over()
            snake.reset()
            # game_on = False

    # detect collision with tail
    if snake.collision():
        score.game_over()
        snake.reset()
        # game_on = False







screen.exitonclick()