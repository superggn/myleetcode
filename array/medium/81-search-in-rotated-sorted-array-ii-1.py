"""
    李威威大佬
    上一题是33题
    https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/er-fen-cha-zhao-by-liweiwei1419/

"""
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        size = len(nums)
        if size == 0:
            return False

        left = 0
        right = size - 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid]:
                    # 落在前有序数组里
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                # 让分支和上面分支一样
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                # 要排除掉左边界之前，先看一看左边界可以不可以排除
                if nums[left] == target:
                    return True
                left = left + 1
        # 后处理，夹逼以后，还要判断一下，是不是 target
        return nums[left] == target

