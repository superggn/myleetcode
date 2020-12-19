"""
    去除边界条件
    初始化cursum和res
    更新cursum和res(全局最大子序列之和,就是max)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res, current_sum = float('-inf'), float('-inf')
        for n in nums:
            current_sum = n if current_sum < 0 else n + current_sum
            res = max(current_sum, res)
        return res

# n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# s = Solution()
# print(s.maxSubArray(n))
