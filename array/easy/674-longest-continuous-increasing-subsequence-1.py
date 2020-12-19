from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # 初始化
        ans = anchor = 0
        # 遍历数组，若没有遍历到头且递增被打断，更新anchor，更新max_length
        for i in range(len(nums)):
            ans = max(ans, i - anchor + 1)# i - ans + 1: 这是从锚定点到所在点之间的距离
            if i < len(nums) - 1 and nums[i] >= nums[i + 1]:
                anchor = i + 1
        return ans


# nums = [1, 3, 5, 7]
nums = [1, 3, 5, 4, 2, 3, 4, 5]
s = Solution()
print(s.findLengthOfLCIS(nums))