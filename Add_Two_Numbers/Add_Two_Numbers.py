# You are given two non-empty linked lists representing two non-negative integer
# s. The digits are stored in reverse order, and each of their nodes contains a si
# ngle digit. Add the two numbers and return the sum as a linked list. 
# 
#  You may assume the two numbers do not contain any leading zero, except the nu
# mber 0 itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#  
# 
#  Example 2: 
# 
#  
# Input: l1 = [0], l2 = [0]
# Output: [0]
#  
# 
#  Example 3: 
# 
#  
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each linked list is in the range [1, 100]. 
#  0 <= Node.val <= 9 
#  It is guaranteed that the list represents a number that does not have leading
#  zeros. 
#  
#  Related Topics Linked List Math Recursion 
#  👍 13155 👎 2964


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        """
        :type next: ListNode
        """
        self.next = next
        self.val = val


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, q: int = 0) -> ListNode:
        node = ListNode()
        if l1 is not None and l2 is not None:
            q_, node.val = divmod(l1.val + l2.val + q, 10)
            node.next = self.addTwoNumbers(l1.next, l2.next, q_)
        elif l1 is None and l2 is not None:
            q_, node.val = divmod(q + l2.val, 10)
            node.next = self.addTwoNumbers(None, l2.next, q_)
        elif l2 is None and l1 is not None:
            q_, node.val = divmod(q + l1.val, 10)
            node.next = self.addTwoNumbers(l1.next, None, q_)
        elif q > 0:
            node.val = q
        else:
            node = None
        return node

# leetcode submit region end(Prohibit modification and deletion)
