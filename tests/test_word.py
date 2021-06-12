import unittest
from word_generation.word_gen.word_gen import Word

class TestWord_gen(unittest.TestCase):
    def test_string_negative(self):
        self.assertEqual(Word.random_string(self, -2),0)

    def test_string_pos(self):
        self.assertEqual(Word.random_string(self, 4096), 4096)
