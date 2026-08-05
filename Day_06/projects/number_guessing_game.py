"""

Project 1: Number Guessing Game ⭐ (Main Project)
Objective

Create a game where the user keeps guessing a secret number until the correct guess is entered.

Concepts Used
while loop
if-elif-else
break
User input
Iteration

Functional Requirements
Store a secret number in a variable.
Ask the user to guess the number.

If the guess is too small, display:

Too Low!

If the guess is too large, display:

Too High!
If the guess is correct:
Display a success message.
Stop the loop using break.
Count the number of attempts.
Display the total attempts after the correct guess.

Challenge (Optional):

Give the user only 5 attempts.
Display Game Over if all attempts are used.

"""

secret_number = 101
attempts = 0
while attempts < 5:
    guess_num = int(input("Guess The Secret Number : "))
    attempts += 1
    if guess_num < secret_number:
        print("Too Low!")
    elif guess_num > secret_number:
        print("Too High!")
    else:
        print("Congratulations!You guessed the secret number.")
        break
else:
    print("Game Over All Attempts Are Used!!")
