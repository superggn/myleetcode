"""
    hash实现，借助内置函数
"""

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


s = "asdf"
t = "fdsa"
sol = Solution()
print(sol.isAnagram(s, t))
