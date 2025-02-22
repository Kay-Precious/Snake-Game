# Snake-Game
A simple implementation of the classic Snake game using Python and the Turtle graphics library.

Table of Contents
- #features
- #requirements
- #installation
- #gameplay
- #code-structure
- #modules
- #classes
- #methods
- #future-development

Features
- Snake movement using arrow keys
- Food pellets appear randomly on the screen
- Scorekeeping and display
- Game over condition when snake collides with wall or itself

Requirements
- Python 3.x
- Turtle graphics library

Installation
1. Clone the repository using git clone
2. Navigate to the project directory
3. Run the game using python main.py

Gameplay
1. Use arrow keys to control the snake's movement
2. Eat food pellets to increase score and snake length
3. Avoid colliding with walls or the snake's own body

Code Structure
The game is implemented in multiple modules, each focusing on a specific functionality:

Modules
- snake.py: Snake movement and collision detection
- food.py: Food pellet creation and placement
- scoreboard.py: Scorekeeping and display

Classes
- Snake: Handles snake movement, collision detection, and growth
- Food: Handles food pellet creation and placement
- Score: Handles scorekeeping and display

Methods
- Snake: Checks for collisions with walls(if modifies) or itself and Updates snake position
- Food: Creates a new food pellet at a random location
- Scoreboard.update_score(): Updates the score display
- main: Game logic and main loop
- data.txt: keep record of current high score

Future Development
- High score leaderboard feature

