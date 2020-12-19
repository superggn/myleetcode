"""
    粗暴遍历，用list存储临时变量
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_ls = []
        for i in s:
            if i in "asdfghjklzxcvbnmqwertyuiopASDFGHJKLZXCVBNMQWERTYUIOP0123456789":
                i = i.lower()
                temp_ls.append(i)
        if len(temp_ls) <= 1:
            return True
        for i in range(len(temp_ls)//2):
            if temp_ls[i] != temp_ls[len(temp_ls)-i-1]:
                return False
        return True

s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))
