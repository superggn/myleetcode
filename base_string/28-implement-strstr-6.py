"""
    KMP from CSDN
    感觉有问题，哪来的那么多-1

"""

needle0 = 'abaabcac'
class Solution:
    def get_next(self, T):
        i = 0
        j = -1
        next_val = [-1] * len(T)
        while i < len(T) - 1:
            if j == -1 or T[i] == T[j]:
                i += 1
                j += 1
                # next_val[i] = j
                if i < len(T) and T[i] != T[j]:
                    next_val[i] = j
                else:
                    next_val[i] = next_val[j]
            else:
                j = next_val[j]
        return next_val

    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        next = self.get_next(needle)
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(needle):
            return i - j
        else:
            return -1


if __name__ == '__main__':
    haystack1 = 'acabaabaabcacaabc'
    needle1 = 'abaabcac'

    s = Solution()
    print(s.strStr(haystack1, needle1))  # 输出 "5"
