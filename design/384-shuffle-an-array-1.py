"""
    打乱数组：官方
    暴力法
"""
import random


class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        temp = list(self.array)
        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(temp))
            self.array[idx] = temp.pop(remove_idx)
        return self.array


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = Solution(nums)
print(s.shuffle())