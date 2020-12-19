"""
    BFS模板
    https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/tao-mo-ban-bfs-he-dfs-du-ke-yi-jie-jue-by-fuxuemin/
    负雪明烛
"""

# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 初始化容器
        queue = collections.deque()
        queue.append(root)
        res = []

        # 一轮while循环遍历一层
        while queue:
            # 初始化层
            size = len(queue)
            level = []
            # 遍历
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                # 向该层的level容器中压入cur.val
                level.append(cur.val)
                # 向待判别的queue容器中压入cur.left,cur.right
                queue.append(cur.left)
                queue.append(cur.right)
            # 若level不为空，向res中压入level
            if level:
                res.append(level)
        return res
