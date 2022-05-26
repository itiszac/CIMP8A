from unittest.mock import patch
from unittest import TestCase, main

from requests import fix_url
import recipes


def get_input(text):
    return input(text)


class Test(TestCase):
    def setUp(self):
        self.counter = 0

    def test_fix_url(self):
        url = "https://www.themealdb.com/api/json/v1/1/search.php?s=soup"
        self.assertEqual(fix_url(url), url)

        url = "https://www.themealdb.com/api/json/v1/1/search.php?s=wonton soup"
        correctUrl = (
            "https://www.themealdb.com/api/json/v1/1/search.php?s=wonton%20soup"
        )
        self.assertEqual(fix_url(url), correctUrl)
        self.assertFalse(fix_url(url) == url)

    @patch("builtins.input", return_value="2")
    def test_get_menu_choice_correct(self, input):
        self.assertEqual(recipes.get_menu_choice(), 2)

    @patch("builtins.input", return_value=10)
    def test_get_menu_choice_incorrect(self, input):
            self.assertEqual(recipes.get_menu_choice(), None)


if __name__ == "__main__":
    main()
