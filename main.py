from ast import While
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.exitonclick()
screen.title('Turtle Crossing')
screen.listen()
screen.tracer(0)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
