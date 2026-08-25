# Number Guessing Game 🎯

A simple command-line Number Guessing Game built in Python.

The player chooses a difficulty level, and the program randomly selects a number within the corresponding range. The player then keeps guessing until they find the correct number.

## 🎮 Features

* Three difficulty levels:

  * **Easy:** Number between 1 and 10
  * **Medium:** Number between 1 and 100
  * **Hard:** Number between 1 and 1000
* Accepts difficulty using either the number or name.
* Gives hints after every incorrect guess:

  * Tells the player if the target number is higher.
  * Tells the player if the target number is lower.
* Keeps track of the number of tries.
* Prevents the same number from being counted twice.
* Handles invalid non-numeric input.
* Allows the player to start another round after winning.
* Displays the previous guesses and whether they were too high or too low.

## 🧠 How It Works

1. The player selects a difficulty.
2. The program generates a random number based on the selected difficulty.
3. The player enters a guess.
4. The program compares the guess with the randomly generated number.
5. If the guess is incorrect, the player receives a higher/lower hint.
6. Repeated guesses are rejected without increasing the number of tries.
7. The game continues until the player guesses the correct number.
8. The player can choose to play another round.

## 🛠️ Concepts Used

This project was built using basic Python concepts, including:

* Functions
* `while` loops
* `if / elif / else` statements
* Lists
* User input
* Type conversion
* Exception handling with `try / except`
* The `random` module
* Function arguments and return values
* String methods such as `.strip()` and `.lower()`

## ▶️ How to Run

Make sure Python is installed on your system.

Run the program from the terminal:

```bash
python number_guessing_game.py
```

Then follow the instructions displayed in the terminal.

## 📌 Future Improvements

Possible improvements for future versions:

* Add a limited number of attempts based on difficulty.
* Add a scoring system.
* Separate the comparison logic into its own function.
* Improve the display of previous guesses.
* Add more difficulty levels.
* Add statistics across multiple rounds.

## 📚 About the Project

This project was created as a Python practice project to work with functions, loops, conditional logic, lists, random number generation, and input validation.

The goal was to build the game independently and practice applying concepts from previous Python projects to a new problem.

## Author
Built by Aryan as part of my Python learning journey.
