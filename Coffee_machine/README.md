# Coffee Machine

## Description

A command-line Coffee Machine simulation written in Python. The program allows users to select coffee, checks ingredient availability, processes payments using coins, and updates the machine's resources and sales report.

## Features

- Allows users to select different types of coffee
- Checks ingredient availability before processing orders
- Accepts payments using quarters, dimes, nickels, and pennies
- Calculates payment and returns change
- Handles insufficient payments
- Tracks remaining ingredients and coffee sales
- Displays machine statistics using the `Report` command
- Shuts down the machine using the `Off` command
- Validates user input and coin quantities

## Concepts Used

- Lists and Dictionaries
- Functions
- `while` and `for` Loops
- Conditional Statements
- Generator Expressions
- `next()` and `any()` Functions
- Dictionary Methods (`.keys()`, `.items()`)
- Exception Handling (`try`, `except`)
- String Methods
- f-Strings
- Importing Data from Another Python File

## How to Run

python main.py

## Game Logic

The machine displays available coffee choices and waits for the user to select a drink.

1. Checks whether enough ingredients are available.
2. Accepts coins and calculates the payment.
3. Requests additional payment if the amount is insufficient.
4. Returns change if the user overpays.
5. Deducts ingredients after a successful transaction.
6. Updates the sales count and total money earned.

The machine also supports `Report` and `Off` commands.

## Error Handling

The program checks for:

- Invalid coffee selections
- Insufficient ingredients
- Insufficient payment
- Negative coin quantities
- Invalid numerical inputs

## Future Improvements

- Track physical coin inventory
- Calculate change using available coins
- Handle situations where exact change is unavailable
- Improve the terminal interface
- Add a graphical user interface (GUI)

## What I Learned

This project helped me practice working with dictionaries, functions, loops, and generator expressions. I also learned how to manage program state, validate user input, handle transactions, and organize a larger Python program into smaller functions.

## Author

Built by Aryan as part of my Python learning journey.
