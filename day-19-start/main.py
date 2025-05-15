import turtle as t
import random

TURN_DEGREE = 10
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

# def move_forward(steps=10):
#     joe.forward(steps)
#
# def move_backward(steps=10):
#     joe.backward(steps)
#
# def turn_left():
#     joe.left(TURN_DEGREE)
#
# def turn_right():
#     joe.right(TURN_DEGREE)
#
# def clear():
#     joe.clear()
#     joe.teleport(0, 0)
#     joe.setheading(0)

def random_color():
    color = []
    for _ in range(3):
        color.append(random.randint(0,255))
    return tuple(color)

def generate_turtles(color_list):
    new_turtles = []
    for color in color_list:
        new_turtle = t.Turtle()
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.speed("fastest")
        new_turtle.shape("turtle")
        new_turtles.append(new_turtle)
    return new_turtles

def starting_lineup(turtle_list):
    count = len(turtle_list)
    spacing = SCREEN_HEIGHT // (count + 1)
    x_pos = -1 * SCREEN_WIDTH // 2 + 10
    for idx, turtle in enumerate(turtle_list):
        turtle.goto(x=x_pos, y=250 - ((idx + 2) * spacing))
        print(turtle.position())

def race_forward(turtle):
    turtle.forward(random.randint(1,10))


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# # init turtle
# joe = t.Turtle()
# init screen
screen = t.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter color ({', '.join(colors)}): ")
turtles = generate_turtles(colors)
starting_lineup(turtles)
winner = None
while not winner:
    for current_turtle in turtles:
        current_turtle.forward(random.randint(1,10))
        print(f"Turtle: {current_turtle.pencolor()} is at {current_turtle.position()}")
        if current_turtle.xcor() >= 230:
            winner = current_turtle.pencolor()
            break
if winner == user_bet.lower():
    print(f"You win, {winner} came in first 🏆")
else:
    print(f"You lost, {winner} came in first 😭")



# # open listener
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="c", fun=clear)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)


t.mainloop()

screen.exitonclick()



