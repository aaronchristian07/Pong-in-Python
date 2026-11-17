import turtle
from constants import *

# entities
player_scores = [0, 0]

screen = turtle.Screen()
screen.title("Pong in Python")
screen.getcanvas().winfo_toplevel().state("zoomed")  # fullscreen
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)

title = turtle.Turtle()
title.penup()
title.hideturtle()
title.speed(0)
title.goto(0, TITLE_ALTITUDE)
title.write("Pong", font=(FONT_STYLE, TITLE_FONT_SIZE, "bold"), align="center")

scoreboard1 = turtle.Turtle()
scoreboard2 = turtle.Turtle()

scoreboards = [scoreboard1, scoreboard2]
for scoreboard in scoreboards:
    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.speed(0)
    position = None
    score = 0
    if scoreboard == scoreboards[0]:
        position = -SCOREBOARD_POSITION_ABS
        score = player_scores[0]
    else:
        position = SCOREBOARD_POSITION_ABS
        score = player_scores[1]
    
    scoreboard.goto(position, SCOREBOARD_ALTITUDE)
    scoreboard.write(
        f"{score}",
        align="center",
        font=(FONT_STYLE, HEADING_FONT_SIZE, "bold")
    )
#endfor

border = turtle.Turtle()
border.teleport(-ARENA_WIDTH / 2, ARENA_HEIGHT / 2)
border.pendown()
border.pencolor("black")
border.speed(0)
border.hideturtle()
for i in range (4):
    distance = 0
    if i % 2 == 0:
        distance = ARENA_WIDTH
    else:
        distance = ARENA_HEIGHT
    border.forward(distance)
    border.rt(90)

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
    print("Hello World")
    input()

if __name__ == "__main__":
    main()