import turtle
import random
import time
turtle.speed(0)
turtle.colormode(255)
def draw_circles():
    turtle.penup()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    turtle.goto(x,y)

    turtle.color(
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
    )
    
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(random.randint(20,60))
    turtle.penup()
    turtle.end_fill()
    turtle.hideturtle()

delay = 0.8
start_time = time.time()
for i in range(15):
    draw_circles()
    time.sleep(delay)
    turtle.clear()
    delay = max(0.01,delay - 0.05)
end_time = time.time()
elapsed_time = round(end_time - start_time, 2)
turtle.penup()
turtle.goto(0,0)
turtle.color("blue")
turtle.pendown()
turtle.write( "Total animation time: {} seconds".format(elapsed_time),
    align="center",
    font=("Arial", 16, "bold"))
turtle.done()

