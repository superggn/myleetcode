"""
    中心扩展算法
    https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
"""


class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        # 初始化左右边界
        # 遍历s
        # 对每个位置，求长度为偶数的回文串和长度为奇数的最长回文串
        # 根据最长的回文串长度，更新左右边界
        # 返回
        start, end = 0, 0
        for i in range(len(s)):
            # 长度=奇数
            left1, right1 = self.expandAroundCenter(s, i, i)
            # 长度=偶数
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]
