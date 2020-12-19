"""
    思路：遍历表格，查找符合条件的值
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    index1 = i
                    index2 = j
                    break
        return [index1, index2]


nums = [2, 7, 11, 15]
s = Solution()
