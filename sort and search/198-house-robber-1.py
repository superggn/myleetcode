"""
    https://leetcode-cn.com/problems/house-robber/solution/wo-shi-yi-ge-hui-dong-tai-gui-hua-de-xiao-tou-by-b/
    动态规划
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        m1 = nums[0]
        m2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            m1, m2 = m2, max(m1 + nums[i], m2)
        return m2
