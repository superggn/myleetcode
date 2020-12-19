"""
    直接用字典
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict0 = {}
        for i in range(len(nums)):
            if i not in dict0.keys():
                dict0[i] = 1
            else:
                dict0[i] += 1
        for k, v in dict0:
            if v > 1:
                return True
        return False

nums = [1,2,3,4,4,5]
s = Solution()
s.containsDuplicate(nums)