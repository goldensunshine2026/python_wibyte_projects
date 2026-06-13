import turtle
import random
import time

# Create an oval shape
turtle.register_shape(
    "oval_head",
    ((-15, 0), (-12, 6), (-6, 10), (6, 10), (12, 6),
     (15, 0), (12, -6), (6, -10), (-6, -10), (-12, -6))
)

t = turtle.Turtle()
t.shape('oval_head')
t.color("black")

n_foods = 10
list_of_foods = []

for kk in range(n_foods):
    food = turtle.Turtle()
    print(food)
    food.penup()
    food.speed(0)
    food.shape("square")
    food.color("blue")
    food.goto(random.randint(-300, 300), random.randint(-300, 300))
    list_of_foods.append(food)

pen = turtle.Turtle()
pen.penup()
pen.goto(300, 300)
pen.color("white")
pen.hideturtle()

report = turtle.Turtle()
report.penup()
report.goto(0, 0)
report.color("white")
report.hideturtle()

started = 0


def right():
    if t.heading() != 180.0:
        t.setheading(0.0)


def left():
    if t.heading() != 0.0:
        t.setheading(180.0)


def up():
    if t.heading() != 270.0:
        t.setheading(90.0)


def down():
    if t.heading() != 90.0:
        t.setheading(270.0)


steps = 0

ts = t.screen
ts.setup(width=800, height=800)
ts.bgcolor("khaki")

# Draw bigger playing boundary
border = turtle.Turtle()
border.speed(0)
border.color("black")
border.penup()
border.goto(-350, -350)
border.pendown()

for _ in range(4):
    border.forward(700)
    border.left(90)

border.hideturtle()

ts.onkey(right, "Right")
ts.onkey(left, "Left")
ts.onkey(up, "Up")
ts.onkey(down, "Down")
ts.listen()

caught = [False] * n_foods
segments = []

game_over = False

while game_over == False:
    steps = steps + 1

    pen.clear()
    pen.write(
        len(segments),
        align="center",
        font=("Courier", 24, "normal")
    )

    for kk in range(len(list_of_foods)):
        if not caught[kk]:
            if t.distance(list_of_foods[kk]) < 20:
                caught[kk] = True
                list_of_foods[kk].color("green")
                segments.append(list_of_foods[kk])

    # move the end segment in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = t.xcor()
        y = t.ycor()
        segments[0].showturtle()
        segments[0].goto(x, y)

    t.forward(20)

    # Boundary collision
    if (t.xcor() > 350 or t.xcor() < -350 or
            t.ycor() > 350 or t.ycor() < -350):

        game_over = True
        time.sleep(1)

        t.clear()
        t.hideturtle()

        for kk in range(len(segments)):
            segments[kk].hideturtle()

        report.clear()
        report.write(
            "GAME OVER\nHit Boundary\nSteps Taken: " + str(steps),
            align="center",
            font=("Courier", 24, "normal")
        )

    if t.xcor() > 10:
        started = 1

    if len(segments) == n_foods:
        if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
            game_over = True
            time.sleep(1)

            t.clear()
            t.hideturtle()

            for kk in range(len(segments)):
                segments[kk].hideturtle()

            report.write(
                "You Win!\nSteps Taken: " + str(steps),
                align="center",
                font=("Courier", 24, "normal")
            )

    time.sleep(0.1)

turtle.done()