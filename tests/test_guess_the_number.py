# guess_the_number.py

import unittest
from unittest import mock
from io import StringIO

from guess_the_number import get_integer_input_in_range

class TestGetIntegerInputInRange(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input within the range
        with mock.patch('builtins.input', side_effect=['5']):
            result = get_integer_input_in_range("Enter a number", 1, 10)
            self.assertEqual(result, 5)

    def test_invalid_then_valid_input(self):
        # Test with invalid input (non-integer) and then a valid integer
        with mock.patch('builtins.input', side_effect=['invalid', '5']), \
            mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_integer_input_in_range("Enter a number", 1, 10)
            printed_output = mock_stdout.getvalue()
            self.assertIn("Invalid input. Please enter an integer.", printed_output)
            self.assertEqual(printed_output.count("Invalid input. Please enter an integer."), 1)
            self.assertEqual(result, 5)

    def test_greater_input(self):
        # Test with input out of the specified range (greater)
        with mock.patch('builtins.input', side_effect=['15', '6']), \
            mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_integer_input_in_range("Enter a number", 5, 10)
            printed_output = mock_stdout.getvalue()
            self.assertIn("Input must be between 5 and 10", printed_output)
            self.assertEqual(printed_output.count("Input must be between 5 and 10"), 1)
            self.assertEqual(result, 6)

    def test_smaller_input(self):
        # Test with input out of the specified range (smaller)
        with mock.patch('builtins.input', side_effect=['-2', '5']), \
            mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_integer_input_in_range("Enter a number", 1, 10)
            printed_output = mock_stdout.getvalue()
            self.assertIn("Input must be between 1 and 10", printed_output)
            self.assertEqual(printed_output.count("Input must be between 1 and 10"), 1)
            self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
