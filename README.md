Hangman Game

This is a simple Hangman game implemented in Python.  
The goal is to guess a hidden word one letter at a time within a limited number of attempts.  
If the word is guessed before attempts run out, the player wins. Otherwise, the word is revealed and the game ends.

Features

- Random word selection from a predefined list
- Guess one letter at a time
- Live display of guessed letters and blanks
- Tracks incorrect guesses and remaining attempts
- Win or lose notification

Prerequisites

- Python 3.x installed on your machine

How to Run the Game

Clone the Repository:
git clone https://github.com/charan2228/hangmangame

Navigate to the Game Directory:
cd hangmangame

Run the Script:
python hangman.py

How to Play

1. A word is randomly chosen.
2. You will see underscores (_) for each unguessed letter.
3. Type a letter and press Enter.
   - If correct, it's revealed in the word.
   - If incorrect, one attempt is lost.
4. Continue guessing until:
   - You guess the word correctly (win)
   - You run out of attempts (lose)

Sample Gameplay

Welcome to Hangman!
You have 6 attempts remaining.
_ _ _ _ _ _

Guess a letter: e
Incorrect! You have 5 attempts remaining.
_ _ _ _ _ _

Guess a letter: o
Correct!
_ o _ _ _ _

Author

charan2228 (https://github.com/charan2228)


