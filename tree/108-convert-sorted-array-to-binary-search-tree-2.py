"""
    方法二：中序遍历，总是选择中间位置右边的数字作为根节点
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 在helper中输入数组的左右边界，生成TreeNode对象，开始递归调用生成子节点，
        # 函数返回当前节点，如果left和right左边和右边为None，返回None
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置右边的数字作为根节点
            mid = (left + right + 1) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)
