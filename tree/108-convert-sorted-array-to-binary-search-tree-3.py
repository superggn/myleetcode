"""
    方法三：中序遍历，选择任意一个中间位置数字作为根节点
"""

# Definition for a binary tree node.
from random import randint
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
                if left > right:
                    return None

                # 选择任意一个中间位置数字作为根节点
                mid = (left + right + randint(0, 1)) // 2

                root = TreeNode(nums[mid])
                root.left = helper(left, mid - 1)
                root.right = helper(mid + 1, right)
                return root

        return helper(0, len(nums) - 1)
