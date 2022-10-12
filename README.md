# Cycle
Cycle is a game similar to the TRON game. In it, the players try to cut each other 
off using cycles that leave a trail behind them. You play this game on a simulated 
terminal, with a textual interface.
---
## Rules
Cycle is played according to the following:

  Players can move up, down, left and right...
    Player one moves using the W, S, A and D keys.
    Player two moves using the I, K, J and L keys.
  Each player's trail grows as they move.
    Players try to maneuver so the opponent collides with their trail.
  If a player collides with their opponent's trail...
    A "game over" message is displayed in the middle of the screen.
    The cycles turn white.
    Players keep moving and turning, but the game has ended.
---
## Getting Started
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command:
```
py cycle      (Windows)
python3 cycle (Everything else)
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the __main__.py file inside the cycle folder and click the "run" icon.
---
## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cycle               (directory holding all source code for game)
  +-- game              (directory holding source code for all classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```
---
## Required Technologies
* Python 3.8.0
* Raylib Python CFFI 3.7
---
## Authors
Jerry Lane and the authors of Snake
