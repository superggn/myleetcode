"""
    先转置矩阵，再翻转每行
    for循环转置
    for循环翻转
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        n = len(matrix[0])
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
