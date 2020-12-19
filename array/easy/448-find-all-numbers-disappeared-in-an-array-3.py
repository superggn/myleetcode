"""
    原地替换，标记原来数组以实现不使用多余的存储空间
    如果哪个位置没被标负，那么对应的索引在数组中肯定没出现过
    用-1标记，不使用额外空间
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for idx, v in enumerate(nums):
            new_idx = abs(v) - 1
            if nums[new_idx] > 0:
                nums[new_idx] *= -1
        ls = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ls.append(i + 1)
        return ls


nums = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution()
print(s.findDisappearedNumbers(nums))
