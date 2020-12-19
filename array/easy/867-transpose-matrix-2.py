from typing import List

from cffi.backend_ctypes import xrange


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [list(i) for i in zip(*A)]


A = [[1, 2, 3], [4, 5, 6]]
s = Solution()
print(s.transpose(A))
