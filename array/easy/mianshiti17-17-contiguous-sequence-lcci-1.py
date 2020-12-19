"""
    nums[i] = max(nums[i]+nums[i-1], nums[i])
    https://leetcode-cn.com/problems/contiguous-sequence-lcci/solution/dong-tai-gui-hua-by-yi-wen-statistics-13/
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if nums == []:
        #     return 0
        # else:
        #     for i in range(1, len(nums)):
        #         nums[i] = max(nums[i] + nums[i - 1], nums[i])
        #     return max(nums)

        if not nums:
            return 0
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])
        return max(nums)


n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

s = Solution()
print(s.maxSubArray(n))

