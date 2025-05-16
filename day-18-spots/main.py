from os import environ
from pathlib import Path
from sys import base_prefix

import colorgram
from random import choice, shuffle
import turtle as t

environ["TCL_LIBRARY"] = str(Path(base_prefix) / "tcl" / "tcl8.6")
environ["TK_LIBRARY"] = str(Path(base_prefix) / "tcl" / "tk8.6")

t.colormode(255)

# 10 x 10 pattern of 20 pixel dots

def dot(turtle, position, color, size=20):
    turtle.pendown()
    turtle.teleport(*position)
    turtle.dot(size, color)
    turtle.teleport(*position)

colors = [color.rgb for color in colorgram.extract('image.jpg', 30)]
print(colors)
joe = t.Turtle()
joe.hideturtle()
joe.speed("fastest")
screen = t.Screen()
# (400, 300)
centers = []
x_start = 200
y_start = 200
cols = 10
rows = 10

for x_pos in range(-1 * x_start, x_start + 1, (x_start * 2) // cols):
    for y_pos in range(-1 * y_start, y_start + 1, (y_start * 2) // rows):
        centers.append(tuple([x_pos, y_pos]))
for _ in range(1):
    shuffle(centers)
    for point in centers:
        dot(joe, point, choice(colors), 20)

# for idx in range(24):
#     joe.color(choice(colors))
#     joe.pendown()
#     joe.forward(30)
#     if idx % 3 == 0:
#         joe.left(45)






screen.exitonclick()
