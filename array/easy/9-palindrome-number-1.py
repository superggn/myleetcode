class Solution:
    def isPalindrome(self, x: int) -> bool:
        re = str(x)[::-1]
        return re == str(x)


n = 121
s = Solution()
print(s.isPalindrome(n))
