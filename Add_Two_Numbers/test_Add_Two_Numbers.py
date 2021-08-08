from typing import List
from unittest import TestCase

from Add_Two_Numbers import ListNode
from Add_Two_Numbers import Solution


class Test(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def makeLinkList(self, arr: List, node: ListNode = None) -> ListNode:
        while arr:
            val = arr.pop()
            return self.makeLinkList(arr, ListNode(val=val, next=node))
        return node

    def test_solution_example_one(self):
        l1 = self.makeLinkList([2, 4, 3])
        l2 = self.makeLinkList([5, 6, 4])
        node = self.solution.addTwoNumbers(l1, l2)
        for n in [7, 0, 8]:
            self.assertEqual(n, node.val)
            node = node.next
        self.assertEqual(None, node)

    def test_solution_example_two(self):
        l1 = self.makeLinkList([0])
        l2 = self.makeLinkList([0])
        node = self.solution.addTwoNumbers(l1, l2)
        for n in [0]:
            self.assertEqual(n, node.val)
            node = node.next
        self.assertEqual(None, node)

    def test_solution_example_three(self):
        l1 = self.makeLinkList([9, 9, 9, 9, 9, 9, 9])
        l2 = self.makeLinkList([9, 9, 9, 9])
        node = self.solution.addTwoNumbers(l1, l2)
        for n in [8, 9, 9, 9, 0, 0, 0, 1]:
            self.assertEqual(n, node.val)
            node = node.next
        self.assertEqual(None, node)
