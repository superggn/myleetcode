"""
    双指针
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1

nums = [0, 0, 0, 1]
s = Solution()
s.moveZeroes(nums)
print(nums)
# print(temp)
