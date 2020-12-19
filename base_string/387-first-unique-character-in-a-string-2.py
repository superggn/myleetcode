class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 初始化ans为数组长度
        ans = len(s)
        # 每个字母都跑一边s
        for c in "abcdefghijklmnopqrstuvwxyz":
            # 这里idx初始化为左侧第一个的位置
            idx = s.find(c)
            # 若从左侧遍历s，能找到c，且c的位置和从右侧遍历的一致（即字符串中只有一个c存在），更新ans
            if idx != -1 and idx == s.rfind(c):
                ans = min(ans, idx)
        # 若ans与长度相等，则ans不在数组内（数组最大索引为n-1，ans若为n，肯定没更新过）
        return ans if ans != len(s) else -1


# s = "loveleetcode"
s = "llggc"
sol = Solution()
print(sol.firstUniqChar(s))
