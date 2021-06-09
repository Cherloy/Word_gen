import unittest
from word_generation.word_gen.word_gen import random_string

class TestWord_gen(unittest.TestCase):
    def test_string_negative(self):
        self.assertEqual(random_string(-2),0)

    def test_string_pos(self):
        self.assertEqual(random_string(4096), 4096)
