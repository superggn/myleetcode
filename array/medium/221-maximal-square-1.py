"""
    dp
    https://leetcode-cn.com/problems/maximal-square/solution/zui-da-zheng-fang-xing-by-leetcode-solution/
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare
