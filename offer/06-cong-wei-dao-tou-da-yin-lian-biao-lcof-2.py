"""
    递归思路，分解问题到更小的规模
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        return self.reversePrint(head.next) + [head.val]


nums = [1, 2, 3, 4, 5]
h = ListNode(1)
ptr = h
for i in range(1, len(nums)):
    ptr.next = ListNode(nums[i])
    ptr = ptr.next

s = Solution()
print(s.reversePrint(h))
