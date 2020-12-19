# Definition for singly-linked list.
from my_code.lib_ggn import display_linked_list, gen_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp_l1 = l1
        temp_l2 = l2
        dummy = ListNode()
        temp = dummy
        while temp_l1 and temp_l2:
            if temp_l1.val < temp_l2.val:
                temp.next = temp_l1
                temp = temp.next
                temp_l1 = temp_l1.next
            elif temp_l1.val >= temp_l2.val:
                temp.next = temp_l2
                temp = temp.next
                temp_l2 = temp_l2.next
        if temp_l1:
            while temp_l1:
                temp.next = temp_l1
                temp = temp.next
                temp_l1 = temp_l1.next
        if temp_l2:
            while temp_l2:
                temp.next = temp_l2
                temp = temp.next
                temp_l2 = temp_l2.next
        return dummy.next


ls1 = [1, 2, 4]
ls2 = [1, 3, 4]
head1 = gen_linked_list(ls1)
head2 = gen_linked_list(ls2)
sol = Solution()
res_head = sol.mergeTwoLists(head1, head2)
display_linked_list(res_head)
