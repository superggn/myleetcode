"""
    用字典
    k = nums[i]
    v = i
    翻一下键和值就好
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict0 = {}
        for i in range(len(nums)):
            if nums[i] in dict0 and i - dict0[nums[i]] <= k:
                return True
            else:
                dict0[nums[i]] = i
        return False

nums = [1,2,3,1]
k = 3
s = Solution()
print(s.containsNearbyDuplicate(nums, k))
