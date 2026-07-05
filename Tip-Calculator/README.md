# Tip Calculator

## Description

A command-line tip calculator written in Python. The program calculates the total bill after adding a user-specified tip and can optionally split the bill among multiple people.

## Features

* Calculate the total bill with a custom tip percentage
* Option to split the bill among multiple people
* Validates **YES/NO** user input
* Handles invalid numeric input
* Prevents division by zero when splitting the bill
* Displays each person's share rounded to two decimal places

## Concepts Used

* Variables
* User Input
* Conditional Statements (`if`, `elif`, `else`)
* `while` Loops
* Exception Handling (`try` / `except`)
* Floating-Point Numbers (`float`)
* Integer Input (`int`)
* f-Strings
* Basic Arithmetic

## How to Run

```bash
python tip_calculator.py
```

## Example

```text
Welcome to Tip Calculator!

Enter the Bill amount: 1200
Enter the tip percentage you want to give: 10

The bill after tipping 10.0% would be 1320.00

Do you want to split the bill? YES/NO
yes

Enter the number of people you would like to split with:
4

Each person would pay 330.00

Thank you for using, Hope you have a great day :)
```

## Error Handling

The program checks for:

* Invalid **YES/NO** responses
* Non-numeric input when entering the number of people
* Division by zero when the user enters **0** people

## Future Improvements

* Validate bill amount and tip percentage
* Allow the user to calculate another bill without restarting the program
* Support different currencies
* Save previous calculations
* Create a graphical user interface (GUI)

## What I Learned

This project helped me practice building interactive command-line programs using loops, conditional statements, and exception handling. It also improved my understanding of program flow by separating different user inputs into individual loops for better control and readability.

## Author

Built by Aryan as part of my Python learning journey.
