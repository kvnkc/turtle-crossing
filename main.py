from turtle import Screen
from player import Player
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.generate_car()
    car_manager.move_car()

    # Detect Player collision
    if player.distance(car_manager) < 30:
        print('game over')

screen.exitonclick()
