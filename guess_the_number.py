# -*- coding: utf-8 -*-
# guess_the_number.py
"""
Guess the Number Game

Project from the 'Generation Python' course for beginners

Project Description: The program generates a random number
and asks the user to guess it. The user can specify a range in which to guess 
the number.

If the user's guess is greater than the random number, 
the program displays the message 'Your number is greater than mine,
try again'. If the guess is less than the random number, the program
displays the message 'Your number is less than mine, try again'.
If the user guesses the number, the program congratulates them and displays
the message 'Correct, congratulations!'

Change log

- Add the ability to specify the left and right boundary 
for random number selection (from 1 to n<100)."
- Add the ability to generate a new number (play again),
after the user has guessed the number.

TODO: 
- Add counting attempts made by the user. When the number is guessed,
the program shows the number of attempts (total, valid, invalid).
"""

import random

def get_integer_input_in_range(prompt: str, lower: int, upper: int) -> int:
    """Gets user input as an integer within a given range.

    Args:
        prompt (str): The prompt to display to the user.
        lower (int): The lower bound of the range.
        upper (int): The upper bound of the range.
    
    Returns:
        int: An integer within the given range.
    """
    user_input = None
    while user_input is None or not lower <= user_input <= upper:
        try:
            user_input = int(input(prompt + f" from {lower} to {upper}: "))
            if not lower <= user_input <= upper:
                print(f"Input must be between {lower} and {upper}")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return user_input

def user_confirms(prompt: str) -> bool:
    """Asks the user a yes/no question and returns a Boolean value.

    Args:
        prompt (str): A question to ask.

    Returns:
        bool: True if the user says 'yes' or 'y', False if 'no' or 'n'.
    """
    valid_responses = {'yes', 'y', 'no', 'n'}
    response = None
    while response is None or response not in valid_responses:
        response = input(prompt + " (yes, no): ").strip().lower()
    if response in {'yes', 'y'}:
        return True
    else:
        return False

def hint(guess: int, n: int) -> str:
    """Hints the user if their number is less than, 
    greater than or equals to the generated one.

    Args:
        guess (int): The user guess.
        n (int): The generated number.

    Returns:
        str: A hint indicating if the user's number is less than, 
    greater than or equals to the generated one.
    """
    if guess < n:
        return f"{guess} is less than my number"
    elif guess > n:
        return f"{guess} is greater than my number"
    else:
        return f"{guess} equals my number"

def play_game():
    """This function allows a player to guess a randomly generated number 
    within a specified range.

    The function prompts the user to enter the boundaries of the number 
    range and generates a random number within that range. It then repeatedly 
    prompts the user to guess the generated number and provides hints until 
    the user correctly guesses the number.

    Args:
        None
    """
    print("Enter the range in which you want to generate the number")
    left = get_integer_input_in_range("Left boundary", 1, 100)
    right = get_integer_input_in_range("Right boundary", left, 100)
    print(f"Guess the number from {left} to {right}")
    n = random.randint(left, right)
    guess = None
    while guess != n:
        guess = get_integer_input_in_range("Your number", left, right)
        print(hint(guess, n))
    print("Congratulations!")

def main():
    """Starts the Guess the Number Game.

    This function welcomes the player, then repeatedly plays the game 
    until the player chooses to quit.

    Args:
        None
    """
    print("\nWelcome to the Guess the Number Game\n")
    while True:
        play_game()
        if not user_confirms("Would you like to play again?"):
            print("\nThank you for playing the Guess the Number Game. See you again...\n")
            break

if __name__ == "__main__":
    main()
