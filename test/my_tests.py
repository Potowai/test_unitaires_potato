import unittest
import os
from src.finder import is_pal

chaine = "kayak"


class MyTestCase(unittest.TestCase):

    def test_mirror(self):
        self.assertIn(chaine[::-1], is_pal(chaine))

    def test_palindrome(self):
        self.assertEqual(chaine[::-1] + os.linesep + "Bien dit!", is_pal(chaine))

if __name__ == '__main__':
    unittest.main()
