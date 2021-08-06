from typing import List
from unittest import TestCase
from Add_Two_Numbers import Solution
from Add_Two_Numbers import ListNode


class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_solution_example_one(self):
        def makeLinkList(arr: List, node: ListNode = None) -> ListNode:
            while arr:
                val = arr.pop()
                return makeLinkList(arr, ListNode(val=val, next=node))
            return node

        l1 = makeLinkList([2, 4, 3])
        l2 = makeLinkList([5, 6, 4])
        expect = [7, 0, 8]
        self.assertEqual(expect, self.solution.addTwoNumbers(l1, l2))
