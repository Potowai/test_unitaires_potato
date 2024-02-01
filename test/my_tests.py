import unittest
import os

from src.langs import English
from utilities.pal_finder import build

chaine = "kayak"


class MyTestCase(unittest.TestCase):

    def test_mirror(self):
        self.assertIn(chaine[::-1], build(chaine=chaine))

    def test_palindrome(self):
        self.assertIn(chaine[::-1] + os.linesep + "FINE", build(chaine=chaine))

    def test_hello(self):
        self.assertIn("HI" + os.linesep + chaine, build(chaine=chaine))

    def test_bye(self):
        self.assertIn("ESC", build(chaine=chaine))

    def test_palindrome_en(self):
        self.assertIn(chaine[::-1] + os.linesep + "Well sayed!", build(chaine, English))

    def test_palindrome_en_hello(self):
        self.assertIn("Hello" + os.linesep + chaine, build(chaine, English))

    def test_bye_multiple_langs(self):
        with self.subTest(chaine):
            self.assertIn("ESC", build(chaine=chaine))
            self.assertIn("Bye bye!", build(chaine, English))


if __name__ == '__main__':
    unittest.main()
