import random
import storage
import time
from loading import loader, clear_screen

# Grid
grid = [] #initalizing grid
for i in range(9):  # fills the grid with 9 rows
    row = [] 
    for j in range(9):  # fills the row with 9 zeros
        row.append(0)
    grid.append(row)
    
# Coordinate system
coordinates = []
for i in range(9):  # fills the grid with 9 rows
    coordinates_row = [] 
    for j in range(9):  # fills the row with 9 zeros
        coordinates_row.append((i,j))
    coordinates.append(coordinates_row)

def visualize(grid):
    # separator = "+" + "---+" * 9  # Separator line for the grid boundaries
    print(" 0   1   2    3   4   5    6   7   8  ")
    separator = '======================================'
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print(separator)  # Print a horizontal separator line after every 3 rows
        else:
            print('--------------------------------------')

        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "|"  # Print a vertical separator line after every 3 columns
            
            # Print the cell value with vertical bars for boundaries
            row += f" {grid[i][j] if grid[i][j] != 0 else ' '} |"
        
        print(f"{row} {i}")
  
# checks that no number repeats in a 3x3 box  
def check_subGrid(row, column, n):
    start_row = 3 * (row // 3) # start of row in a 3x3 subgrid
    start_col = 3 * (column // 3) # start of column in a 3x3 subgrid

    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == n:
                return False
    return True

# checks that no number repeats in a row
def check_row(i,n): # i is the row, n is the a randomly selected number
    if n in grid[i]:
        return False
    return True

# checks that no number repeats in a column
def check_column(j,n): # j is the column
    for i in range(9):
        if grid[i][j] == n:
            return False
    return True

# combines the 3 Sudoku conditions
def is_valid(x, y, n): 
    return check_row(x, n) and check_column(y, n) and check_subGrid(x, y, n)
# returns True if all conditions are met

def fill_grid():
    for i in range(9):
        for j in range(9): # for every entry
            if grid[i][j] == 0:
                # create a list of numbers and shuffle them
                numbers = list(range(1,10))
                random.shuffle(numbers) 
                for num in numbers: # loops through items in shuffled list
                    if is_valid(i, j, num): # checks if an item is valid
                        grid[i][j] = num
                        if fill_grid() == True: # recursive call occurs if valid entry is made, and moves to the next cell in the list
                            return True # if the grid is filled
                        grid[i][j] = 0 # makes the entry 0 and tests next number in shuffled list
                return False # if no numbers can make the grid valid, it exits the current function (in the recusive call)
    return True # if a valid grid is formed

def generate_valid_sudoku():
    fill_grid()
    # answer = grid
    return [row[:] for row in grid] # stores the fully-filled grid as the answer

# DIFFICULTY LEVEL
def difficulty(level): # argument is the level the user chooses
    if level == 5: # extremely difficult
        given_cells = list(range(22,28))
        minimum_filled_cells = 0
    elif level == 4: # difficilt
        given_cells = list(range(28,32))
        minimum_filled_cells = 2
    elif level == 3: # medium
        given_cells = list(range(32,36))
        minimum_filled_cells = 3
    elif level == 2: # easy
        given_cells = list(range(36,50))
        minimum_filled_cells = 4
    elif level == 1: #very easy
        given_cells = list(range(50, 70))
        minimum_filled_cells = 5
    return given_cells, minimum_filled_cells

# Punching holes in our grid to form a puzzle
def create_holes(grid, level):
    given_cells, minimum_filled_cells = difficulty(level) 
    # given cells - number of cells 
    # minimum_filled_cell - minimum number if filled cells in a row 
    random.shuffle(given_cells)
    holes = 81 - (random.choice(given_cells))
    number_of_holes = 0 # initial number of holes
    while number_of_holes < holes:
        for x in range(9):
            i, j = random.choice(coordinates[x]) # picks a random coordinate to remove
            filled_cells = 0 
            for cell in grid[x]:
                if cell != 0:
                    filled_cells += 1 # this counts the number of filled cells in a row
            if filled_cells > minimum_filled_cells: 
            # this continues creating holes until remaining cells go below the threshold
                if grid[i][j] != 0:
                    grid[i][j] = 0
                    grid[8-i][8-j] = 0  # symmetrically remove the corresponding entry
                    number_of_holes += 2  # count both holes
    puzzle = grid
    return puzzle

def play_game():
    answer = generate_valid_sudoku()
    loader("Welcome to Sudoku!",)
    clear_screen()
    loader("Checking system health", emoji = "🟢")
    clear_screen()
    print("These are the rules...\n")
    print(
          '''
          RULES
The sudoku rules are simple. A 9x9 square must be filled in with numbers from 1-9 with no repeated numbers in each line, horizontally or vertically. To challenge you more, there are 3×3 squares marked out in the grid, and each of these squares can’t have any repeat numbers either.

You have only 3 chances to input a wrong number.

To play this game:
1. Enter your name
2. Enter your preferred difficulty level (1-5): 
	- 1: Very Easy
	- 2: Easy
	- 3: Medium
	- 4: Hard
	- 5: Very Hard
3. Enter the coordinates of the cell you want to enter the number into, separated with a comma, with each row and column beginning from the 0th position. For example, 0,5 for the cell in the 0th row, 5th column.
4. Enter the number you wish to put in the cell.

Good luck!'''
          )
    
    # Entering Name and Difficulty level
    name = input("\nEnter your name: \n").strip().capitalize()
    clear_screen()
    print(f"Welcome, {name}!")
    print()
    level = int(input("Enter your difficulty level... 1-5\n"))

    # Creating and displaying puzzle...
    puzzle = create_holes([row[:] for row in answer],level)
    visualize(puzzle)
    print("\n\n")
    

    number_of_tries = 0
    correct_cells = 0

    # Counting the number of cells that are fille in the puzzle
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                correct_cells += 1

    # Initialalizing user coordinates and cell entries
    m = 0
    n = 0
    choice = 0

    # Initializing time
    initialization_time = time.time()

    # Loop to handle playing the game by running it continually
    while correct_cells < 81 and number_of_tries < 3:
        # Starting timer 
        passed_time = time.time() - initialization_time 
        secs = 0
        mins = 0
        hours = 0

        secs = int(passed_time)
        mins = secs // 60
        hours = mins // 60
        
        timer = f'{hours}:{mins%60}:{secs%60}'
        
        print(f"Time elapsed: {timer}") 

        print('\n\n')

        # User coordinates and choice entries
        m,n = input("Enter the cell coordinates: ").split(',')
        m = int(m)
        n = int(n)
        choice = int(input("Enter the digit(0-9) you wish to enter: "))

        # Loop to handle whether user entry was right or wrong
        if answer[m][n] == choice:
            puzzle[m][n] = choice
            print("Correct!!!")
            correct_cells += 1
            visualize(puzzle)
            
            status = "Successful"
        
        else:
            print("WRONG")
            number_of_tries += 1
            print(f"You have {3-number_of_tries} more tries")
            visualize(puzzle)
            status = "Unsuccessful"

    # Ending time and recording time used to play
    end_time = time.time()
    time_used = end_time - initialization_time

    secs = int(time_used)
    mins = secs // 60
    hours = mins // 60

    #Time Used
    final_time = f"{hours}:{mins%60}:{secs%60}"

    print()
    print()

    #Display time used
    print(f"Time Used: {final_time}")


# PERSISTENCE
    info = storage.load_from_storage('Games_Info.txt')
    info[name] = [status, final_time]
    storage.save_to_storage('Games_info.txt', info)

play_game()