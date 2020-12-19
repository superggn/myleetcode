"""
    字典
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = {}
        for i in nums:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
        for i in dct.keys():
            if dct[i] == 1:
                return i
