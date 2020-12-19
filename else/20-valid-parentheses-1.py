"""
    使用字典及stack实现括号匹配
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # 边界条件：若不成对，干掉
        # 初始化pair字典，存储用的栈
        # 遍历s，
        # 若是后括号：若栈里没货了，GG；若和栈里的前括号不匹配，GG；弹出对应前括号
        # 若不是后括号，把字符往栈里塞；
        # 若stack里还有货，GG，否则通关
        if len(s) % 2 == 1:
            return False
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
