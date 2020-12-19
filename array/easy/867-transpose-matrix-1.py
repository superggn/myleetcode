from typing import List

from cffi.backend_ctypes import xrange


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return None
        m = len(A)
        n = len(A[0])
        res = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = A[i][j]
        return res


A = [[1, 2, 3], [4, 5, 6]]
s = Solution()
print(s.transpose(A))
