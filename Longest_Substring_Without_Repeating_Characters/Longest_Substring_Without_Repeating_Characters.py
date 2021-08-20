# Given a string s, find the length of the longest substring without repeating c
# haracters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  Example 4: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics Hash Table String Sliding Window 
#  👍 16399 👎 792


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_idx = 0
        max_length = 0
        hashmap = {}
        for idx, char in enumerate(s):
            if char not in hashmap:
                pass
            else:
                start_idx = max(start_idx, hashmap[char] + 1)
            hashmap[char] = idx
            max_length = max(max_length, idx - start_idx + 1)
        return max_length
# leetcode submit region end(Prohibit modification and deletion)
