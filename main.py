import turtle

# constants
UNIVERSAL_RATIO = 0.8
HEADING_FONT_SIZE = 24

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

PLAYER_POS_RATIO = UNIVERSAL_RATIO * 0.5  # 0.5 for half the screen
PLAYER_POSITION_ABS = PLAYER_POS_RATIO * SCREEN_WIDTH

TITLE_POS_RATIO = UNIVERSAL_RATIO * 0.5
TITLE_ALTITUDE = TITLE_POS_RATIO * SCREEN_HEIGHT
TITLE_FONT_SIZE = HEADING_FONT_SIZE

SCOREBOARD_ALTITUDE = TITLE_ALTITUDE - 1.5 * TITLE_FONT_SIZE
SCOREBOARD_FONT_RATIO = UNIVERSAL_RATIO
SCOREBOARD_FONT_SIZE = SCOREBOARD_FONT_RATIO * TITLE_FONT_SIZE
SCOREBOARD_POSITION_ABS = 0.25 * SCREEN_WIDTH
SCOREBOARD_FONT_SIZE = 1.5 * HEADING_FONT_SIZE

# entities
player_scores = [0, 0]

screen = turtle.Screen()
screen.title("Pong in Python")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)

title = turtle.Turtle()
title.penup()
title.hideturtle()
title.goto(0, TITLE_ALTITUDE)
title.write("Pong", font=("Comic Sans", TITLE_FONT_SIZE, "bold"), align="center")

scoreboard1 = turtle.Turtle()
scoreboard2 = turtle.Turtle()

scoreboards = [scoreboard1, scoreboard2]
for scoreboard in scoreboards:
    scoreboard.penup()
    scoreboard.hideturtle()
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
        font=("Comic Sans", HEADING_FONT_SIZE, "bold")
    )
#endfor

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