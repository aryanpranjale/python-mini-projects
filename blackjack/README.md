# Blackjack Game

A simple command-line Blackjack game built in Python as part of my Python learning journey.

The project focuses on practicing Python fundamentals such as functions, loops, conditionals, lists, user input, random selection, and basic game logic.

## Features

- Start or exit the game from the command line
- Player receives two cards
- Dealer receives two cards, with one card initially hidden
- Player can choose to:
  - **Hit** — draw another card
  - **Stand** — end their turn
- Dealer automatically draws cards until reaching a score of 17 or higher
- Detects player and dealer busts
- Correctly handles:
  - Number cards (`2–10`)
  - Face cards (`J`, `Q`, `K`) as 10
  - Aces as either 1 or 11
- Determines the winner based on the final scores
- Supports multiple rounds

## How Blackjack Works

The goal is to get as close to **21** as possible without going over.

Card values:

| Card | Value |
|------|-------|
| 2–10 | Face value |
| J, Q, K | 10 |
| A | 1 or 11 |

The player gets to choose whether to **Hit** or **Stand**.

The dealer must keep drawing cards while their score is below 17.

## Example

Do you want to play a round of blackjack?
Enter Yes/Y to play, Else enter any key to exit:
y

Get ready to play
['8', 'A']
10

Hit or Stand
Enter Hit/H to hit and Stand/S to stand:
h

['8', 'A', '5']

Hit or Stand
Enter Hit/H to hit and Stand/S to stand:
s

['10', '7']
Your score was: 14
Dealers' score was : 17
Dealer wins!

##Future Improvements
 -Use a proper 52-card deck
 -Prevent the same physical card from being drawn more than once
 -Add suits: Hearts, Diamonds, Clubs, and Spades
 -Add ASCII card artwork
 -Add proper Blackjack detection
 -Improve the user interface
 -Add score/betting system

 What I Practiced

This project helped me practice:

##Functions
-while and for loops
-Lists
-List comprehensions
-if / elif / else
-try / except
-User input
-random.choice()
-Mutable lists
-Program state
-Breaking a problem into smaller functions
-Translating real-world rules into program logic

##Author

Aryan

Built as a learning project while learning Python.
