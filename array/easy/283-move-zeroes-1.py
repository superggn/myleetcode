"""
    此方法超级慢，因为每次都要判断0在不在nums里面
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        while 0 in nums:
            nums.remove(0)
            cnt += 1
        while cnt != 0:
            nums.append(0)
            cnt -= 1


nums = [0, 0, 0, 1]
s = Solution()
s.moveZeroes(nums)
print(nums)
# print(temp)
