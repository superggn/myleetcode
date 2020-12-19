"""
    统一思路；找5个数字：最大的3个和最小的两个
    方法1：排序找

    就两种情况，0，1，-1和-1，-2，-3
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1]
        )



