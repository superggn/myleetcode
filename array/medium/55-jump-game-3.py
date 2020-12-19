"""
    熊猫解题
    贪心算法
    https://leetcode-cn.com/problems/jump-game/solution/xiong-mao-shua-ti-python3-tan-xin-wei-hu-ke-da-dao/
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums: return True  # 如果没有0则一定可以到达
        if len(nums) < 2: return True
        max_distance = nums[0]  # 设定可以达到的最大坐标
        for i in range(1, len(nums) - 1):
            if i <= max_distance:  # 表示当前坐标可以达到
                max_distance = max(max_distance, i + nums[i])  # 更新可以达到的最远坐标
            else:
                break
        return max_distance >= len(nums) - 1

