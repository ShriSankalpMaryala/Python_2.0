import turtle
import time
import random
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
dart = turtle.Turtle()
dart.shape("triangle")
dart.color("red")

dart.penup()
dart.left(90)
dart.goto(0,-280)

balloons = []
running = True
def move_left():
    x = dart.xcor() - 30
    if x > -290:
        dart.setx(x)
def move_right():
    x = dart.xcor() + 30
    if x < 290:
        dart.setx(x)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")


def spawn_balloon():
    balloon = turtle.Turtle()
    balloon.penup()
    balloon.shape("circle")
    balloon.color(random.choice(["red" , "green" , "blue", "yellow"]))
    balloon.goto(random.randint(-350,350), random.randint(200,300))
    balloon.speed = random.uniform(1,3)
    balloons.append(balloon)

while running:
    screen.update()
    spawn_balloon()


























screen.mainloop()



