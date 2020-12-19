"""
    因为要考虑在数组中出现的次数，不能简单地用集合运算，要用哈希表（字典）
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        size1 = len(nums1)
        size2 = len(nums2)
        if size1 > size2:
            long_arr = nums1
            short_arr = nums2
        else:
            long_arr = nums2
            short_arr = nums1
        dct = {}
        for i in short_arr:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
        res = []
        for j in long_arr:
            if j in dct.keys():
                dct[j] -= 1
                if dct[j] >= 0:
                    res.append(j)
        return res
