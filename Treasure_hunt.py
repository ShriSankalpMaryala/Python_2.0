import random
grid = []

def create_grid():
    for i in range(5):
        row = []
        for j in range (5):
            row.append("_")
        grid.append(row)
    return grid

# create_grid()

def place_treasure():
   row = random.randint(0,4)
   column = random.randint(0,4)
   return row,column

def hint(treasure_row,treasure_column,guess_row,guess_column):
    if guess_row < treasure_row:
        return "move down"
    elif guess_row > treasure_row:
        return "move up"
    elif guess_column < treasure_column:
        return "move right"
    elif guess_column > treasure_column:
        return "move left"
    return "congratulations you found the treasure"

def treasure_hunt():
    grid = create_grid()
    treasure_row,treasure_column = place_treasure()
    print("welcome to this game of trying to find treasure")
    attempts = 0
    
    while True:
        print("current grid: ")
        for row in grid:
            print(" ".join(row))

        try:
            guess_row = int(input("enter the row between 0 - 4: ")) 
            guess_column = int(input("enter the column number from 0 - 4: "))   
        except ValueError:
            print("invalid choice please enter a number between 0 - 4 ")
            continue
        if guess_row not in range(5) or guess_column not in range(5):
            print("invalid choice please enter a number between 0 - 4 ")
            continue
        
        attempts += 1

        if guess_row == treasure_row and guess_column == treasure_column:
            print("congratulations you found the treasure in {} attempts".format(attempts))
            break
        else:
            give_hint = hint(treasure_row,treasure_column,guess_row,guess_column)
            print("hint: {}".format(give_hint))

treasure_hunt()

         
        
            

            
