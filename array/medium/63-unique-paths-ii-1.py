"""
    熊猫
    二维dp
    https://leetcode-cn.com/problems/unique-paths-ii/solution/xiong-mao-shua-ti-python3-2wei-dpzhu-yi-bi-kai-pyt/
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
            初始化变量和路径列表
            for循环初始化首行、首列
            遍历内容，若无障碍，计算dp

        """
        # 初始化变量和路径列表
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        temp = [[0] * n for i in range(m)]

        # 初始化首行首列
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                temp[0][j] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                temp[i][0] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    temp[i][j] = temp[i - 1][j] + temp[i][j - 1]
        return temp[-1][-1]
