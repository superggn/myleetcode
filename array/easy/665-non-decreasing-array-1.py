"""
    在修改1个元素之后，要保证之后不能有
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 初始化计数器
        count = 0
        # 遍历数组，每移动1次，cnt += 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                # 在确认索引位于数组中间的情况下：确认前后区间共4个数字是否仍然不对劲（反序），如果是，直接GG，如果不是，还能打打
                if i + 1 < len(nums) and i - 2 >= 0:
                    if nums[i + 1] < nums[i - 1] and nums[i - 2] > nums[i]:
                        return False
            # cnt check
            if count > 1:
                return False
        return True


nums = [6, 4, 2, 3]

s = Solution()
print(s.checkPossibility(nums))
