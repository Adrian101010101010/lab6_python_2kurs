import unittest
from src.lab6 import search_substring


class TestSearchSubstringFunction(unittest.TestCase):
    def test_empty_strings(self):
        haystack = ""
        needle = ""
        result = search_substring(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_needle(self):
        haystack = "abracadabra"
        needle = ""
        result = search_substring(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_haystack(self):
        haystack = ""
        needle = "abc"
        result = search_substring(haystack, needle)
        self.assertEqual(result, [])

    def test_no_match(self):
        haystack = "abracadabra"
        needle = "xyz"
        result = search_substring(haystack, needle)
        self.assertEqual(result, [])

    def test_single_match(self):
        haystack = "abracadabra"
        needle = "cad"
        result = search_substring(haystack, needle)
        self.assertEqual(result, [4])

    def test_multiple_matches(self):
        haystack = "ababcababcabcabc"
        needle = "abc"
        result = search_substring(haystack, needle)
        self.assertEqual(result, [2, 7, 10, 13])


if __name__ == '__main__':
    unittest.main()
