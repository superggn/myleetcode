from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        ans = [[1] * i for i in range(1, rowIndex + 1)]
        for i in range(2, rowIndex):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans[rowIndex - 1]


s = Solution()
print(s.getRow(9))
