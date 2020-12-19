"""
    官方的暴力法
    https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/solution/qia-pai-fen-zu-by-leetcode-solution/
"""
import collections


class Solution(object):
    def hasGroupsSizeX(self, deck):
        count = collections.Counter(deck)
        size = len(deck)
        for x in range(2,size + 1):
            if size % x == 0:
                if all(v%x == 0 for v in count.values()):
                    return True
        return False


d = [1, 2, 3, 4, 4, 3, 2, 1]

s = Solution()
print(s.hasGroupsSizeX(d))
