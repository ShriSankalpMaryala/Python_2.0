import turtle
# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
# Register shapes
turtle.shape("square")
turtle.speed(100)
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
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)

screen.mainloop()

def create_maze():
    for y in range(len(maze)):
        for x in range(len(maze[y]))
        actor = maze[y][x]
        screen_x = -288 + (x*24)
        screen_y = 288 - (y*24)