import unittest

from src import ch01_is_unique as testing_file


class TestIsUnique(unittest.TestCase):
    def test_input_empty_string_returns_false(self):
        result = testing_file.is_unique('')
        self.assertFalse(result)

    def test_input_repeated_characters_returns_false(self):
        result = testing_file.is_unique('AAABCD')
        self.assertFalse(result)

    def test_input_unique_numbers_returns_true(self):
        result = testing_file.is_unique('ABCD')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
