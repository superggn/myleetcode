"""
    快慢指针
"""

from my_code.lib_ggn import display_linked_list, gen_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


head = gen_linked_list([3, 2, 0, -4])
temp = head

while temp.next:
    temp = temp.next
tail = temp
tail.next = head.next

sol = Solution()
head = sol.hasCycle(head)
print(head)
