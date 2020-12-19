"""
    sunday解法
    https://leetcode-cn.com/problems/implement-strstr/solution/python3-sundayjie-fa-9996-by-tes/
    偏移表告诉我们下一步可能匹配需要移动的最小步数。
    比双指针好
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Func: 计算偏移表
        # st:即needle
        # dic：根据输入下一个字符的内容，开始计算haystack切片窗口需要滑动的步数

        def calShiftMat(st):
            dic = {}
            for i in range(len(st) - 1, -1, -1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st) - i
            dic["ot"] = len(st) + 1
            return dic

        # 其他情况判断
        if len(needle) > len(haystack):
            return -1
        if needle == "":
            return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx + len(needle) <= len(haystack):
            # 待匹配字符串
            str_cut = haystack[idx:idx + len(needle)]
            # 判断是否匹配
            if str_cut == needle:
                return idx
            else:
                # 边界处理,若切出来的字符串已经到了尽头，返回-1
                if idx + len(needle) >= len(haystack):
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx + len(needle)]
                # cur_c:下一个字符
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]

        return -1 if idx + len(needle) >= len(haystack) else idx


h = "aaacaaab"
n = "aaab"
sol = Solution()
print(sol.strStr(h, n))
