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
        longest = []

        def isPalindrome(string: str):
            return string == string[::-1]

        maxLen = 0
        while len(s) > maxLen:
            subStr = s
            while len(subStr) > maxLen:
                strlen = len(subStr)
                if subStr[0] == subStr[-1] and isPalindrome(subStr):
                    if strlen > maxLen:
                        longest.append(subStr)
                        maxLen = strlen
                        break
                    break
                else:
                    ridx = subStr.rindex(subStr[0])
                    if subStr[ridx] != subStr[-1]:
                        subStr = subStr[:ridx + 1]
                    else:
                        subStr = subStr[:-1]
            s = s[1:]
        return longest[-1]
