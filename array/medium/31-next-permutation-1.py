"""
    两遍扫描
    来自官方
    题意：
        找出这个数组排序出的所有数中，刚好比当前数大的那个数
    https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 从后向前遍历
        i = len(nums) - 2
        # i表示降序终止的位置，题解中的“较小数”
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # j表示从后向前找，比i大的数，二者交换位置
        # 如果i != -1,证明数组不是全降序，可以进行交换的操作
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 交换位置后，i为“较大数”的位置，这时，把i右侧的数组进行升序排列，让变大的幅度尽可能小
        # 升序只需要交换left和right的位置，因为原来i右侧的数组全部为降序
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
