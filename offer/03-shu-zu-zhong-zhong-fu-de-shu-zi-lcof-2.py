from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        temp = nums[-1]
        for i in nums:
            if i == temp:
                return i
            temp = i
