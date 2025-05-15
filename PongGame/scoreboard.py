from turtle import Turtle

FONT = ("Courier", 80, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scores = {
            "l": 0,
            "r": 0
        }
        self.positions = {
            "l": (-100, 180),
            "r": (100, 180)
        }
        self.show_score()

    def show_score(self):
        self.clear()
        for side, score in self.scores.items():
            self.goto(*self.positions[side])
            self.write(score, align="center", font=FONT)
