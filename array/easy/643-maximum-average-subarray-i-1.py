"""
    超时了
    每次都重新算，不好，基于上一个修改就好
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum([nums[i] for i in range(k)])
        for i in range(1,len(nums) - k+1):
            temp_sum = sum([nums[i + j] for j in range(k)])
            cur_sum = max(temp_sum, cur_sum)
        return cur_sum / k

nums = [0,1,1,3,3]
s = Solution()
print(s.findMaxAverage(nums, 4))
