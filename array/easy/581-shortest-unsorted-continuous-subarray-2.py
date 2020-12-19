"""
    双指针法
    如果有比现在最小值小的，右指针挪到左边
    如果有比现在最大值大的，左指针挪到右边
    边界条件可能要改一下
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        size = len(nums)
        if size <= 1:
            return 0
        left = size - 2
        right = 1
        cur_min = nums[-1]
        cur_max = nums[0]
        # 注意，此处初始化up和down的时候，考虑完全升序的数组情况下，不会改变up和down的数值，此时初始化的值能满足输出正确答案
        up = 0
        down = 1
        while left >= 0 and right < size:
            # 寻找不按序下降的
            if nums[left] > cur_min:
                down = left
            else:
                cur_min = nums[left]
            # 寻找不按序上升的
            if nums[right] < cur_max:
                up = right
            else:
                cur_max = nums[right]
            left -= 1
            right += 1

        return up - down + 1


n = [2, 6, 4, 8, 10, 9, 15]
s = Solution()
print(s.findUnsortedSubarray(n))
