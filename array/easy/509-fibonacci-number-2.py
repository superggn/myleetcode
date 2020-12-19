"""
    注意！！
    递归类型的问题，可以使用动态规划！！！
    保存已经计算过的数值

    妹的，看了半天问题在哪，结果range语法搞错了
        range里面的逗号用成了冒号，结果各种return不在函数内，invalid syntax,'return' outside of function......

"""


class Solution:
    def memoir(self, number):
        dct = {0: 0, 1: 1}
        for i in range(2, number + 1):
            dct[i] = dct[i - 1] + dct[i - 2]

        return dct[number]

    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoir(N)


s = Solution()
print(s.fib(81) % (1e9 + 7))
