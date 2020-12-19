"""
    思路：堆栈
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        res = []
        while stack:
            res.append(stack.pop())
        return res


nums = [1, 2, 5, 3, 4, 6, 2, 0]
h = ListNode(1)
ptr = h
for i in range(1, len(nums)):
    ptr.next = ListNode(nums[i])
    ptr = ptr.next

s = Solution()
print(s.reversePrint(h))