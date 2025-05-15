from turtle import Turtle

WIDTH = 20
HEIGHT = 100
MAX_Y = 250
MIN_Y = -1 * MAX_Y
TOP = -1
BOTTOM = 0

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.cfg = {
            'center': (-350, 0),
            'up': 'w',
            'down': 's'
        }
        if side == 'right':
            self.cfg = {
                'center': (350, 0),
                'up': 'Up',
                'down': 'Down'
            }
        self.penup()
        self.shape("square")
        self.color("white", "white")
        self.speed("fastest")
        self.shapesize(stretch_wid=HEIGHT // WIDTH, stretch_len=1)
        self.center()
        self.moving = False
        self.direction = 'up'
        self.getscreen().onkeypress(fun=self.start_up, key=self.cfg['up'])
        self.getscreen().onkeypress(fun=self.start_down, key=self.cfg['down'])
        self.getscreen().onkeyrelease(fun=self.stop_moving, key=self.cfg['up'])
        self.getscreen().onkeyrelease(fun=self.stop_moving, key=self.cfg['down'])

    def start_up(self):
        self.moving = True
        self.direction = "up"

    def start_down(self):
        self.moving = True
        self.direction = "down"

    def stop_moving(self):
        self.moving = False

    def move(self):
        func_map = {
            'up': self.up,
            'down': self.down
        }
        if self.moving:
            func_map[self.direction]()

    def can_go_up(self):
        """
        Method to determine if the paddle can go up
        :return: bool
        """
        if self.ycor() < MAX_Y:
            return True
        return False

    def can_go_down(self):
        """
        Method to determine if the paddle can go up
        :return: bool
        """
        if self.ycor() > MIN_Y:
            return True
        return False

    def up(self):
        if self.can_go_up():
            x_pos, y_pos = self.pos()
            self.goto(x_pos, y_pos + WIDTH)

    def down(self):
        if self.can_go_down():
            x_pos, y_pos = self.pos()
            self.goto(x_pos, y_pos - WIDTH)

    def center(self):
        """
        Center paddle on self.cfg['center']
        """
        x_val, y_val = self.cfg['center']
        self.goto(x=x_val, y=y_val)

    def hits(self, pos):
        x_val, y_val = self.pos()

        if y_val - (HEIGHT // 2) <= pos[1] <= y_val + (HEIGHT // 2):
            if x_val < 0: # left side
                if pos[0] <= x_val + WIDTH:
                    return True
            else: # right side
                if pos[0] >= x_val - WIDTH:
                    return True
        return False



