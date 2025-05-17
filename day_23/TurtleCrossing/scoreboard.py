from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, player, car_manager):
        super().__init__()
        self.player = player
        self.level = 1
        self.car_manager = car_manager
        self.display_level()
        self.penup()
        self.hideturtle()
        self.sleep_timer = 0.1

    def level_up(self):
        self.level += 1
        self.player.level_up()
        self.car_manager.level_up()
        self.display_level()
        self.sleep_timer *= .9

    def display_level(self):
        self.clear()
        self.penup()
        self.goto(-280, 265)
        self.write(f"Level: {self.level}", font=FONT, align='left')

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", font=FONT, align='center')