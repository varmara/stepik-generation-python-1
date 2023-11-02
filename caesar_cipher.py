# -*- coding: utf-8 -*-
# caesar_cipher.py
"""
Caesar Cipher Encryption and Decryption

Project Description

This Python program uses the Caesar cipher to encrypt and decrypt text.
After finishing the task, asks the user if they want to use the program again.

The program will prompt the user for the following information:

Direction: 'encrypt' or 'decrypt'
Language:  'ru' for Russian or 'en' for English
Shift:     The number of positions to shift the letters
Text:      Text to encrypt/decrypt

Russian alphabet assumed to have 32 letters (ё is replaced with е).
Non-alphabetic characters (punctuation, spaces, numbers) remain unchanged. 
Letter case is preserved.
"""

from guess_the_number import get_integer_input_in_range, user_confirms

def caesar_shift(i: int, direction: int, shift: int, n_letters: int) -> int:
    """
    Encrypts or decrypts a character using the Caesar cipher.

    Args:
        i (int): The character to encrypt or decrypt.
        direction (int): The direction of the cipher (1 for encrypt, -1 for decrypt).
        shift (int): The number of positions to shift the character.
        n_letters (int): The number of letters in the alphabet.

    Returns:
        The encrypted or decrypted character.
    """
    return (i + direction * shift) % n_letters

def get_direction() -> int:
    """
    Prompts the user to choose an encoding direction (encrypt or decrypt).
    Returns an integer representing the chosen direction,
    either 1 for encrypt or -1 for decrypt.

    Returns:
        An integer representing the chosen encoding direction.

    Example usage:
        get_direction()
    """
    allowed_directions = {"e": 1, "encrypt": 1, "d": -1, "decrypt": -1}
    while True:
        direction = input("Choose encoding direction (encrypt, decrypt): ").lower()
        try:
            return allowed_directions[direction]
        except KeyError:
            print("Invalid direction. Please try again.")

def get_language(codes: dict):
    """Prompts the user to enter a language
    and return s the two-letter language code.

    Returns: 
        The two-letter language code
    """
    language = input("Enter a two-letter language code (en, ru): ").lower()
    if language not in codes:
        print("Unsupported language.")
        return None
    else:
        return (language)

def is_in_language(letter_ord: int, language: str) -> bool:
    """Checks if the alphabetic character order number belongs 
    to the specified language.

    Args:
        letter_ord (int): A character order number.
        language (str): A two-letter language code (e.g., 'en' or 'ru').

    Returns:
        True if the alphabetic character order number belongs
        to the specified language, False otherwise.
    """
    if language == 'en':
        return ord('a') <= letter_ord <= ord('z') \
            or ord('A') <= letter_ord <= ord('Z')
    elif language == 'ru':
        return ord('а') <= letter_ord <= ord('я') \
          or ord('А') <= letter_ord <= ord('Я')
    return False

def caesar(text, direction, n_letters, shift, language):
    """Perform Caesar Cipher Encryption and Decryption.

    This function encrypts or decrypts the input text using the Caesar 
    cipher algorithm and returns the result.

    Args:
        text (str): The text to encrypt or decrypt.
        direction (int): The encryption/decryption direction (1 - encrypt, -1 - decrypt).
        n_letters (int): The number of letters in the alphabet for the specified language.
        shift (int): The number of positions to shift the letters.
        language (str): The language (ru for Russian or en for English).

    Returns:
        str: The encrypted or decrypted text.

    Note:
    - For Russian language (ru), the letter 'ё' is replaced with 'е'.
    - Non-alphabetic characters (punctuation, spaces, numbers) are not changed.
    - The case of the letters is preserved.
    """
    base_ord = (ord('a'), ord('A')) if language == 'en' else (ord('а'), ord('А')) 
    output = ''
    for character in text:
      if character.isalpha():
        ch_ord = ord(character)
        if is_in_language(ch_ord, language):
          base = base_ord[0] if character.islower() else base_ord[1]
          ch_ord -= base
          i = caesar_shift(ch_ord, direction, shift, n_letters)
          output += chr(i + base)
        else:
           print("Invalid text:")
           return None
      else:
         output += character
    return output

def cipher():
    """Perform Encryption or Decryption.

    This function interactively prompts the user to input programs parameters:
    - choose between Caesar cipher encryption or decryption
    - choose the language
    - input a shift value
    - provide a text to be encrypted or decrypted
    Than it calls the Caesar cipher algorithm to process the input text 
    and prints the result.

    Args:
        None

    Returns:
        None
    """
    language_codes = {'en': 26, 'ru': 32}
    direction = get_direction() 
    language = get_language(language_codes)
    n_letters = language_codes[language]
    shift = get_integer_input_in_range("Enter shift", 1, n_letters - 1)
    text = input("Enter text: ")
    if language == 'ru':
       text = text.replace('Ё', 'Е').replace('ё', 'е')
    print(caesar(text, direction, n_letters, shift, language))
    return None

def main():
    """Entry point for the Ceasar Cipher.

    This function repeatedly prompts the user to encrypt or decrypt text 
    using the Ceasar Cipher. It continues running until the user chooses to exit.

    Args:
        None
    """
    print('\nWelcome to the Ceasar Cipher\n')
    while True:
        cipher()
        if not user_confirms("Would you like to cipher/decipher something else?"):
            print('\nThank you for using the Ceasar Cipher. See you again...\n')
            break

if __name__ == "__main__":
    main()
