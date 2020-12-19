"""
    统一思路；找5个数字：最大的3个和最小的两个
    方法2：线性扫描


"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = -float('inf')
        max2 = -float('inf')
        max3 = -float('inf')
        min1 = float('inf')
        min2 = float('inf')

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1*max2*max3 , max1*min1*min2)

