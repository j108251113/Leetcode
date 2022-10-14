# Given a string s, return the longest palindromic substring in s.
#
# A string is called a palindrome string if the reverse of that string is the same as the original string.
#
#
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#
# Constraints:
#
#     1 <= s.length <= 1000
#     s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        def isPalindrome(string: str):
            return string == string[::-1]

        if len(s) == 2:
            return s if isPalindrome(s) else s[0]

        if isPalindrome(s):
            return s
