"""
    位运算:最优！
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return None
        res = 0
        for i in nums:
            res = i ^ res
        return res
