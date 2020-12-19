"""
    正则表达式写法
    用正则其实算是取巧了
"""

import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall(r'^[+-]?\d+', s.lstrip())), 2**31 - 1), -2**31)



sol = Solution()
# s = "-91283472332"
s = "-12"
print(sol.myAtoi(s))