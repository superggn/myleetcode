# Definition for singly-linked list.
from my_code.lib_ggn import gen_linked_list, display_linked_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        return prev


ls = [1, 2, 3, 4, 5]
head = gen_linked_list(ls)
sol = Solution()
head = sol.reverseList(head)
display_linked_list(head)
