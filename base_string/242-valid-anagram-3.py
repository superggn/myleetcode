"""
    内置函数排序
"""

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False


s = "asdf"
t = "fdsa"
sol = Solution()
print(sol.isAnagram(s, t))
