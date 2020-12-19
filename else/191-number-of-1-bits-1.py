"""
    移位方法
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += 1 if n&1 else 0
            n >>= 1
        return cnt

n = 0b11111111111111111111111111111101


s = Solution()
print(s.hammingWeight(n))


"""
    内建函数，取巧
"""
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count("1")


