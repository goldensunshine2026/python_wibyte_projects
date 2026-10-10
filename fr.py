import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")
t.pensize(2)
t.color("brown")


# Tree fractal function
def branch(sz, level):
    if level == 0:
        return

    t.forward(sz)

    # Right branch
    t.right(30)
    branch(sz * 0.7, level - 1)

    # Left branch
    t.left(60)
    branch(sz * 0.7, level - 1)

    # Return to the original direction
    t.right(30)
    t.backward(sz)


# Start drawing the tree
t.penup()
t.goto(0, -280)
t.pendown()
t.setheading(90)

branch(100, 8)

t.hideturtle()
turtle.done()