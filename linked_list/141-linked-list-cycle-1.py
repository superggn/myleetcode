"""
    集合判别
    把遍历跑起来，如果指针见过，那就有环，反之没有
"""

from my_code.lib_ggn import display_linked_list, gen_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
