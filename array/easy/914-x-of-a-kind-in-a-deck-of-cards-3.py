"""
    手动写GCD
"""
import collections
from functools import reduce


class Solution(object):
    def hasGroupsSizeX(self, deck):
        vals = collections.Counter(deck).values()
        gcd = reduce(self.gcd0, vals)
        return gcd >= 2

    def gcd0(self, a, b):
        if a > b:
            smaller = b
            bigger = a
        else:
            smaller = a
            bigger = b
        if bigger % smaller == 0:
            return smaller
        else:
            return self.gcd0(smaller, bigger % smaller)


# d = [1, 2, 3, 4, 4, 3, 2, 1]
d = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]

s = Solution()
print(s.hasGroupsSizeX(d))
