"""
    挨个遍历第二版，时间最少，感觉跟第一版没啥区别
    时间还长了
    记得最后把max0更新下
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max0 = 0
        temp_max = 0
        flag = False
        for i in range(len(nums)):
            if flag:
                if nums[i] == 1:
                    temp_max += 1
                else:
                    max0 = max(max0, temp_max)
                    temp_max = 0
                    flag = False
            else:
                if nums[i] == 1:
                    flag = True
                    temp_max += 1

        return max(max0, temp_max)


nums = [1, 1, 1, 0, 1, 1, 1, 1, 1]
s = Solution()
print(s.findMaxConsecutiveOnes(nums))
