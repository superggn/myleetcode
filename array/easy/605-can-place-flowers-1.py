"""
    防御式编程：左右各加1个0，不用写边界条件

"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
            连续3个0即可种1朵花
        """
        flowerbed = [0] + flowerbed
        flowerbed = flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0

nums = [1, 0, 0, 0, 0, 1]
s = Solution()
print(s.canPlaceFlowers(nums, 2))