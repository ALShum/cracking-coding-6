import unittest

from src import ch01_palindrome_permutation as testing_file


class TestPalindromePermutation(unittest.TestCase):
    def test_input_not_palindrom_return_false(self):
        result = testing_file.palindrome_permutation('hello')
        self.assertFalse(result)

    def test_input_even_palindrome_return_true(self):
        result = testing_file.palindrome_permutation('Tact Coa')
        self.assertTrue(result)

    def test_input_odd_palindrome_return_true(self):
        result = testing_file.palindrome_permutation('NONO')
        self.assertTrue(result)
