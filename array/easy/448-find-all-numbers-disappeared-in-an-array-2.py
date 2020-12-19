"""
    集合运算
    这里用的时间都非常长，动不动几百毫秒
    性能80%
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s1 = set(range(1, len(nums) + 1))
        s2 = set(nums)
        return list(s1 - s2)


nums = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution()
print(s.findDisappearedNumbers(nums))
