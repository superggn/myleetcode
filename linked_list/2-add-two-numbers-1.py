"""
    根据题意可知链表数字位数是从小到大的

    因为两个数字相加会产生进位，所以使用i来保存进位。
    则当前位的值为(l1.val + l2.val + i) % 10
    则进位值为(l1.val + l2.val + i) / 10
    建立新node，然后将进位传入下一层。

    https://leetcode-cn.com/problems/add-two-numbers/solution/di-gui-si-lu-jian-dan-dai-ma-duan-by-dnanki/
"""
from my_code.lib_ggn import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def dfs(l, r, i):
            if not l and not r and not i: return None
            s = (l.val if l else 0) + (r.val if r else 0) + i
            node = ListNode(s % 10)
            node.next = dfs(l.next if l else None, r.next if r else None, s // 10)
            return node
        return dfs(l1, l2, 0)


