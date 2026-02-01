import turtle
# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
# Register shapes
turtle.shape("square")
turtle.speed(40)
# Maze grid
maze = [
    "XXXXXXXXXXXXXXX",
    "X             X",
    "X XXXXX XXXXX X",
    "X X     X     X",
    "X X XXX X XXX X",
    "X X   X X X   X",
    "X XXX X X X XXX",
    "X     X X X   X",
    "XXXXX X X X XXX",
    "X     X   X   X",
    "X XXXXX XXXXX X",
    "X             X",
    "XXXXXXXXXXXXX F"
]

# Turtle setup
player = turtle.Turtle()
player.img
player.color("blue")
player.penup()
player.speed(0)


obstacles = []

def create_maze():
    global finish_line
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            actor = maze[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)
            if actor == "A":
                obstacle = turtle.Turtle()
                obstacle.shape("circle")
                obstacle.color("blue")
                obstacle.penup()
                obstacle.goto(screen_x,screen_y)
                obstacles.append(obstacle)
            elif actor == "S":
                finish_line = turtle.Turtle()
                finish_line.shape("rectangle")
                finish_line.color("yellow")
                finish_line.penup()
                finish_line.goto(screen_x, screen_y)
def is_valid_move(x,y):
    for obstacle in obstacles:
        if obstacle.xcor() == x and obstacle.ycor() == y:
            return False
    return True
def move_up():
    new_x = player.xcor()
    new_y = player.ycor() + 24
    if is_valid_move(new_x, new_y):
       player.goto(new_x,new_y)
       check_win()
def move_down():
    new_x = player.xcor()
    new_y = player.ycor() - 24
    if is_valid_move(new_x, new_y):
       player.goto(new_x,new_y)
       check_win()
def move_right():
    new_x = player.xcor() + 24
    new_y = player.ycor()
    if is_valid_move(new_x, new_y):
       player.goto(new_x,new_y)
       check_win()
def move_left():
    new_x = player.xcor() - 24
    new_y = player.ycor()
    if is_valid_move(new_x, new_y):
       player.goto(new_x,new_y) 
       check_win()
def check_win():
    if player.distance(finish_line)< 12:
        player.hideturtle()
        finish_line.hideturtle()
        screen.bye()

        print("Congratulations! You completed the maze.")
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")











create_maze()
player.goto(-264,264)
screen.mainloop()

            