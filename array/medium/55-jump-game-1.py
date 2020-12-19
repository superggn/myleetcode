"""
    官方
    贪心算法
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            维护：最远距离rightmost
            for循环遍历数组，
                判别当前位置是否满足要求
                    更新rightmost
                若跑到数组外边了，OK
            不OK，return False
        """
        n = len(nums)
        rightmost = 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True

        return False


# nums = [4, 0, 0, 0, 1]
nums = [3, 2, 1, 0, 4]
s = Solution()
print(s.canJump(nums))
