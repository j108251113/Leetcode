from unittest import TestCase
from Two_Sum import Solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_two_sum_example_one(self):
        nums = [2, 7, 11, 15]
        target = 9
        expect = [0, 1]
        self.assertEqual(expect, self.solution.twoSum(nums, target))

    def test_two_sum_example_two(self):
        nums = [3, 2, 4]
        target = 6
        expect = [1, 2]
        self.assertEqual(expect, self.solution.twoSum(nums, target))
