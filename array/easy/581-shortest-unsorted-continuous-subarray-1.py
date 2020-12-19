"""
    最简洁的写法：
        排序
        寻找破坏升序降序的位置，算出长度
    重点是去除边界条件：
        res == num
    这种做法用了排序，还是算作弊了
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        res = sorted(nums)
        if res == nums:
            return 0
        left = 0
        right = len(nums) - 1
        while res[left] == nums[left]:
            left += 1
        while res[right] == nums[right]:
            right -= 1
        return right - left + 1
