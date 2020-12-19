"""
    双指针
    https://leetcode-cn.com/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode-solution/
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 初始化双指针及ans
        # 遍历双指针，当两个指针没有碰撞的时候
        # 计算当前面积、截止到现在最大面积
        # 根据短板效应，更新指针位置，哪个短，动哪个
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
