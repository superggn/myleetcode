"""
    1、翻转全部
    2、翻转前k个
    3、翻转后n-k个

"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n
        swap(0, n - 1)
        swap(0, k - 1)
        swap(k, n - 1)


# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# s = Solution()
# s.rotate(nums,k)
# print(nums)
