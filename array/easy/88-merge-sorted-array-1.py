"""
    最暴力：1、合并。2、排序。
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1[:] = sorted(nums1[:m] + nums2)
        # 注意：类内必须使用拷贝[:]来操作变量，否则指针指向别的地方
        # nums1 = sorted(nums1[:m] + nums2)


n1 = [1, 2, 3, 0, 0, 0]
m = 3
n2 = [2, 5, 6]
n = 3
s = Solution()
s.merge(n1, m, n2, n)

print(n1)
