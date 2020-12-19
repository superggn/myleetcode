"""
    集合运算
    集合去重
    集合求和*2-原数组求和
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_ = set()
        for i in nums:
            set_.add(i)
        return sum(set_) * 2 - sum(nums)
