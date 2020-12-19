"""
    Rabin-Karp
    计算哈希值
    都特么什么玩意儿，看不明白
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_n, len_h = len(needle), len(haystack)
        if len_n > len_h:
            return -1

        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 31

        # lambda-function to convert character to integer
        h_to_int = lambda i: ord(haystack[i]) - ord('a')
        n_to_int = lambda i: ord(needle[i]) - ord('a')

        # compute the hash of strings haystack[:len_n], needle[:len_n]
        h = ref_h = 0
        for i in range(len_n):
            # 计算haystack的哈希值
            h = (h * a + h_to_int(i)) % modulus
            # 计算needle的哈希值
            ref_h = (ref_h * a + n_to_int(i)) % modulus
        if h == ref_h:
            return 0



        # const value to be used often : a**len_n % modulus
        a_n = pow(a, len_n, modulus)
        for start in range(1, len_h - len_n + 1):
            # compute rolling hash in O(1) time
            h = (h * a - h_to_int(start - 1) * a_n + h_to_int(start + len_n - 1)) % modulus
            if h == ref_h:
                return start

        return -1


h = "aaacaaab"
n = "aaab"
sol = Solution()
print(sol.strStr(h, n))
