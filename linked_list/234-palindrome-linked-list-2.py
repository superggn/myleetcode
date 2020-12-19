"""
    逆转后半部分，遍历比较前后两半是否相同，恢复链表结构之后返回flag
"""

from my_code.lib_ggn import display_linked_list, gen_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        first_half_end = self.end_of_first_half(head)
        second_hald_start = self.reverse_list(first_half_end.next)
        temp_ptr1 = head
        temp_ptr2 = second_hald_start
        flag = True
        while temp_ptr2:
            if temp_ptr2.val != temp_ptr1.val:
                flag = False
                break
            temp_ptr1 = temp_ptr1.next
            temp_ptr2 = temp_ptr2.next

        # 恢复链表
        first_half_end.next = self.reverse_list(second_hald_start)

        return flag

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


ls = [1, 2, 3, 2, 1, 2, 3, 2, 1]
head = gen_linked_list(ls)
sol = Solution()
print(sol.isPalindrome(head))
