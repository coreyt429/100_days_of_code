from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.refresh()

    def get_high_score(self):
        try:
            with open('high_score.txt') as file:
                input_text = file.read()
                return int(input_text.strip())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open('high_score.txt', 'w') as file:
            file.write(str(self.high_score))

    def increase_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)
        if self.high_score > 0:
            self.goto(150, 260)
            self.write(f"High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        for idx in range(3, 0, -1):
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            self.refresh()
            self.goto(0, 0)
            self.write(f"Game Over: {idx}", True, align=ALIGNMENT, font=FONT)
            self.getscreen().update()
            time.sleep(1)
        self.reset()


    def reset(self):
        self.score = 0
        self.refresh()


