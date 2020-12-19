"""
    暴力
"""


class Solution:
    def fib(self, N: int) -> int:
        if N == 1:
            return 1
        elif N == 0:
            return 0
        return self.fib(N - 1) + self.fib(N - 2)

s = Solution()
print(s.fib(100))