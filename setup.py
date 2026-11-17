import turtle as t

def draw_rectangle(pen: t.Turtle, width: int, height: int, centre_x: int, centre_y: int):
    pen.hideturtle()
    pen.speed(0)
    pen.setheading(0)
    pen.penup()
    pen.pencolor("black")

    start_x = centre_x - 0.5*width
    start_y = centre_y + 0.5*height
    pen.teleport(start_x, start_y)
    pen.pendown()

    for i in range(4):
        distance = 0
        if i % 2 == 0:
            distance = width
        else:
            distance = height
        pen.forward(distance)
        pen.rt(90)