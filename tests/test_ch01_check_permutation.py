import unittest

from src import ch01_check_permutation as testing_file


class TestCheckPermutation(unittest.TestCase):
    def test_input_first_string_empty_returns_false(self):
        result = testing_file.check_permutation('', 'AA')
        self.assertFalse(result)

    def test_input_second_string_empty_returns_false(self):
        result = testing_file.check_permutation('AA', '')
        self.assertFalse(result)

    def test_input_not_permutation_returns_false(self):
        result = testing_file.check_permutation('ABCD', 'BCDE')
        self.assertFalse(result)

    def test_input_permutation_reverse_returns_true(self):
        result = testing_file.check_permutation('GOD', 'DOG')
        self.assertTrue(result)

    def test_input_permutation_not_sorted_returns_true(self):
        result = testing_file.check_permutation('AAGOD', 'ADAOG')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
