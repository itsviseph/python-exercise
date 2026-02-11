import unittest
from analyzer import word_count, unique_word_count, most_common_word


class TestAnalyzer(unittest.TestCase):

    def test_word_count_basic(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_word_count_empty(self):
        self.assertEqual(word_count(""), 0)

    def test_word_count_extra_spaces(self):
        self.assertEqual(word_count("  hello   world  "), 2)

    def test_unique_word_count(self):
        self.assertEqual(unique_word_count("hello hello world"), 2)

    def test_most_common_word(self):
        self.assertEqual(most_common_word("apple banana apple"), ("apple", 2))

    def test_most_common_word_empty(self):
        self.assertIsNone(most_common_word(""))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            word_count(123)


if __name__ == "__main__":
    unittest.main()
