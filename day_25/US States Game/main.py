import turtle
from turtle import Turtle
import math
import pandas

STEP=20

screen = turtle.Screen()
screen.screensize(800,600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
print(screen.screensize())


def calc_heading(origin, destination):
    # Get the current position of the turtle
    current_x, current_y = origin
    new_x, new_y = destination

    # Calculate the angle to the destination point
    angle = math.degrees(math.atan2(new_y - current_y, new_x - current_x))

    # Set the turtle's heading to this angle
    return angle

def place_state(state_df):
    origin = (0, 300)
    state_name = state_df.state.to_list()[0]
    x_cor = int(state_df.x.to_list()[0])
    y_cor = int(state_df.y.to_list()[0])
    destination = (x_cor, y_cor)
    state_turtle = Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.teleport(*origin)
    state_turtle.setheading(calc_heading(origin, destination))
    while state_turtle.distance(destination) > STEP:
        state_turtle.forward(STEP)
        state_turtle.clear()
        state_turtle.write(state_name, align="center")
    state_turtle.goto(*destination)
    state_turtle.clear()
    state_turtle.write(state_name, align="center")

state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()
print(all_states)
game_on = True
title = "Guess the State"
correct_guesses = []
guesses = []
while game_on:
    if correct_guesses:
        title = f"{len(correct_guesses)}/50 States Correct"
    answer_state = turtle.textinput(title=title, prompt="What's another state name?").title()
    if answer_state.lower() == 'exit':
        break
    guesses.append(answer_state.title())
    state = state_data[state_data["state"] == answer_state]
    if len(state) == 1:
        state_name = state.state.to_list()[0]
        if state_name not in correct_guesses:
            place_state(state)
            correct_guesses.append(state_name)
    if len(correct_guesses) == 50:
        game_on = False
print("Correct guesses:")
for state in correct_guesses:
    print(f"    {state}")
print()
print("Incorrect guesses:")
for guess in guesses:
    if guess not in correct_guesses:
        print(f"    {guess}")
print()
print("Missing States:")
missing_states = [state for state in all_states if state not in correct_guesses]
for state in missing_states:
    print(f"    {state}")
new_data = pandas.DataFrame(missing_states)
print(new_data)
new_data.to_csv("missing_states.csv")
screen.exitonclick()
