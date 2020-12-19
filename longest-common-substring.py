"""
    不对，超时了
"""

class Solution:
    def LCS(self, str1, str2):
        dp = []

        # 初始化
        for i in range(len(str1) + 1):
            dp.append([])
            for j in range(len(str2) + 1):
                dp[i].append(0)

        # 填表
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

        # for i in range(len(dp)):
        #     for j in range(len(dp[0])):
        #         print(dp[i][j], end=" ")
        #     print()
        # 找值

        max_len = 0
        x = y = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if max_len <= dp[i][j]:
                    max_len = dp[i][j]
                    x = i - 1
                    y = j - 1

        sub_str = str2[y - max_len + 1:y + 1]
        return sub_str


# str1 = "1AB2345CD"
# str2 = "12345EF"


str1 = "1AB23475CD"
str2 = "12345EF"

s = Solution()
print(s.LCS(str1, str2))
