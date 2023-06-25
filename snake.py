# A simple terminal based snake clone
import os
import random
from pytimedinput import timedInput
from colorama import Fore, Back
# Built in way to clear terminal
clear = lambda: os.system('clear')

# Colors
red = Back.RED
green = Back.GREEN
yellow = Back.YELLOW
white = Back.WHITE
reset = Back.BLACK
grey = Back.WHITE

# Print everything in terminal
def renderGrid():
    for r in range(HEIGHT):
        for c in range(WIDTH):
            if c in [0, WIDTH - 1] or r in [0, HEIGHT - 1]: # Draw edge
                print(grey + "  " + reset, end = "")
            elif (c, r) == applePos: # Draw apple
                print(red +"  ", end = "")
            elif (c, r) in snake:
                if (c, r) == snake[-1]: # Draw snake head
                    print(white + "  ", end = "")
                else: # Draw snake body
                    print(yellow + "  ", end = "")
            else: # Draw empty cell
                print(green + "  ", end = "")
        print()

# Change the value of applePos
def newApple():
    x, y = snake[-1]
    while (x, y) in snake:
        x = random.randint(1,WIDTH - 2)
        y = random.randint(1,HEIGHT - 2)
    global applePos
    applePos = (x, y)

# Do all of the game logic and return 2 if the game is over
def updateSnake():
    global score
    newHead = (snake[-1][0] + direction[0], snake[-1][1] + direction[1])
    if newHead in snake:
        return 2
    if newHead[0] in [0, WIDTH - 1] or newHead[1] in [0, HEIGHT - 1]:
        return 2
    if newHead == applePos:
        newApple()
        score += 1
    snake.append(newHead)
    if len(snake) > score:
        snake.pop(0)
        
# Read input from user for 1.0/FPS secounds and keep the last input if nothing was clicked in the latest window
def getDir(direction):
    newDirection = DIRECTIONS.get(timedInput("", 1.0 / FPS)[0].lower(), direction)
    if newDirection[0] * -1 == direction[0] and newDirection[1] * -1 == direction[1]:
        return direction
    return newDirection

#settings
WIDTH = 32
HEIGHT = 32
FPS = 10

#setup
DIRECTIONS = {"a": (-1, 0), "d": (1, 0), "w": (0, -1), "s": (0, 1), "q": (0, 0), "h": (-1, -1)}
direction = DIRECTIONS["a"]
snake = [(WIDTH // 2, HEIGHT // 2), (WIDTH // 2 + 1, HEIGHT // 2), (WIDTH // 2 + 1, HEIGHT // 2 + 1)]
score = len(snake)
starting = score
applePos = (0, 0)
newApple()
#game loop
while True:
    clear()
    renderGrid()
    direction = getDir(direction)
    if updateSnake() == 2 or direction == (0, 0): #end the game
        clear()
        break
    if direction == (-1, -1): #display help menu
        clear()
        print("This is a simple snake game\nyou can controll the snake with these controlls:\nw - up\na - left\ns - down\nd - right\n\nTo quit to game enter 'q'\nTo get help enter 'h'\n")
        break

#end game
print("Svaka cast!\nVas rezultat je: " + str(score - starting))
