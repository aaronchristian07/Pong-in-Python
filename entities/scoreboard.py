from turtle import Turtle
from constants import *

class Scoreboard(Turtle):
    FONT = (FONT_STYLE, TITLE_FONT_SIZE, "bold")

    def __init__(self) -> None:
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.render()

    def render(self) -> None:
        self.clear()
        for x, score in ((-SCOREBOARD_X_ABS, self.left_score),
                         (SCOREBOARD_X_ABS, self.right_score)):
            self.goto(x, SCOREBOARD_ALTITUDE)
            self.write(score, align="center", font=self.FONT)

    def point(self, left: bool) -> None:
        if left:
            self.left_score += 1
        else:
            self.right_score += 1
        self.render()  # re-render new score
