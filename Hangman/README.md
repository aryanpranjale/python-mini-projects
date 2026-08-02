# Hangman

A simple console-based Hangman game built in Python.

The game randomly selects a word from a CSV file based on the difficulty chosen by the player. Guess one letter at a time before you run out of lives!

## Features

- Random word selection from a CSV file
- Three difficulty levels:
  - Easy
  - Medium
  - Hard
- Input validation
  - Accepts only a single alphabetic character
  - Prevents duplicate guesses
- ASCII Hangman that updates after every wrong guess
- Win/Lose messages
- Displays:
  - Remaining lives
  - Guessed letters
  - Current progress of the word

## Project Structure

```
Hangman/
│── hangman.py
│── words.csv
└── README.md
```

## Requirements

- Python 3.x

No external libraries are required.

The project only uses Python's built-in modules:

- csv
- random
- pathlib

## How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/hangman.git
```

Go into the project folder:

```bash
cd hangman
```

Run the game:

```bash
python hangman.py
```

## CSV Format

The `words.csv` file should contain two columns:

```csv
word,difficulty
apple,easy
python,medium
xylophone,hard
```

## Future Improvements

Some ideas I'd like to add in the future:

- Play Again option
- Categories (Animals, Countries, Programming, etc.)
- Colored terminal output
- Hint system
- Score tracking
- Larger word database

## What I Learned

This project helped me practice:

- Functions
- Lists
- Loops
- Conditionals
- File handling
- Reading CSV files
- Error handling using `try` and `except`
- User input validation
- Organizing code into reusable functions

## Author

Aryan Pranjale
