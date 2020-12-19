"""
    直接把数量存字典里
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = 1
            else:
                dct[nums[i]] += 1
        ls = []
        for j in range(1, len(nums) + 1):
            if j not in dct:
                ls.append(j)
        return ls


nums = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution()
print(s.findDisappearedNumbers(nums))




