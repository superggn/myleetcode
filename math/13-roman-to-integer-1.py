"""
    简单题：
        罗马数字转整数，左边比右边大，就减左边，反之加左边
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s) - 1):
            if dct[s[i]] < dct[s[i + 1]]:
                res -= dct[s[i]]
            else:
                res += dct[s[i]]
        res += dct[s[-1]]
        import time
        time.sleep(0.002)
        return res


