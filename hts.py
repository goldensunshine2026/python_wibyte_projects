import turtle
import random
import time
# BONUS: custom snake head shape
turtle.register_shape(
    "snake_head",
    ((-18, 0), (-8, 10), (18, 0), (-8, -10))
)

screen = turtle.Screen()
screen.bgcolor("khaki")
screen.setup(width=600, height=600)

t = turtle.Turtle()
t.shape("snake_head")
t.color("black")
t.penup()

n_foods = 10
list_of_foods = []

for kk in range(n_foods):
    food = turtle.Turtle()
    food.penup()
    food.speed(0)
    food.shape("square")
    food.color("blue")
    food.goto(random.randint(-200, 200), random.randint(-200, 200))
    list_of_foods.append(food)

pen = turtle.Turtle()
pen.penup()
pen.goto(180, 180)
pen.color("black")
pen.hideturtle()

report = turtle.Turtle()
report.penup()
report.goto(0, 0)
report.color("black")
report.hideturtle()

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

caught = [False] * n_foods
segments = []
steps = 0
game_over = False

def game_loop():
    global steps, game_over

    if game_over:
        return

    steps += 1

    # update score
    pen.clear()
    pen.write(len(segments), align="center", font=("Courier", 24, "normal"))

    # check food collision
    for kk in range(len(list_of_foods)):
        if not caught[kk]:
            if t.distance(list_of_foods[kk]) < 20:
                caught[kk] = True
                list_of_foods[kk].color("green")
                segments.append(list_of_foods[kk])

    # move body from back to front
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move first segment to head
    if len(segments) > 0:
        x = t.xcor()
        y = t.ycor()
        segments[0].goto(x, y)

    # move head
    t.forward(20)

    # win condition
    if len(segments) == n_foods:
        if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
            game_over = True
            t.hideturtle()
            for seg in segments:
                seg.hideturtle()
            report.write("Steps Taken: " + str(steps),
                         align="center", font=("Courier", 24, "normal"))
            return

    screen.ontimer(game_loop, 100)

game_loop()
screen.mainloop()

# t.done()