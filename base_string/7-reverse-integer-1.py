class Solution:
    def reverse(self, x: int) -> int:
        f = 1 if x > 0 else -1
        b = 0
        while (x != 0):
            a = abs(x) % 10
            b = b * 10 + a
            x = int(x / 10)
            if b > 2 ** 31:
                return 0
        return b * f


x = 8463847412
y = -123
s = Solution()
print(s.reverse(x))
