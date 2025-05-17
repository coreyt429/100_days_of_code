"""
Module for pong screen related classes and functions
"""
from turtle import Screen, Turtle
HEIGHT = 600
WIDTH = 800
MAX_X = WIDTH // 2
MIN_X = -1 * MAX_X
MAX_Y = HEIGHT // 2
MIN_Y = -1 * MAX_Y
LINE_LEN = HEIGHT // 20

class PongScreen():
    """
    Class to manage pong screen
    """
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.title("Pong")
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.pencolor("white")
        self.turtle.shapesize(0.5)
        self.turtle.fillcolor("white")
        self.turtle.pensize(11)
        self.turtle.pen()
        self.draw_center_line()
        self.screen.listen()

    def update(self):
        self.screen.update()

    def draw_center_line(self):
        self.turtle.penup()
        self.turtle.goto(x=0, y=MIN_Y)
        self.turtle.setheading(90)
        self.turtle.shape("square")
        draw = False
        for y_val in range(MIN_Y, MAX_Y, LINE_LEN):
            if draw:
                self.turtle.stamp()
                self.turtle.pendown()
                self.turtle.goto(x=0, y=y_val)
                self.turtle.stamp()
                draw = False
            else:
                self.turtle.penup()
                self.turtle.goto(x=0, y=y_val)
                draw=True

    def exitonclick(self):
        self.screen.exitonclick()

if __name__ == "__main__":
    screen = PongScreen()
    screen.exitonclick()