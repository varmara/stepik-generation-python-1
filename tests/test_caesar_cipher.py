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

class TestGetLanguage(unittest.TestCase):
    # TODO: Test get_language (Unsupported language) 
    pass

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
        # Test encryption in Russian
        direction = 1
        language = 'ru'
        self.assertEqual(
            caesar("Умом Россию не понять!", direction, 32, 1, language), 
            "Фнпн Спттйя ож рпоауэ!"
            )
        self.assertEqual(
            caesar("Блажен, кто верует, тепло ему на свете!", direction, 32, 10, language), 
            "Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!"
            )
    
    def test_ru_decrypt(self):
        # Test decryption in Russian
        direction = -1
        language = 'ru'
        self.assertEqual(
            caesar("Фнпн Спттйя ож рпоауэ!", direction, 32, 1, language), 
            "Умом Россию не понять!"
            )
        self.assertEqual(
            caesar("Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!", direction, 32, 10, language), 
            "Блажен, кто верует, тепло ему на свете!"
            )
        self.assertEqual(
            caesar("Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.", direction, 32, 7, language), 
            "Скупой теряет все, желая все достать."
            )

    def test_en_encrypt(self):
        # Test encryption in English  
        direction = 1
        language = 'en'
        n_letters = 26
        self.assertEqual(
            caesar("avetruetocaesar", direction, n_letters, 1, language), 
            "bwfusvfupdbftbs"
            )
        self.assertEqual(
            caesar("@Rerrf, Ergrwe - Ffewewf", direction, n_letters, 14, language), 
            "@Fsfft, Sfufks - Ttskskt"
            )
        self.assertEqual(
            caesar("To be, or not to be, that is the question!", direction, n_letters, 17, language), 
            "Kf sv, fi efk kf sv, kyrk zj kyv hlvjkzfe!"
            )
        
    def test_en_decrypt(self):
        # Test decryption in English
        direction = -1
        language = 'en'
        n_letters = 26
        self.assertEqual(
            caesar("bwfusvfupdbftbs", direction, n_letters, 1, language), 
            "avetruetocaesar"
            )
        self.assertEqual(
            caesar("@Fsfft, Sfufks - Ttskskt", direction, n_letters, 14, language), 
            "@Rerrf, Ergrwe - Ffewewf"
            )
        self.assertEqual(
            caesar("Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.", direction, n_letters, 25, language), 
            "The grass is always greener on the other side of the fence."
            )
        self.assertEqual(
            caesar("Hawnj pk swhg xabkna ukq nqj.", direction, n_letters, 22, language), 
            "Learn to walk before you run."
            )

class TestCipher(unittest.TestCase):
    # TODO: Test cipher (a round of encryption/decryption)
    pass



if __name__ == '__main__':
    unittest.main()

