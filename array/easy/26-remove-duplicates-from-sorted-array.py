from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        if len(nums) == 0:
            return 0
        for _ in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

            j += 1
        return i + 1
n=[0,0,1,1,1,2,2,3,3,4]
s=Solution()
s.removeDuplicates(n)
print(n)

