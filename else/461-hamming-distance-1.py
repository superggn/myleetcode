class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        o = x | y
        a = x & y
        cnt_o = 0
        cnt_a = 0
        while o:
            cnt_o += 1 if o & 1 else 0
            o >>= 1
        while a:
            cnt_a += 1 if a & 1 else 0
            a >>= 1
        return cnt_o - cnt_a


x = 1
y = 4
s = Solution()
print(s.hammingDistance(x, y))

