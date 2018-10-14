import unittest

from src import ch01_urlify as testing_file


class TestUrlify(unittest.TestCase):
    def test_input_exceed_string_space_with_length_returns_url_or_error_msg(
        self
    ):
        result = testing_file.urlify('Mr John Smith  ', 13)
        self.assertEqual(result, 'Mr%20John%20Smith')

        result = testing_file.urlify_solution('Mr John Smith  ', 13)
        self.assertEqual(result, 'String is too short for output')

    def test_input_exceed_string_text_with_length_returns_url_or_error_msg(
        self
    ):
        result = testing_file.urlify('Mr John Smithhh  ', 13)
        self.assertEqual(result, 'Mr%20John%20Smith')

        result = testing_file.urlify_solution('Mr John Smithhh  ', 13)
        self.assertEqual(result, 'String is too short for output')

    def test_input_fit_string_with_length_returns_url_string(self):
        result = testing_file.urlify('Mr John Smith', 13)
        self.assertEqual(result, 'Mr%20John%20Smith')

        result = testing_file.urlify_solution('Mr John Smith', 13)
        self.assertEqual(result, 'Mr%20John%20Smith')

    def test_input_fit_string_with_length_returns_url_or_error_msg(self):
        result = testing_file.urlify('Mr John Smith', 13)
        self.assertEqual(result, 'Mr%20John%20Smith')

        result = testing_file.urlify_solution('Mr John Smith', 13)
        self.assertEqual(result, 'String is too short for output')

    def test_input_empty_string_with_length_returns_empty_string(self):
        result = testing_file.urlify('', 0)
        self.assertEqual(result, '')

        result = testing_file.urlify_solution('', 0)
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
