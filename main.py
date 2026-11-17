import turtle
from constants import *
from setup import *
from entities.scoreboard import Scoreboard

# entities
player_scores = [0, 0]

screen = turtle.Screen()
screen.tracer(0)
screen.title("Pong in Python")
screen.getcanvas().winfo_toplevel().state("zoomed")  # fullscreen
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)

title = turtle.Turtle()
title.penup()
title.hideturtle()
title.speed(0)
title.goto(0, TITLE_ALTITUDE)
title.write("Pong", font=(FONT_STYLE, TITLE_FONT_SIZE, "bold"), align="center")

scoreboard = Scoreboard()

draw_rectangle(ARENA_WIDTH, ARENA_HEIGHT, 0, 0)
draw_dotted_line(0, ARENA_HEIGHT / 2, ARENA_HEIGHT, 10)

player1 = turtle.Turtle(shape="square")
player2 = turtle.Turtle(shape="square")
players = [player1, player2]
for player in players:
    player.penup()
    if player == players[0]:
        player.teleport(-PLAYER_POSITION_ABS, 0)
    else:
        player.teleport(PLAYER_POSITION_ABS, 0)

    player.shapesize(5, 1)
#endfor

ball = turtle.Turtle("square")
ball.color("red")

def main():
    screen.update()
    screen.tracer(1, 10)
    screen.mainloop()

if __name__ == "__main__":
    main()
