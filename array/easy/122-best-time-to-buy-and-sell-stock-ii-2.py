from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        sum = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                sum += prices[i+1] - prices[i]
        return sum
