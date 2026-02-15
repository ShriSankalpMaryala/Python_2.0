import turtle
import time
import random
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
dart = turtle.Turtle()
dart.shape("triangle")
dart.color("blue")

dart.penup()
dart.left(90)
dart.goto(0,-280)

fireworks = []
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

def game_over():
    global running
    running = False
    game_over_display = turtle.Turtle()
    game_over_display.hideturtle()
    game_over_display.color("red")
    game_over_display.write("GAME OVER", align="center" , font=("Arial",36,"bold"))
    screen.update()
    time.sleep(2)
    screen.bye(2)


def spawn_fireworks():
    firework = turtle.Turtle()
    firework.penup()
    firework.shape("triangle")
    firework.color(random.choice(["red" , "green" , "blue", "yellow", "pink", "white"]))
    firework.goto(random.randint(-350,350), random.randint(200,300))
    firework.speed = random.uniform(1,8)
    fireworks.append(firework)
    if random.random()<0.2:
        firework.color("black")
        firework.is_bomb = True
    else:
        firework.is_bomb = False
    fireworks.append(firework)

score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-280, 260)
score_display.color("black")
score_display.write("Score: {}".format(score), font=("Arial", 16, "normal"))
def update_score(points):
    global score
    score +=  points
    score_display.clear()
    score_display.write("Score: {}".format(score), font=("Arial", 16, "normal"))


while running:
    screen.update()
    spawn_fireworks()
    for firework in fireworks[:]:
        firework.sety(firework.ycor() - firework.speed)
        if firework.ycor() < -200:
            fireworks.remove(firework)
            firework.hideturtle()
            if dart.distance(firework)< 30:
                if firework.is_bomb:
                    game_over()
                else:
                    update_score(10)
                    fireworks.remove(firework)


























screen.mainloop()



