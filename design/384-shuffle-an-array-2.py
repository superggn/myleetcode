"""
    Fisher-Yates 洗牌算法 【通过】
"""
import random


class Solution:
    def __init__(self, nums):
        self.array = nums
        # 这里用list是把original和原来的nums隔离开，复制出一块新的内存空间来存放original,不然会被引用传参改变数值
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        # 更新original存放的内存空间，防止在后面被改变
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = Solution(nums)
n1 = s.shuffle()
print(s.shuffle())
print(s.reset())
