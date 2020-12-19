"""
    二分法:
        缩start和end
        注意start和end中间差1

        注意，end不参与索引取值，所以不用取len(nums)-1，直接len(nums)就OK
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        mid = (start + end) // 2
        while start < end:
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
            mid = (start + end) // 2
        return start




n = [1, 3, 5, 6]
s = Solution()
print(s.searchInsert(n, 7))
print(n)
