import unittest
from Longest_Palindromic_Substring import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_one_character(self):
        s = "a"
        expect = "a"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

    def test_two_characters(self):
        s = "ab"
        expect = "a"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "bb"
        expect = "bb"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

    def test_three_characters(self):
        s = "aba"
        expect = "aba"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "abc"
        expect = "a"
        self.assertEqual(expect, self.solution.longestPalindrome(s))

        s = "aab"
        expect = "aa"
        self.assertEqual(expect, self.solution.longestPalindrome(s))


if __name__ == '__main__':
    unittest.main()
