import time
import os

# A loader to make the game more interactive
def loader(message, emoji='🔢🔢🔢'):  # Arguments are the message, and a preset emoji
    print(message)
    for i in range(9):
        loading_bar = emoji *i + '.' * (10-i)
        progress = i/10 * 100
        print(f"\r{loading_bar} {progress:.1f}%", end='')
        time.sleep(0.2)
    clear_screen()


def clear_screen(): # Clear the screen of the terminal
    if(os.name == 'posix'):
      os.system('clear')
# clears the screen on MacOS and Linux OS

#Creation of a function that casuses a delay or pause between different lines of code running
def delay(s):
    time.sleep(s)

