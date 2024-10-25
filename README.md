
# Snake Game

This project is a classic **Snake Game** developed using Python's **Turtle Graphics**. The objective is to control the snake using the arrow keys, eat the food, and grow the snake without hitting the walls or itself. This game includes score tracking and displays a game-over message when the player loses.

## Features

- **Simple controls**: Use the arrow keys to move the snake.
- **Growing Snake**: Each time the snake eats food, it grows in length.
- **Score Tracking**: The score increases with each piece of food eaten.
- **Collision Detection**: The game ends if the snake hits a wall or itself.

## Gameplay

- **Start the Game**: Run the game script to start.
- **Controls**: Use the `Up`, `Down`, `Left`, and `Right` arrow keys to move the snake.
- **Objective**: Guide the snake to eat as much food as possible without colliding with the walls or its own body.
- **End Condition**: The game ends if the snake hits the walls or itself. A "Game Over" message will display on the screen.

## Getting Started

### Prerequisites
- Python 3.x
- `turtle` module (included with Python's standard library)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mukulmw/Snake_Game.git
   cd Snake_Game
   ```

2. **Run the game**:
   ```bash
   python main.py
   ```

## Code Structure

- **`main.py`**: The main script that initializes the game, updates the screen, and manages game conditions.
- **`snake.py`**: Contains the `Snake` class, which manages the snake's movement, growth, and direction changes.
- **`food.py`**: Contains the `Food` class, which randomly places food on the screen when eaten.
- **`scoreboard.py`**: Contains the `Scoreboard` class, which tracks and displays the player’s score and displays the game-over message.


---

Feel free to add more sections, such as **Known Issues** or **Future Enhancements** if you have plans for further development!