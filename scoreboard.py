from turtle import Turtle

FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-280, 270)
        self.write(f"level: {self.level}", align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
