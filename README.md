# Nine-Men-s-Morris🎮
**Nine Men's Morris** is a strategic two-player board game brought to life in the command line! This version of the game is written in **Python**, follows a **layered architecture** for modularity and maintainability, and includes a **single-player mode** where you can play against a basic AI opponent.

## Game Overview 📜
Nine Men's Morris is a classic strategy game where two players (you and the computer) take turns placing and moving pieces on the board to form "mills" (rows of three pieces). Each time a player forms a mill, they can remove one of their opponent's pieces. The objective is to reduce your opponent to two pieces or block all their moves.

## Features ✨
- **Command Line Interface** (CLI) for an intuitive and simple game experience.
- **Single-player mode**: Play against a computer opponent.
    - The AI uses basic strategies to block your moves and create mills.
   
- **Layered Architecture**:
   - **Presentation Layer**: Handles the game interface and user interactions.
   - **Business Logic Layer**: Contains the core rules and mechanics of the game.
   - **Data Layer**: Manages the board state and player information.
