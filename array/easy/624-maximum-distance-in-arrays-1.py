"""
    粗暴遍历，这个方法巨慢，但是在某些情况下还可以
"""
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_ = arrays[0][-1]
        min_ = arrays[0][0]
        ans = float("-inf")
        for i in range(1, len(arrays)):
            ans = max(ans, max(abs(arrays[i][-1] - min_), abs(arrays[i][0] - max_)))
            min_ = min(arrays[i][0], min_)
            max_ = max(arrays[i][-1], max_)
        return ans


