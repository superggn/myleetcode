"""
    滑动窗口
    https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/hua-dong-chuang-kou-on-er-fen-fa-onlogn-by-powcai/
"""

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        left = 0
        cur = 0
        res = float("inf")
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        return res if res != float("inf") else 0
