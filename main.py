from turtle import Screen
from player import FINISH_LINE_Y, Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(car_manager.move_speed)
    car_manager.generate_car()
    car_manager.move_car()

    # Detect Player collision
    for car in car_manager.all_cars:
        if player.distance(car) < 27:
            game_is_on = False
            scoreboard.game_over()

    # Detect Player cross finish line and update level
    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        car_manager.car_speed()
        scoreboard.level_up()
        print(car_manager.move_speed)

screen.exitonclick()
