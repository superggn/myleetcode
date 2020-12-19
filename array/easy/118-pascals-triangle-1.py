"""
    注意看返回类型，以及输出是啥
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] * i for i in range(1, numRows + 1)]
        for r in range(2, numRows):
            for c in range(1, r):
                ans[r][c] = ans[r - 1][c - 1] + ans[r - 1][c]
        return ans


s = Solution()
result = s.generate(10)
for i in range(len(result)):
    print(' ' * (len(result) - 1 - i), result[i])
