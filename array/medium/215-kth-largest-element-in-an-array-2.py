"""
    堆排序
    https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/pai-xu-by-powcai-2/
"""
import heapq
from typing import List


# 堆排序
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
