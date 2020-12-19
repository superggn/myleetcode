"""
    dfs
    https://leetcode-cn.com/problems/path-sum/solution/xiong-mao-shua-ti-python3-di-gui-fu-shi-pin-ti-jie/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        if root.val == target and not root.left and not root.right:
            return True
        left = self.hasPathSum(root.left, target - root.val)
        right = self.hasPathSum(root.right, target - root.val)
        return left or right
