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
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        list_list = [[]]
        for char in s:
            if char not in list_list[-1]:
                list_list[-1].append(char)
            elif last_add != char:
                new_list = list_list[-1].copy()
                new_list.reverse()
                while new_list.pop() != char:
                    continue
                new_list.reverse()
                new_list.append(char)
                list_list.append(new_list)
            else:
                list_list.append([char])
            last_add = char
        return max(map(len, list_list))
# leetcode submit region end(Prohibit modification and deletion)
