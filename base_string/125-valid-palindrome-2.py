"""
    使用内建函数
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 格式化字符串大小写
        s = s.lower()
        # 临时变量ls
        ls = []
        for item in s:
            if item in 'abcdefghijklmnopqrstuvwxyz0123456789':
                ls.append(item)
        return (ls[::1] == ls[::-1])


s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))
