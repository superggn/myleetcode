from my_code.lib_ggn import *


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        v_head = ListNode()
        v_head.next = head
        p = q = v_head
        for _ in range(n):
            q = q.next
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return v_head.next



# 生成输入链表
ls = [1, 2, 3, 4, 5]
head = gen_linked_list(ls)
# display_linked_list(head)

sol = Solution()
head = sol.removeNthFromEnd(head, 5)

display_linked_list(head)

