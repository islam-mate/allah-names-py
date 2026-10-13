import unittest
from allah_names import (
    get_all_names,
    get_by_number,
    get_random_name,
    search_names,
)


class TestAllahNames(unittest.TestCase):

    def test_total_names(self):
        names = get_all_names()
        self.assertEqual(len(names), 99)

    def test_first_name(self):
        name = get_by_number(1)
        self.assertIsNotNone(name)
        self.assertEqual(name.arabic, "الله")
        self.assertEqual(name.number, 1)

    def test_search_names(self):
        # Search for Rahman
        results = search_names("Rahman")
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0].arabic, "الرحمن")

        # Search for Arabic text
        results_ar = search_names("الرحيم")
        self.assertTrue(len(results_ar) > 0)

    def test_random_name(self):
        name = get_random_name()
        self.assertTrue(1 <= name.number <= 99)
        self.assertTrue(len(name.arabic) > 0)


if __name__ == "__main__":
    unittest.main()
