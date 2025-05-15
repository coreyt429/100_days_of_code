import turtle
from turtle import Turtle, Screen

def square(turt, size=100):
    for _ in range(4):
        turt.pendown()
        turt.forward(size)
        turt.left(90)
        turt.penup()
        print(turt.position())

def triangle(turt, size=100):
    for _ in range(3):
        turt.pendown()
        turt.forward(size)
        turt.left(120)
        turt.penup()
        print(turt.position())



# timmy = Turtle()
# my_screen = Screen()
#
# timmy.shape("turtle")
# timmy.color("DeepSkyBlue")
# timmy.pencolor("coral")
# print(timmy.position())
# square(timmy, 200)
#
# timmy.left(45)
# timmy.forward(75)
# timmy.right(45)
# timmy.pencolor('DarkGreen')
# triangle(timmy, 100)
#
#
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'], )
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'


print(table)


