class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {}
        for i in s:
            if i in dct.keys():
                dct[i] += 1
            else:
                dct[i] = 1
        for i in range(len(s)):
            if dct[s[i]] <= 1:
                return i


s = "loveleetcode"
sol = Solution()
print(sol.firstUniqChar(s))
