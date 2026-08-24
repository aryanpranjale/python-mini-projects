# Password Generator

A simple command-line password generator built with Python.

This project was created as a practice project to work with functions, loops, lists, input validation, exception handling, and Python's `random` module.

## Features

* Choose a password length between **8 and 24 characters**
* Press Enter to use the default password length of **8**
* Choose whether to include:

  * Lowercase letters
  * Uppercase letters
  * Numbers
  * Symbols
* Handles invalid user input without crashing
* Randomly generates each password character
* Converts the generated character list into a final password string

## How It Works

The program first creates lists containing:

* Lowercase alphabets (`a-z`)
* Uppercase alphabets (`A-Z`)
* Numbers (`0-9`)
* Common password symbols

The user then chooses the password length and which character types they want to include.

The selected character sets are combined into one list. The program randomly selects characters from this list until the requested password length is reached.

Finally, the generated characters are joined together to produce the password.

## Example

```text
Welcome to password generator

Enter password length (8–24):
Press Enter to use the default (8).
12

Do you want capital letters (Yes/y or No/n):
y

Do you want Numbers (Yes/y or No/n):
y

Do you want Symbols (Yes/y or No/n):
y

Your final password generated is:
a7@Kp2#xLm9$
```

## Concepts Practiced

This project helped practice:

* Functions
* `while` loops
* `for` loops
* Lists
* List comprehensions
* `random.choice()`
* `ord()`
* `chr()`
* String methods such as `strip()` and `lower()`
* `join()`
* `try/except`
* `ValueError`
* Conditional statements
* User input validation

## Future Improvements

Possible improvements for future versions:

* Allow the user to generate multiple passwords at once
* Allow the user to choose the exact number of letters, numbers, and symbols
* Guarantee at least one character from every selected character category
* Add an option to exclude confusing characters such as `0`, `O`, `1`, `l`, and `I`
* Add password strength checking

## Requirements

* Python 3.x

No external libraries are required.

## Running the Program

Run the Python file from a terminal:

```bash
python password_generator.py
```

## Author
 Built by Aryan as part of my Python learning journey.
