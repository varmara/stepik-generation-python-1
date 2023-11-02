# caesar_cipher.py

import unittest
from unittest import mock
from io import StringIO

from caesar_cipher import caesar_shift, get_direction, caesar, is_in_language

class TestCaesarShift(unittest.TestCase):
    def test_encrypt(self):
        # Test encryption
        self.assertEqual(caesar_shift(0, 1, 3, 26), 3)    # 'a' -> 'd'
        self.assertEqual(caesar_shift(12, 1, 5, 26), 17)  # 'm' -> 'r'
        self.assertEqual(caesar_shift(25, 1, 1, 26), 0)   # 'z' -> 'a'

    def test_decrypt(self):
        # Test decryption
        self.assertEqual(caesar_shift(3, -1, 3, 26), 0)    # 'd' -> 'a'
        self.assertEqual(caesar_shift(17, -1, 5, 26), 12)  # 'r' -> 'm'
        self.assertEqual(caesar_shift(0, -1, 1, 26), 25)   # 'a' -> 'z'
    
class TestGetDirection(unittest.TestCase):
    def test_valid_input_encrypt(self):
        with mock.patch('builtins.input', side_effect=['encrypt']):
            result = get_direction()
            self.assertEqual(result, 1)

    def test_valid_input_decrypt(self):
        with mock.patch('builtins.input', side_effect=['decrypt']):
            result = get_direction()
            self.assertEqual(result, -1)

    def test_valid_input_case_insensitivity(self):
        with mock.patch('builtins.input',
                        side_effect=['Encrypt', 'ENCRYPT', 'EnCrYpT', 
                                     'Decrypt', 'DECRYPT', 'DeCrYpt']):
            results = [get_direction() for _ in range(6)]
            self.assertEqual(results, [1, 1, 1, -1, -1, -1])

    def test_invalid_input2_encrypt(self):
        with mock.patch('builtins.input', side_effect=['invalid', 'just encrypt', 'encrypt']), \
            mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_direction()
            printed_output = mock_stdout.getvalue()
            self.assertIn("Invalid direction. Please try again.", printed_output)
            self.assertEqual(printed_output.count("Invalid direction. Please try again."), 2)
            self.assertEqual(result, 1)

    def test_invalid_input2_decrypt(self):
        with mock.patch('builtins.input', side_effect=['invalid', 'just decrypt', 'decrypt']), \
            mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_direction()
            printed_output = mock_stdout.getvalue()
            self.assertIn("Invalid direction. Please try again.", printed_output)
            self.assertEqual(printed_output.count("Invalid direction. Please try again."), 2)
            self.assertEqual(result, -1)

class TestIsInLanguage(unittest.TestCase):
    def test_in_russian(self):
        self.assertEqual(is_in_language(ord('а'), 'ru'), True)
        self.assertEqual(is_in_language(ord('я'), 'ru'), True)
        self.assertEqual(is_in_language(ord('А'), 'ru'), True)
        self.assertEqual(is_in_language(ord('Я'), 'ru'), True)
    
    def test_in_english(self):
        self.assertEqual(is_in_language(ord('a'), 'en'), True)
        self.assertEqual(is_in_language(ord('z'), 'en'), True)
        self.assertEqual(is_in_language(ord('A'), 'en'), True)
        self.assertEqual(is_in_language(ord('Z'), 'en'), True)

    def test_not_in_russian(self):
        self.assertEqual(is_in_language(ord('a'), 'ru'), False)
        self.assertEqual(is_in_language(ord('z'), 'ru'), False)
        self.assertEqual(is_in_language(ord('A'), 'ru'), False)
        self.assertEqual(is_in_language(ord('Z'), 'ru'), False)
    
    def test_not_in_english(self):
        self.assertEqual(is_in_language(ord('а'), 'en'), False)
        self.assertEqual(is_in_language(ord('я'), 'en'), False)
        self.assertEqual(is_in_language(ord('А'), 'en'), False)
        self.assertEqual(is_in_language(ord('Я'), 'en'), False)

class TestCaesar(unittest.TestCase):
    def test_ru_encrypt(self):
        # Test encryption caesar(text, direction, n_letters, shift, language)
        self.assertEqual(
            caesar("Умом Россию не понять!", 1, 32, 1, 'ru'), 
            "Фнпн Спттйя ож рпоауэ!"
            )
    
    def test_ru_decrypt(self):
        # Test encryption caesar(text, direction, n_letters, shift, language)
        self.assertEqual(
            caesar("Фнпн Спттйя ож рпоауэ!", -1, 32, 1, 'ru'), 
            "Умом Россию не понять!"
            )

if __name__ == '__main__':
    unittest.main()
