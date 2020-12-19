"""
    暴力遍历
    https://leetcode-cn.com/problems/diving-board-lcci/solution/xiong-mao-shua-ti-python3-mei-zeng-jia-yi-ge-chang/
"""
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        # 边界条件
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        # 初始化
        res = [shorter * k]
        diff = longer - shorter

        for i in range(1, k + 1):
            res.append(res[-1] + diff)
        return res
