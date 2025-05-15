from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.length = 3
        self.segments = []
        self.turns = {}
        self.head = None
        self.segments = []
        self.reset()

    def reset(self):
        for segment in self.segments:
            segment.clear()
            segment.goto(1000, 1000)
            segment.hideturtle()
        self.segments = []
        for idx in range(3):
            self.segments.append(self.new_section((idx * -1 * MOVE_DISTANCE, 0)))
        self.head = self.segments[0]

    def new_section(self, pos):
        new_turtle = Turtle()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.teleport(*pos)
        new_turtle.penup()
        return new_turtle

    def extend(self):
        pos = self.segments[-1].pos()
        self.segments.append(self.new_section(pos))

    def pos(self):
        return self.head.pos()

    def distance(self, x_val, y_val):
        return self.head.distance(x_val, y_val)

    def collision(self):
        pos = self.pos()
        for segment in self.segments[1:]:
            if pos == segment.pos():
                print(f"collided with segment {segment.pos()}")
                return True
        return False

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            pos = self.segments[segment_num - 1].pos()
            self.segments[segment_num].goto(*pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
