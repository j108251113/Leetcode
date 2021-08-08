from unittest import TestCase
from Longest_Substring_Without_Repeating_Characters import Solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_empty_string(self):
        s = ''
        expect = 0
        self.assertEqual(expect, self.solution.lengthOfLongestSubstring(s))

    def test_one_character_repeating(self):
        s = 'bbbbb'
        expect = 1
        self.assertEqual(expect, self.solution.lengthOfLongestSubstring(s))
