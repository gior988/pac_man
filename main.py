import turtle
import time
screen=turtle.Screen()

pacman=turtle.Turtle()
pacman.shape("circle")
pacman.shapesize(2,2)
pacman.penup()
pacman_direction="up"
pacman.setheading(90)
pacman.goto(-300,250)


def pacman_go_up():
    pacman.setheading(90)
    pacman_direction="up"

screen.onkeypress(pacman_go_up,"Up")
screen.listen()

while True:
    screen.update()