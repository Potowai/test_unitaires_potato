import unittest
from src.finder import is_pal

chaine = "random"


class MyTestCase(unittest.TestCase):

    def test_mirror(self):
        self.assertEqual(chaine[::-1], is_pal(chaine))


if __name__ == '__main__':
    unittest.main()
