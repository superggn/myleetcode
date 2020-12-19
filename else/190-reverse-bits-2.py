"""
    带记忆化的按字节颠倒
    https://leetcode-cn.com/problems/reverse-bits/solution/dian-dao-er-jin-zhi-wei-by-leetcode/
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 24
        cache = dict()
        while n:
            # 0xff是8位
            # 反转低8位，挪到最高位
            ret += self.reverseByte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
        return ret

    def reverseByte(self, byte, cache):
        # 若反转后的结果没有在字典中存储，待会儿反转完存一下
        if byte not in cache:
            # 这里是怎么反转的，没看明白
            cache[byte] = ((byte * 0x0202020202) & 0x010884422010) % 1023
        return cache[byte]


s = Solution()
print(s.reverseBits(2147483648))
