"""
    异或
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_ = x ^ y
        cnt = 0
        while xor_:
            cnt += 1 if xor_ & 1 else 0
            xor_ >>=1
        return cnt



x = 1
y = 4
s = Solution()
print(s.hammingDistance(x, y))

