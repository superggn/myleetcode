"""
    更快的双指针
    来自提交详情
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxsize = 0

        while left < right:
            f = right - left
            if height[left] < height[right]:
                h = height[left]
                left = left + 1
            else:
                h = height[right]
                right = right - 1
            size = f * h
            if maxsize < size:
                maxsize = size
        return maxsize


h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
s = Solution()
print(s.maxArea(h))
