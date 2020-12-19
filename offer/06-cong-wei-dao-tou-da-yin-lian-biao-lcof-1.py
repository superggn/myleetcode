"""
    思路：直接放到列表里然后翻转列表
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]  # 或者 reverse(res)


nums = [1, 2, 5, 3, 4, 6, 2, 0]
h = ListNode(1)
ptr = h
for i in range(1, len(nums)):
    ptr.next = ListNode(nums[i])
    ptr = ptr.next

s = Solution()
print(s.reversePrint(h))
