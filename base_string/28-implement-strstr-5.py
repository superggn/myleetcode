# 作者：tooooo_the_moon
# 链接：https://leetcode-cn.com/problems/implement-strstr/solution/kmpsuan-fa-by-aa694849243/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
    KMP
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pnext = self.gen_pnext(needle)
        i, j = 0, 0
        len_h, len_n = len(haystack), len(needle)
        while i < len_h and j < len_n:
            if haystack[i] == needle[j] or j == -1:
                i += 1
                j += 1
            else:
                j = pnext[j]
        if j == len_n:
            return i - len_n
        else:
            return -1

    def gen_pnext(self, p: str) -> list:
        k = -1
        pnext = [-1] * len(p)
        i = 0
        while i < len(p) - 1:
            if k == -1 or p[i] == p[k]:
                k += 1
                i += 1
                if p[i] == p[k]:
                    pnext[i] = pnext[k]
                else:
                    pnext[i] = k
            else:
                k = pnext[k]
        return pnext


h = "aaacaaab"
n = "aaab"
sol = Solution()
# print(sol.strStr(h, n))
print(sol.gen_pnext(n))

