"""
    数组拆分，简单的排序之后奇数位相加
"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum0 = 0
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 0:
                sum0 += nums[i]
        return sum0

