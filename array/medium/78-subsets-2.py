"""
    迭代
    https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
