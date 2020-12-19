"""
    双指针法
    也能用二分查找，也算是双指针，慢指针遍历数组，快指针进行二分查找

"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
