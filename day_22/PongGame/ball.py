from turtle import Turtle
from random import choice
from pong_screen import HEIGHT, WIDTH

SPEED = 0.1
MAX_X = WIDTH // 2 - 20
MIN_X = -1 * MAX_X
MAX_Y = HEIGHT // 2 - 20
MIN_Y = -1 * MAX_Y
X=0
Y=1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white", "white")
        self.shapesize(1)
        self.penup()
        self.goto((0,0))
        self.moving = False
        self.ball_speed = SPEED
        self.vector = self.init_vector()

    def reset_position(self):
        direction = self.vector[0]
        self.ball_speed = SPEED
        self.vector = self.init_vector()
        if not (direction < 0 < self.vector[0] or direction > 0 > self.vector[0]):
            self.bounce(0)
        self.goto(0, 0)

    def init_vector(self):
        velocity = []
        for _ in range(2):
            velocity.append(choice((-1, 1)) * 10)
        return tuple(velocity)

    def set_vector(self, x_val, y_val=None):
        if isinstance(x_val, tuple):
            self.vector = x_val
        else:
            self.vector = (x_val, y_val)

    def bounce(self, idx):
        vector_list = list(self.vector)
        vector_list[idx] *= -1
        self.vector = tuple(vector_list)

    def hit_wall(self):
        if not (MIN_Y < self.ycor() < MAX_Y):
            return Y
        if not (MIN_X < self.xcor() < MAX_X):
            return X
        return -1

    def hit_paddle(self, paddles):
        for paddle in paddles:
            if paddle.hits(self.pos()):
                return True
        return False

    def move(self):
        next_pos = tuple(float(a + b) for a, b in zip(self.pos(), self.vector))
        self.goto(next_pos)

    def speed_up(self):
        self.ball_speed *= 0.9
        # x_val, y_val = self.vector
        # x_val = x_val / abs(x_val) * self.ball_speed
        # y_val = y_val / abs(y_val) * self.ball_speed
        # self.vector = (x_val, y_val)



