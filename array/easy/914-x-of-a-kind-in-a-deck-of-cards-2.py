"""
    最大公约数
    https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/solution/qia-pai-fen-zu-by-leetcode-solution/
"""
import collections
from functools import reduce


class Solution(object):
    def hasGroupsSizeX(self, deck):
        from math import gcd
        vals = collections.Counter(deck).values()
        # reduce(func,params)
        # func是一个两个参数的函数
        # reduce把params里的参数往func里面塞，返回值作为第一个参数，直到params全部用完
        # 简而言之就是扩充func可接受的参数数量，原来只能接收2个参数，现在把一整个数组的参数全怼进去
        return reduce(gcd, vals) >= 2


d = [1, 2, 3, 4, 4, 3, 2, 1]

s = Solution()
print(s.hasGroupsSizeX(d))
