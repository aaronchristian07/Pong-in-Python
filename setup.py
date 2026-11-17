from turtle import Turtle

def init_pen() -> Turtle:
    pen = Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pencolor("black")
    pen.pensize(3)
    return pen

def draw_rectangle(width: int, height: int, centre_x: int, centre_y: int) -> None:
    pen = init_pen()
    pen.setheading(0)
    pen.penup()

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

def draw_dotted_line(start_x: int, start_y: int, length: int, steps: int) -> None:
    pen = init_pen()
    pen.setheading(270)  # south
    pen.teleport(start_x, start_y)

    pen.penup()

    """
    10x + 9y = length
    10x + 4.5x = length
    x = length / 14.5
    x = length / (steps + 0.5 * (steps - 1))
    """
    step_distance = length / (steps + 0.5 * (steps - 1))
    gap_distance = 0.5 * step_distance

    covered_distance = 0
    while covered_distance < length:
        pen.pendown()
        pen.forward(step_distance)
        pen.penup()
        pen.forward(gap_distance)
        covered_distance += (step_distance + gap_distance)
