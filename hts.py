import turtle
import random

# -------------------- Screen --------------------

screen = turtle.Screen()
screen.bgcolor("khaki")
screen.setup(width=600, height=600)
screen.title("Snake Game")

# -------------------- Snake head --------------------

triangle = (
    (0, 20),      # tip
    (8, -12),
    (-8, -12)
)

screen.register_shape("snake_head", triangle)

t = turtle.Turtle()
t.shape("snake_head")
t.color("black")
t.penup()
t.speed(0)
t.setheading(90)

# -------------------- Food --------------------

n_foods = 10
list_of_foods = []

for kk in range(n_foods):
    food = turtle.Turtle()
    food.penup()
    food.speed(0)
    food.shape("square")
    food.color("blue")
    food.goto(random.randint(-200, 200),
              random.randint(-200, 200))
    list_of_foods.append(food)

# -------------------- Score --------------------

pen = turtle.Turtle()
pen.penup()
pen.goto(180, 180)
pen.color("black")
pen.hideturtle()

report = turtle.Turtle()
report.penup()
report.color("black")
report.hideturtle()

# -------------------- Controls --------------------

def right():
    if t.heading() != 180:
        t.setheading(0)


def left():
    if t.heading() != 0:
        t.setheading(180)


def up():
    if t.heading() != 270:
        t.setheading(90)


def down():
    if t.heading() != 90:
        t.setheading(270)


screen.listen()
screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(up, "Up")
screen.onkey(down, "Down")

# -------------------- Variables --------------------

caught = [False] * n_foods
segments = []
steps = 0
game_over = False

# -------------------- Game loop --------------------

def game_loop():
    global steps, game_over

    if game_over:
        return

    steps += 1

    # Display the score
    pen.clear()
    pen.write(
        f"Score: {len(segments)}",
        align="center",
        font=("Courier", 18, "normal")
    )

    # Check for collisions with food
    for kk in range(len(list_of_foods)):
        if not caught[kk]:
            if t.distance(list_of_foods[kk]) < 20:
                caught[kk] = True
                list_of_foods[kk].color("green")
                segments.append(list_of_foods[kk])

    # Move the tail
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the first segment
    if len(segments) > 0:
        segments[0].goto(t.xcor(), t.ycor())

    # Move the head
    t.forward(20)

    # Winning condition
    if len(segments) == n_foods:
        if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
            game_over = True

            t.hideturtle()

            for seg in segments:
                seg.hideturtle()

            report.write(
                "Steps Taken: " + str(steps),
                align="center",
                font=("Courier", 24, "normal")
            )
            return

    screen.ontimer(game_loop, 100)


# -------------------- Start the game --------------------

game_loop()
screen.mainloop()