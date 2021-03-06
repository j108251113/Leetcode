# Given an array of integers nums and an integer target, return indices of the t
# wo numbers such that they add up to target.
#
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice.
#
#  You can return the answer in any order.
#
#
#  Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
#  Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
#  Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
#  Constraints:
#
#
#  2 <= nums.length <= 104
#  -109 <= nums[i] <= 109
#  -109 <= target <= 109
#  Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time comp
# lexity? Related Topics Array Hash Table
#  👍 23271 👎 774


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 2:
            return [0, 1]

        for idx, num in enumerate(nums):
            difference = target - num
            rest_nums = nums[idx + 1:length]
            if difference == num and difference in rest_nums:
                return [idx, rest_nums.index(difference) + idx + 1]
            else:
                if difference in rest_nums:
                    return [idx, nums.index(difference)]
# leetcode submit region end(Prohibit modification and deletion)
