import turtle
import random
import time

t = turtle.Turtle()
t.shape('square')
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
    food.goto(random.randint(-200, 200), random.randint(-200, 200))
    list_of_foods.append(food)
