"""
    动态规划
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0  # 边界条件
        dp = [0] * n  # 注意，这里的dp里面装着的其实就是best_price
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]


prices = [7, 1, 5, 3, 6, 4]
s = Solution()

print(s.maxProfit(prices))
