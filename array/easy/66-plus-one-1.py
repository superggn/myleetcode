"""
    直接转成整数，再转回数组
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - 1 - i))
        num += 1
        ls = []
        while num // 10 != 0 or num%10 != 0:
            ls.append(num % 10)
            num = num // 10
        ls1 = ls[::-1]
        return ls1


n = [4, 3, 2, 1]
s = Solution()
print(s.plusOne(n))
