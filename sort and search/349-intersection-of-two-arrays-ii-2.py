"""
    聪明点，遍历短数组，构造{数字：出现次数}的字典，再遍历长数组

"""
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct = {}
        # 区分long,short
        if len(nums1) > len(nums2):
            arr_short = nums2
            arr_long = nums1
        else:
            arr_short = nums1
            arr_long = nums2
        # 构造字典
        for i in arr_short:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1

        res = []
        for i in arr_long:
            if i in dct and dct[i] > 0:
                dct[i] -= 1
                res.append(i)

        return res











