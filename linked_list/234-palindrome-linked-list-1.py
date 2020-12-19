from my_code.lib_ggn import display_linked_list, gen_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ls = []
        temp = head
        while temp:
            ls.append(temp.val)
            temp = temp.next
        return ls == ls[::-1]


ls = [1, 2, 3, 2, 2, 1]
head = gen_linked_list(ls)
sol = Solution()
print(sol.isPalindrome(head))
