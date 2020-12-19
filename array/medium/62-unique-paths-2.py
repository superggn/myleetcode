"""
    动态规划
    https://leetcode-cn.com/problems/unique-paths/solution/dong-tai-gui-hua-by-powcai-2/
"""
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 注意，这里不能用[1] for i in range(n)，这样的话出来的就不是[1,1,1,1]而是[[1],[1],[1],[1]]
        # 初始化dp

        # dp是2维数组
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[-1][-1]


s = Solution()
print(s.uniquePaths(3, 7))
