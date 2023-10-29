# -*- coding: utf-8 -*-
# guess_the_number.py
"""
Number Guesser

Project from the "Generation Python" course for beginners

Project Description: The program generates a random number from 1 to 100
and asks the user to guess it.

If the user's guess is greater than the random number, 
the program displays the message 'Your number is greater than mine,
try again'. If the guess is less than the random number, the program
displays the message 'Your number is less than mine, try again'.
If the user guesses the number, the program congratulates them and displays
the message 'Correct, congratulations!'

Change log

- Added counting attempts made by the user. When the number is guessed,
the program shows the number of attempts (total, valid, invalid).
- Added the ability to specify the right boundary for random number selection
(from 1 to n).
- Added the ability to generate a new number (play again),
after the user has guessed the number.

"""

import random

def is_valid_integer_in_range(value, lower, upper):
    try:
        int_value = int(value)
        return lower <= int_value <= upper
    except ValueError:
        return False

def get_boundaries():
    print('\nEnter the boundaries of the number range the program will generate')
    while True:
        left = input('Left boundary (number from 1 to 100): ')
        if is_valid_integer_in_range(left, 1, 100):
            left = int(left)
            break
        else:
            print('Enter an integer from 1 to 100')

    while True:
        right = input(f'Right boundary (from {left} to 100): ')
        if is_valid_integer_in_range(right, left, 100):
            right = int(right)
            return left, right
        else:
            print(f'Enter an integer from {left} to 100')

def get_user_guess(left, right):
    count_invalid = 0
    while True:
        value = input(f'\nEnter a number from {left} to {right}: ')
        if is_valid_integer_in_range(value, left, right):
            return int(value), int(count_invalid)
        else:
            count_invalid += 1
            print(f'Enter an integer from {left} to {right}')

def play_game(left, right):
    n = random.randint(left, right)
    count_valid_attempts = 0
    count_invalid_attempts = 0
    print(f'\nGuess the number from {left} to {right}')
    while True:
        value, invalid_attempts = get_user_guess(left, right)
        count_invalid_attempts += invalid_attempts
        if value == n:
            count_valid_attempts += 1
            print('Correct, congratulations!')
            print(f'\nTotal attempts {count_valid_attempts + count_invalid_attempts}',
                  f', valid - {count_valid_attempts}, ', 
                  f'invalid - {count_invalid_attempts}')
            break
        elif value < n:
            print('Your number is less than mine, try again')
            count_valid_attempts += 1
        elif value > n:
            print('Your number is greater than mine, try again')
            count_valid_attempts += 1

def play_again():
    while True:
        response = input('Would you like to play again? (yes, no, quit): ').strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n', 'quit', 'q']:
            return False
        else:
            print('Please enter either "yes", "no" or "quit".')

def main():
    print('\nWelcome to the Number Guesser\n')
    while True:
        left, right = get_boundaries()
        play_game(left, right) 
        if not play_again():
            print('\nThank you for playing the number guesser. See you again...')
            break

if __name__ == "__main__":
    main()
