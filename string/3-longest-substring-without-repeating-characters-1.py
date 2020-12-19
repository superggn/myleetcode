"""
    滑动窗口
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 不只是相邻的，只要子串中出现过1次，就不允许第二次出现
        # 哈希集合，记录每个字符是否出现过
        occur = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        right, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occur.remove(s[i - 1])
            # 在没越界，且无重复的条件下，右边界不断延伸
            while right + 1 < n and s[right + 1] not in occur:
                # 不断地移动右指针
                occur.add(s[right + 1])
                right += 1
            # 第 i 到 right 个字符是一个极长的无重复字符子串
            ans = max(ans, right - i + 1)
        return ans
