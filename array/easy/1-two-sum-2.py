"""
    思路：把遍历过的数据存入缓存，每次查找之前，先在缓存中查找有没有，如果有目标数据，就不用算了。
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, v in enumerate(nums):
            if v in cache:
                return [cache[v], idx]
            remnant = target - v
            cache[remnant] = idx
        return None


nums = [1, 1, 1, 1, 1, 2, 1, 4, 1, 1]
s = Solution()
print(s.twoSum(nums, 9))

