"""
    布赖恩·克尼根算法
    通过减一，异或，消除右侧的1
"""


class Solution:
    def hammingDistance(self, x, y):
        xor = x ^ y
        distance = 0
        # 直接越过0位，操作最右侧的1！！！！！！简直神一样的操作
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance


x = 1
y = 41238
s = Solution()
print(s.hammingDistance(x, y))
