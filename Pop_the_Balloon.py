import turtle
import time
import random
screen = turtle.Screen()
screen.bgcolor("white")
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

def spawn_balloon():
    balloon = turtle.Turtle()
    balloon.penup()
    balloon.shape("circle")
    balloon.color(random.choice(["red" , "green" , "blue", "yellow"]))
    balloon.goto(random.randint(-350,350), random.randint(200,300))
    balloon.speed = random.uniform(50,80)
    if random.random()<0.2:
        balloon.color("black")
        balloon.is_bomb = True
    else:
        balloon.is_bomb = False
    balloons.append(balloon)
    
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
    spawn_balloon()
    for balloon in balloons[:]:
        balloon.sety(balloon.ycor() - balloon.speed)
        if balloon.ycor() < -200:
            balloons.remove(balloon)
            balloon.hideturtle()
            if dart.distance(balloon)< 30:
                if balloon.is_bomb:
                    game_over()
                else:
                    update_score(10)
                    balloons.remove(balloon)
                    balloon.hideturtle()


























screen.mainloop()



