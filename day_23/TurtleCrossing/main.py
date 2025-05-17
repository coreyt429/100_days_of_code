import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard(player=player, car_manager=car_manager)
screen.listen()
screen.onkeypress(fun=player.start_moving, key="Up")
screen.onkeyrelease(fun=player.stop_moving, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(scoreboard.sleep_timer)
    player.move()
    car_manager.move()
    car_manager.add_car()
    screen.update()
    if player.crossed_finish_line():
        scoreboard.level_up()
    if car_manager.detect_collision(player):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
