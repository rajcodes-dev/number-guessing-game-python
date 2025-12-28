# Number Guessing Game 

A robust, interactive command-line interface (CLI) game built with Python. This project demonstrates core programming fundamentals including state management, input validation, and control flow.

## Overview

The computer generates a random number between **1 and 100**. The player attempts to guess the number and receives real-time feedback ("Too high" or "Too low") until the correct number is found. The game tracks attempts and offers a replay option upon completion.

## Features

* **Randomized Gameplay:** Uses Python’s `random` module for unpredictable outcomes.
* **Input Validation:** Robust error handling ensures only integers between 1-100 are processed.
* **Interactive Feedback:** Provides hints (Too High/Too Low) to guide the user.
* **Replay Loop:** Allows users to start a new game immediately without restarting the script.
* **Attempt Counter:** Tracks and displays the total number of guesses used.

## Key Concepts

This project was built to practice and demonstrate:
* **Control Flow:** `if`, `elif`, `else` logic.
* **Loops:** `while` loops and nested structures for game state.
* **Input Handling:** Capturing and sanitizing user inputs.
* **Modules:** Implementing the standard `random` library.

## Getting Started

### Prerequisites
* Python 3.x installed on your system.

### Installation & Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rajcodes-dev/number-guessing-game-python
   cd number-guessing-game
   ```

2. **Run the script:**
   ```bash
   python number_guessing_game.py
   ```
   
3. **Output:**
   ```console
   -----Welcome to 'Guess the number' game.-----

    Guess the number: 45
    Too low!, Guess high
    
    Guess the number: 72
    Too high!, Guess low
    
    Guess the number: 60
    Hooray! You guessed the correct number.
    You guessed the number in 3 attempts.
   ```
   
## Future Improvements:
   * Add difficulty levels (Easy/Medium/Hard)
   * Implement a high-score / scoring system
   * Refactor code into modular functions
   * Create an Object-Oriented Programming (OOP) version
   * Add a "limited attempts" mode

## Author:
   * **Raj Tiwari** Beginner Python Programmer | Building real-world projects to master clean coding practices.
     
