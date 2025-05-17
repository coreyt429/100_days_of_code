from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CARS=25
MAX_Y=250
MIN_Y=-250
MIN_X=-270
MAX_X=270

class Car(Turtle):
    def __init__(self, x_pos=270):
        super().__init__()
        self.penup()
        self.color(choice(COLORS))
        self.goto(x_pos, randint(MIN_Y, MAX_Y))
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.setheading(180)

    def move(self):
        self.forward(MOVE_INCREMENT)

    def detect_collision(self, player):
        p_y_cor = player.ycor()
        x_cor, y_cor = self.pos()
        # player can't leave the center line
        # so check x_cor first.
        # player range is -10 to 10
        # car is 40 long, so
        if -30 < x_cor < 30:
            print(f"{x_cor} is in range, check {y_cor}")
            if abs(y_cor - p_y_cor) < 20:
                print(f"splat {self.pos()} hit {player.pos()}")
                return True
        return False



class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_count = CARS
        for _ in range(self.car_count):
            self.cars.append(Car(randint(MIN_X, MAX_X)))

    def level_up(self):
        self.car_count += 1
        pass

    def move(self):
        cars = []
        for idx, car in enumerate(self.cars):
            car.move()
            if car.xcor() >= -350:
                cars.append(car)
        self.cars = cars
        # while len(self.cars) < self.car_count:
        #     self.cars.append(Car())

    def add_car(self):
        if randint(1, 6) == 3:
            self.cars.append(Car())

    def detect_collision(self, player):
        for car in self.cars:
            if car.detect_collision(player):
                return True
        return False


