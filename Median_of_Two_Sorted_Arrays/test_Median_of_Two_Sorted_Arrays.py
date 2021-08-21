from unittest import TestCase
from Median_of_Two_Sorted_Arrays import Solution


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_one_digit(self):
        nums1 = []
        nums2 = [1]
        expect = 1.00000
        self.assertEqual(expect, self.solution.findMedianSortedArrays(nums1, nums2))

        nums1 = [2]
        nums2 = []
        expect = 2.00000
        self.assertEqual(expect, self.solution.findMedianSortedArrays(nums1, nums2))

    def test_two_digits(self):
        nums1 = [1]
        nums2 = [1]
        expect = 1.00000
        self.assertEqual(expect, self.solution.findMedianSortedArrays(nums1, nums2))

        nums1 = [2]
        nums2 = [1]
        expect = 1.50000
        self.assertEqual(expect, self.solution.findMedianSortedArrays(nums1, nums2))
