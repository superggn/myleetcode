"""
    巧妙的移动数位方法
"""
# https://leetcode-cn.com/problems/number-of-1-bits/solution/python3-san-chong-fang-fa-qiu-jie-wei-1de-ge-shu-b/
# 二进制中最低位的1会通过n-1操作消失，而比最低位1高的位不变，通过n&=n-1保留剩余高位的1及低位的0；
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res


n = 0b11111111111111111111111111111101

s = Solution()
print(s.hammingWeight(n))
