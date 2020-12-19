"""
    自己写的
    集合运算
    效果还不错
    主要时间应该还是在sort里
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set0 = set(nums)
        ls = list(set0)
        ls.sort()
        if len(ls) < 3:
            return ls[-1]
        else:
            return ls[-3]
