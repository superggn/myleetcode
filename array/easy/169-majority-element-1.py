"""
    简单点，找众数直接排序取中间就好了
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums) // 2]
