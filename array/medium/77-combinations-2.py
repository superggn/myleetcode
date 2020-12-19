"""
    组合递归写法
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def search(n, k, i, cur):
            res = []
            if len(cur) == k: return [cur[:]]
            if i == n + 1: return []  # 暗示如果cur 还不够的话, 已经不能再继续搜索了
            # 不要 i 的搜索
            res.extend(search(n, k, i + 1, cur))
            # 要 i 搜索并恢复现场
            cur.append(i)
            res.extend(search(n, k, i + 1, cur))
            cur.pop()
            return res

        return search(n, k, 1, [])
