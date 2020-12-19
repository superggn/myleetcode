"""
    双指针
    i是快指针，j是慢指针
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 边界条件初始化
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]

        result = []
        # j是一段区间的开头
        j = 0

        for i in range(len(nums)):
            if i:
                # 开始不连续了，结算
                if nums[i] - nums[i-1] != 1:
                    if j == i-1:
                        result.append(str(nums[j]))
                    else:
                        result.append(str(nums[j]) + '->' + str(nums[i-1]))
                    if i == len(nums)-1:
                        result.append(str(nums[i]))
                    j = i
            # 到头了，结算
            # i到头了，j没到头
            if i == len(nums)-1 and j < len(nums)-1:
                result.append(str(nums[j]) + '->' + str(nums[i]))
        return result

nums = [0,2,3,4,6,8,9]
s = Solution()
print(s.summaryRanges(nums))