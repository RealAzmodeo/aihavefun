import unittest
from main import get_random_joke

class TestMain(unittest.TestCase):
    def test_get_random_joke(self):
        joke = get_random_joke()
        self.assertIsInstance(joke, str)

if __name__ == "__main__":
    unittest.main()
