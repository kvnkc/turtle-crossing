from turtle import Screen
from player import Player
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
