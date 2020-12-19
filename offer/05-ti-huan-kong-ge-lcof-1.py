class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ""
        for i in s:
            if i != " ":
                res += i
            else:
                res += "%20"
        return res
str0 = "We are happy."
s=Solution()
print(s.replaceSpace(str0))