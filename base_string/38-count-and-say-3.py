"""
    通过定义全局变量加速判别，有取巧的嫌疑
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        # 边界条件确认
        if n == 1:
            return '1'
        # 递归调用
        s = self.countAndSay(n - 1)

        pos, res = 0, ''
        # 用enumerate取出idx和value
        for idx, value in enumerate(s):
            if value != s[pos]:
                res += str(idx - pos) + s[pos]
                pos = idx
        res += str(len(s) - pos) + s[-1]  # 最后一个元素莫忘统计
        return res


n = 4
sol = Solution()
print(sol.countAndSay(n))
