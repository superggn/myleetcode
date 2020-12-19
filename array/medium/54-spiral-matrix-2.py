"""
    读题！！！
        从首行开始，从外向内螺旋遍历！
    拿一行

    https://leetcode-cn.com/problems/spiral-matrix/solution/na-yi-xing-ni-shi-zhen-zhuan-yi-xia-by-suixin-3/
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix:
            # 取出矩阵首行，削去首行
            res += matrix.pop(0)
            # 矩阵往左边旋转，削掉首行
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res

        res = []
        while matrix:
            # 取出第一行
            res += matrix.pop(0)
            # matrix更新为matrix转置后行颠倒，把下一个要取出的行放到第一个
            matrix = list(map(list, zip(*matrix)))[::-1]
            print(matrix)
        return res


m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s = Solution()
print(s.spiralOrder(m))
