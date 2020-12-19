"""

"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum([nums[i] for i in range(k)])
        ls = [cur_sum]
        for i in range(len(nums) - k):
            cur_sum += nums[i+k] - nums[i]
            ls.append(cur_sum)
        res = max(ls)
        return res / k