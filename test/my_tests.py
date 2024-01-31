import unittest
import os

from src.langs import English, Francais
from src.finder import is_pal

chaine = "kayak"


class MyTestCase(unittest.TestCase):

    def test_mirror(self):
        self.assertIn(chaine[::-1], is_pal(chaine))

    def test_palindrome(self):
        self.assertIn(chaine[::-1] + os.linesep + "Bien dit!", is_pal(chaine))

    def test_hello(self):
        self.assertIn("Bonjour" + os.linesep + chaine, is_pal(chaine))

    def test_bye(self):
        self.assertIn("Au revoir!", is_pal(chaine))

    def test_palindrome_en(self):
        self.assertIn(chaine[::-1] + os.linesep + "Well sayed!", is_pal(chaine, English))

    def test_palindrome_en_hello(self):
        self.assertIn("Hello" + os.linesep + chaine, is_pal(chaine, English))

    def test_bye_multiple_langs(self):
        with self.subTest(chaine):
            self.assertIn("Au revoir!", is_pal(chaine))
            self.assertIn("Bye bye!", is_pal(chaine, English))


if __name__ == '__main__':
    unittest.main()
