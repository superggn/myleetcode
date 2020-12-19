"""

"""
from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        total = len(nums) * len(nums[0])
        if r * c != total:
            return nums

        temp_ls = []

        for i in range(len(nums)):
            for j in range(len(nums[0])):
                temp_ls.append(nums[i][j])

        result = []
        for i in range(r):
            result.append([])
            for j in range(c):
                result[i].append(temp_ls[i * c + j])
        return result
