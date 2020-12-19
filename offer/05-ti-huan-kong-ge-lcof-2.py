"""

    MD这道题性能纯属看运气

"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        temp = []
        for i in s:
            if i != " ":
                temp.append(i)
            else:
                temp.append("%20")
        return "".join(temp)


str0 = "We are happy."
sol = Solution()
print(sol.replaceSpace(str0))
