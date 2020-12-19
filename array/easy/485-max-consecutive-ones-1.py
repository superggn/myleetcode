"""
    遍历一下就好了
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxcnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                maxcnt = max(maxcnt,cnt)
                cnt = 0
        return max(maxcnt, cnt)