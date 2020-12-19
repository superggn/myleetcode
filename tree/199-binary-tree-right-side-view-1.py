"""
    熊猫
    BFS
    https://leetcode-cn.com/problems/binary-tree-right-side-view/solution/xiong-mao-shua-ti-python3-bfsmo-ban-zong-jie-yi-2/
"""


# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        tmp_layer = collections.deque()  # 还是BFS用到的queue
        tmp_layer.append(root)  # 先将初始节点压入
        while len(tmp_layer) > 0:
            count = 0  # 计数，用来记录是某一层的第几个元素
            next_layer = []
            while len(tmp_layer) > 0:  # 处理某一层的节点
                tmp_node = tmp_layer.popleft()
                if count == 0:  # 根据题意只要最右侧的元素，所以根据下面先压入队列的是右子树，后压入左子树，我们只要队列中的第一个元素
                    res.append(tmp_node.val)
                count += 1
                # 将某个节点的右左子树压入
                if tmp_node.right is not None:
                    next_layer.append(tmp_node.right)
                if tmp_node.left is not None:
                    next_layer.append(tmp_node.left)
            tmp_layer = collections.deque(next_layer)  # 更新下一层的tmp
        return res
