"""
    一天可以交易多次...只要不同时持有多只股票，1天买多少次都行
    那就造呗，每天的差额都算上，正的就买，负的拉倒
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] - prices[i - 1] > 0)
