# Higher or Lower

## Description

A command-line Higher or Lower game written in Python. The program displays two choices and asks the player to guess which one has more followers. The player earns a point for every correct answer and the game continues until an incorrect answer is given.

## Features

* Randomly selects choices from a dataset
* Compares the follower counts of two choices
* Keeps track of the player's score
* Reuses the previous **B** choice as the new **A** choice after a correct answer
* Selects a new choice for **B** after every correct answer
* Prevents previously selected choices from appearing again
* Validates **A/B** user input
* Clears the terminal between rounds
* Allows the player to start another game after losing

## Concepts Used

* Lists
* Dictionaries
* Variables
* User Input
* Conditional Statements (`if`, `elif`, `else`)
* `while` Loops
* Functions
* `return` Statements
* Random Selection (`random.choice()`)
* f-Strings
* String Methods (`lower()`, `strip()`)
* List Membership
* Basic Program Flow
* Importing Data from Another Python File

## How to Run

```bash
python higher_lower.py
```

## Example

```text
Score: 0

Choice A: Cristiano Ronaldo, Footballer, from Portugal
VS
Choice B: Taylor Swift, Musician, from United States

Who has more followers A or B ?
a

Score: 1

Choice A: Taylor Swift, Musician, from United States
VS
Choice B: Lionel Messi, Footballer, from Argentina

Who has more followers A or B ?
b

Score: 2

...

Who has more followers A or B ?
a

Your score was 2

Do you want to play another round?
Enter Yes/Y to play, or enter any key to exit:
no

Thank you for playing!
```

## Game Logic

The game starts by randomly selecting two different choices as **A** and **B**.

If the player chooses correctly:

1. The score increases by 1.
2. The current **B** becomes the new **A**.
3. A new unused choice is selected as **B**.
4. The game continues.

Previously selected choices are stored in a list so that they cannot be selected again.

If the player chooses incorrectly, the game ends and the final score is displayed.

## Error Handling

The program checks for:

* Invalid **A/B** responses
* Repeated choices being selected
* Previously selected choices appearing again during the game

## Future Improvements

* Add a proper game-over screen
* Add ASCII art for the game title and choices
* Improve the terminal interface
* Add different difficulty levels
* Add a high-score system
* Add more data to the dataset
* Make the game cross-platform instead of using Windows-specific terminal commands
* Create a graphical user interface (GUI)

## What I Learned

This project helped me practice working with lists of dictionaries and using functions to organize a larger Python program. I also learned how to manage state throughout a game by keeping track of previously selected choices, scores, and the current A and B choices.

The project also helped me understand how to structure a game loop where one choice can become the next round's starting choice while a new choice is selected for comparison.

## Author

Built by Aryan as part of my Python learning journey.
