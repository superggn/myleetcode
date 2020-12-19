"""
    和移除相同元素思路相同，使用双指针法
    把相同的丢到后面去
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        if len(nums) == 0:
            return 0
        for _ in range(len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i


n = [0, 1, 2, 2, 3, 3, 4, 0, 4, 2]
s = Solution()
print(s.removeElement(n, 3))
print(n)