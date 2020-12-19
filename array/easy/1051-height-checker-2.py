"""
    排序，逐项对比
    https://leetcode-cn.com/problems/height-checker/solution/dui-bi-pai-xu-ji-shu-pai-xu-by-yi-wen-statistics/
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        frequency = [0 for i in range(101)]
        for i in heights:
            frequency[i] += 1
        k = 0
        res = 0
        for j in range(1, 101):
            while frequency[j]:
                if heights[k] != j:
                    res += 1
                k += 1
                frequency[j] -= 1
        return res
