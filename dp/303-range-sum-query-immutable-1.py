from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.mem = nums[:]
        for i in range(1, len(nums)):
            self.mem[i] = self.mem[i - 1] + self.mem[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.mem[j] - self.mem[i] + self.nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)