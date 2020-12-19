"""
    直接用内置的转换函数
    转换的函数，查找、排序的有自己的题，不用纠结
    单行转换

    转成str，join连上——转int——+1——转str——分割放数组里

    控制数组的0开头:（好烦啊，之前不用管开头的0的...）
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len0 = len(digits)
        res_str = str(int("".join(str(j) for j in digits)) + 1)
        zeros = 0
        if len(res_str) < len0:
            zeros = len0 - len(res_str)
        res_str = "0" * zeros + res_str

        return [int(i) for i in res_str]
