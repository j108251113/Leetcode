import unittest
from Longest_Palindromic_Substring import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_one_character(self):
        s = "a"
        expect = "a"
        self.assertEqual(expect, self.solution.longestPalindrome(s))


if __name__ == '__main__':
    unittest.main()
