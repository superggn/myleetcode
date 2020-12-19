"""
    快速幂 + 递归

    定义quickMul函数
    return通过正负分类讨论

"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # quickMul:递归进行幂次相乘
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
