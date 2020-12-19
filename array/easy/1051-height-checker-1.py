"""
    排序，逐项对比
    https://leetcode-cn.com/problems/height-checker/solution/dui-bi-pai-xu-ji-shu-pai-xu-by-yi-wen-statistics/
    评论区某网友：这题目有毛病。。。要求你对比排序后和排序前位置不一样的个数就直接说吗。。。花里胡哨的
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights1 = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != heights1[i]:
                res += 1
        return res
