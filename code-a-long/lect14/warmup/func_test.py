import unittest
from warmup_lect14 import firstlastword


class SwapWordsTests(unittest.TestCase):
    def test_regular_sentence(self):
        input_sentence = "Hello world"
        expected_output = "world Hello"
        actual_output = firstlastword(input_sentence)
        self.assertEqual(expected_output, actual_output)
        # assert(expected_output == actual_output)

    def test_one_word(self):
        input_word = "Hello"
        expected_output = "Hello"
        actual_output = firstlastword(input_word)
        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
