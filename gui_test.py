from pygame import *

import time
import pygame
import sys

#initialising pygame
pygame.init()
font = pygame.font.SysFont(None, 40)
timer = pygame.time.Clock()

grid = [] #initalizing grid

for i in range(9):  # fills the grid with 9 rows
    row = [] 
    for j in range(9):  # fills the row with 9 zeros
        row.append(0)
    grid.append(row)


#defining size of game window
windowsSize = pygame.display.set_mode((900,900)) 
pygame.display.set_caption("Sudoku")

padding = 180

def draw():
    windowsSize.fill((255, 255, 255))

    for i in range(9):
        for j in range(9):
            rect = pygame.Rect(padding+(j * 60), padding+(i * 60), 60, 60)
            pygame.draw.rect(windowsSize, (0, 0, 0), rect, 1)

    for x in range(0, 10, 3):
        pygame.draw.line(windowsSize, (0,0,0), pygame.Vector2(padding+(x * 60), padding+0), pygame.Vector2(padding+(x * 60), padding+540), 5)
        pygame.draw.line(windowsSize, (0,0,0), pygame.Vector2(padding+0, padding+(x * 60)), pygame.Vector2(padding+540, padding+(x * 60)), 5)


def display_numbers():
    for i in range(9):
        for j in range(9):
            output = grid[i][j]
            # print(output)
            text = font.render(str(output), True, pygame.Color(0,0,0))
            windowsSize.blit(text, pygame.Vector2((i*60) + padding + 22, (j*60) + padding + 18))

def timer(startTime):
    secs = 0
    mins = 0
    hours = 0
    elapsed = time.time() - startTime
    secs = int(elapsed)
    hours = mins // 60
    mins = secs // 60
    timer = f'{hours}:{mins%60}:{secs%60}'
    print(timer,end='\r') 

    stopclock = font.render(timer, True, pygame.Color(0,0,0))
    windowsSize.blit(stopclock, pygame.Vector2(600, 100))



def start_screen():
    name = ''
    level = None
    # status = True

    play_button = font.render("PLAY", True, (0,0,0))
    play_rect = play_button.get_rect(topleft=(400,700))

    while level is None or name == '':
        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                    key = pygame.key.name(event.key)
                    if key == '1':
                        level = 1
                    elif key == '2':
                        level = 2
                    elif key == '3':
                        level = 3
                    elif key == '4':
                        level = 4
                    elif key == '5':
                        level = 5
                        
                if event.key == pygame.K_RETURN:
                    if name and level:
                        return level, name
                    
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    if name and level:  
                        return level, name
                    
        windowsSize.fill((255,255,255))

        level_prompt = "1: Very Easy, 2: Easy, 3: Medium, 4: Hard, 5: Very Hard"
        level_text = font.render(level_prompt, True, (0,0,0))
        windowsSize.blit(level_text, (88, 480))

        # cursor = pygame.mouse.get_pos()
        name_input = "Enter your name: "
        input_area = font.render(name_input, True, pygame.Color(0,0,0))
        windowsSize.blit(input_area, pygame.Vector2(330, 250))

        name_area = font.render(name, True, (0, 0, 0))
        windowsSize.blit(name_area, (370, 300))

        
        
        windowsSize.blit(play_button, play_rect)
        pygame.draw.rect(windowsSize, (0,0,0), play_rect, 2)

            # if rect2.collidepoint(event.pos):
            #     msg = "PLAY Button was pressed"
            # if rect3.collidepoint(event.pos):
            #     msg = "STOP Button was pressed"

        pygame.display.update()

    return level or 'Default level', name or ''

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

def main():
    # print(grid)
    while True:
        startTime = time.time()
        level, name = start_screen() # The return value of the startscreen function is the username
        
        if level == 1:
            pass
        elif level == 2:
            # Set easy difficulty parameters
            pass
        elif level == 3:
            # Set medium difficulty parameters
            pass
        elif level == 4:
            # Set hard difficulty parameters
            pass
        elif level == 5:
            pass

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT: 
                    sys.exit()
            
            # start_screen()
            draw()
            display_numbers()
            timer(startTime)
            pygame.display.flip()
    

main()
# print(draw())