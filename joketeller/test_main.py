import unittest
from unittest.mock import patch
from main import get_random_joke

class TestMain(unittest.TestCase):
    @patch('main.requests.get')
    def test_get_random_joke(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {
            "setup": "What do you call a bear with no teeth?",
            "punchline": "A gummy bear!"
        }
        mock_get.return_value = mock_response

        joke = get_random_joke()
        self.assertEqual(joke, "What do you call a bear with no teeth? - A gummy bear!")

if __name__ == "__main__":
    unittest.main()
