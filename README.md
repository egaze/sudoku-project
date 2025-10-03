# Sudoku Game Project

Welcome to the Sudoku Game Project! This repository contains a classic Sudoku game implemented in Python, featuring both a **terminal-based** and a **graphical (Pygame)** interface. Challenge yourself, track your progress, and enjoy a smooth user experience with animated loaders and persistent stats.

---

## Features

- **Classic Sudoku Gameplay:** 9x9 grid, fill rows, columns, and 3x3 boxes with numbers 1–9.
- **Difficulty Levels:** Five levels from Very Easy to Very Hard.
- **Terminal Mode:** Play interactively in your terminal.
- **Graphical Mode:** Play with a GUI using Pygame. (Working on it)
- **Progress Tracking:** Game results and times are saved in [`Games_Info.txt`](Games_Info.txt).
- **Animated Loaders:** Engaging loading screens and terminal clearing.

---

## File Overview

| File                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| [`sudoku.py`](sudoku.py)         | Main terminal-based Sudoku game logic and user interaction.                  |
| [`gui_test.py`](gui_test.py)       | Pygame-based graphical interface for Sudoku.                               |
| [`storage.py`](storage.py)        | Handles saving and loading game progress and stats.                         |
| [`loading.py`](loading.py)        | Loader animations and utility functions for terminal mode.                  |
| [`Games_Info.txt`](Games_Info.txt)    | Stores player names, results, and times.                                    |

---

## How to Play

### Terminal Version

1. Run the game:
    ```sh
    python sudoku.py
    ```
2. Follow the prompts:
    - Enter your name.
    - Select a difficulty level (1–5).
    - Enter cell coordinates and your chosen number.
    - You have 3 chances for incorrect entries.
3. Your results and time will be saved automatically.

### Graphical Version (Pygame)

1. Install Pygame if needed:
    ```sh
    pip install pygame
    ```
2. Run the GUI:
    ```sh
    python gui_test.py
    ```
    (Still working on it)
3. Enter your name and select difficulty using your keyboard.
4. Click "PLAY" to start and interact with the grid.

---

## Saving & Loading Progress

Game results are stored in [`Games_Info.txt`](Games_Info.txt) using the [`storage.load_from_storage`](storage.py) and [`storage.save_to_storage`](storage.py) functions.

---

## Requirements

- Python 3.7+
- Pygame (for GUI mode)

---

## Credits

Developed by (Me)[Eyiram Gaze](https://github.com/egaze) & [Daniel Asenso-Gyambibi](https://github.com/DanielAsenso-G)

---

Enjoy Sudoku and challenge your mind! If you have suggestions or want to contribute, feel free to open an issue or pull request.
