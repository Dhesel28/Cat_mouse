# Cat and Mouse Game

## Introduction

This is a simple implementation of a Cat and Mouse game using the Pygame library inspired by Four in row game. The game allows two players to take turns placing their pieces (Cat and Mouse) on a grid. The first player to get four of their pieces in a row wins the game.

## How to Play

1. Make sure you have Python and Pygame installed on your system.
2. Ensure you have the necessary image and sound files in the same directory as the Python script (`cat.png`, `mouse.png`, `winning.mp3`, `cat_noise.mp3`, `player2.mp3`).
3. Run the Python script `cat_mouse_game.py`.

## Game Controls

- mouse click: Place a chip on the grid and you can hover your chips.
- 'r' key: Reset the game.

## Rules

- Players take turns placing their pieces on the grid.
- The first player to get four of their pieces in a row (horizontally, vertically, or diagonally) wins the game.
- The game will display the winner and the duration of the game.

## Game Logic

The game operates on a grid with 6 rows and 7 columns. Each player (Cat and Mouse) takes turns to place their respective pieces on the grid. The game logic is implemented as follows:

- The grid is represented as a 2D list, where each element can be 0 (empty), 1 (Cat), or 2 (Mouse).
- The `check_valid_location(col)` method ensures that a player can only place their piece in an unoccupied column.
- The `open_row(col)` method finds the lowest available row in a given column for piece placement.
- The `drop_chips(row, col, chips)` method updates the grid with the player's piece.
- The `check_victory(chips)` method checks for a winning condition in horizontal, vertical, and diagonal directions.

## File Descriptions

- `cat_mouse_game.py`: contains the Python code for the game.
- `cat.png`, `mouse.png`: Images used for the game pieces.
- `winning.mp3`, `cat_noise.mp3`, `player2.mp3`: Sound files used in the game.
