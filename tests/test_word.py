import unittest
import pathlib as pl
from word_generation.word_gen.word_gen import Word

class TestWord_gen(unittest.TestCase):
    def test_string_negative(self):
        self.assertEqual(Word.random_string(-2), 0)

    def test_random_drawing(self):
        Word.random_drawing('circle''rectangle''ellipse''line')
        path = pl.Path("test.docx")
        self.assertTrue(path.is_file())

    def test_get_table(self):
        Word.get_table()
        path = pl.Path("test1.docx")
        self.assertTrue(path.is_file())

    def test_merge(self):
        path = pl.Path("result.docx")
        Word.merge(path)
        self.assertTrue(path.is_file())

    def test_trash_clean(self):
        path = pl.Path("test.txt")
        Word.trash_clean()
        self.assertFalse(path.is_file())