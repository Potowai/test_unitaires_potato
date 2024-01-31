import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_val = True
        self.assertEqual(True, my_val)  # add assertion here


if __name__ == '__main__':
    unittest.main()
