"""
    更简洁的写法
"""
from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        res = [i for j in nums for i in j]
        return [res[i:i + c] for i in range(0, len(res), c)]

nums = [[1, 2],
        [3, 4]]
r = 4
c = 1

s = Solution()
print(s.matrixReshape(nums, r, c))