"""
    双指针
    比较粗暴，遍历完之后如果不成功，直接返回初始位置
    变量名说明：
    len_h
    len_n
    ph:pointer_haystack
    pn:pointer_needle
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_n, len_h = len(needle), len(haystack)
        if len_n == 0:
            return 0

        ph = 0
        #
        while ph < len_h - len_n + 1:
            # find the position of the first needle character
            # in the haystack string
            # 双指针推进
            while ph < len_h - len_n + 1 and haystack[ph] != needle[0]:
                ph += 1

            # compute the max match string
            # 开始匹配工作，保留匹配结束后的当前匹配长度cur_len
            cur_len = pn = 0
            # while p_n和p_h没超出范围,且相应位置字符匹配
            while pn < len_n and ph < len_h and haystack[ph] == needle[pn]:
                ph += 1
                pn += 1
                cur_len += 1

            # if the whole needle string is found,
            # return its start position
            if cur_len == len_n:
                return ph - len_n

            # otherwise, backtrack
            # 若匹配不成功，返回原来的位置
            ph = ph - cur_len + 1

        return -1

