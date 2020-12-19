from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        m1 = nums[0]
        m2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            m1, m2 = m2, max(m2, m1 + nums[i])
        return m2


