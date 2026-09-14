# Temperature Converter

## Description

A command-line temperature converter written in Python. The program allows users to convert temperatures between Celsius, Fahrenheit, and Kelvin using a simple menu-driven interface.

## Features

* Convert Celsius to Kelvin
* Convert Celsius to Fahrenheit
* Convert Kelvin to Celsius
* Convert Kelvin to Fahrenheit
* Convert Fahrenheit to Celsius
* Convert Fahrenheit to Kelvin
* Menu-driven interface
* Handles invalid menu selections by prompting the user again

## Concepts Used

* Functions
* While Loops
* Conditional Statements (`if`, `elif`, `else`)
* User Input
* Floating-Point Numbers (`float`)
* Variables
* Mathematical Expressions
* f-Strings

## How to Run

```bash
python temperature_converter.py
```

## Example

```text
Enter the Reading: 37

Choose the Desired Output

1. Celsius to Kelvin
2. Celsius to Fahrenheit
3. Kelvin to Celsius
4. Kelvin to Fahrenheit
5. Fahrenheit to Celsius
6. Fahrenheit to Kelvin

Enter the number associated with your desired change: 2

37.0°C converted into 98.6°F
```

## Current Limitations

* The program assumes the user enters valid numeric input for the temperature and menu choice.
* Input validation using `try` and `except` has not been implemented yet.

## Future Improvements

* Add input validation using `try` and `except`
* Format output to two decimal places
* Allow multiple conversions without restarting the program
* Organize each conversion into its own function
* Add support for additional temperature scales

## What I Learned

This project helped me practice building menu-driven programs, using loops for input validation, working with floating-point numbers, writing mathematical conversion formulas, and improving the readability of my code by storing calculations in variables before displaying the results.

## Author

Built by Aryan as part of my Python learning journey.
