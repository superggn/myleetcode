"""
    思想：存储历史最低点
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1e9
        best_profit = -1e9
        for today in prices:
            best_profit = max(today - min_price, best_profit)
            min_price = min(today, min_price)
        if best_profit < 0:
            return 0
        return best_profit


n = [7, 1, 5, 3, 6, 4]
s = Solution()

print(s.maxProfit(n))
