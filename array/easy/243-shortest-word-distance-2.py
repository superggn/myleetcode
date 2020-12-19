"""
    用俩表格存一下word1和word2的位置，再相减，再遍历找最小
"""
from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        pos1 = []
        pos2 = []
        for i, v in enumerate(words):
            if v == word1:
                pos1.append(i)
            if v == word2:
                pos2.append(i)
        # 开始相减

        dif = []
        for i in range(len(pos1)):
            for j in range(len(pos2)):
                dif.append(abs(pos1[i]-pos2[j]))
        result = min(dif)
        return result

