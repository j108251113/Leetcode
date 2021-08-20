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

    def test_three_characters(self):
        str_list = ['aba', 'abb']
        expect = 2
        for string in str_list:
            self.assertEqual(expect, self.solution.lengthOfLongestSubstring(string))

    def test_four_characters(self):
        str_list = ['abab', 'abca', 'abbb']
        expect = [2, 3, 2]
        for idx, string in enumerate(str_list):
            self.assertEqual(expect[idx], self.solution.lengthOfLongestSubstring(string))

    def test_five_characters(self):
        str_list = ['ababc', 'abbcd']
        expect = [3, 3]
        for idx, string in enumerate(str_list):
            self.assertEqual(expect[idx], self.solution.lengthOfLongestSubstring(string))

    def test_example_string(self):
        str_list = ['abcabcbb', 'pwwkew']
        expect = [3, 3]
        for idx, string in enumerate(str_list):
            self.assertEqual(expect[idx], self.solution.lengthOfLongestSubstring(string))

    def test_leetcode_failed_testcase(self):
        str_list = ['dvdf', 'ckilbkd', "anviaj", 'abba']
        expect = [3, 5, 5, 2]
        for idx, string in enumerate(str_list):
            self.assertEqual(expect[idx], self.solution.lengthOfLongestSubstring(string))
