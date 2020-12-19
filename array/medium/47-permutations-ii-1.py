"""
    来自李威威大佬
    https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
"""
from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:
                    # 这里是剪枝条件：当前节点和上一个节点的相同，并且，上一个节点的值刚刚被撤销（位子空出来了，你这个长得和上一个一样的再坐进去，就重复了）
                    # 即去重
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []
        # 这里做一下排序
        # 注意，凡是涉及去重，即对相邻两个位置进行操作的，提前sort一下数组
        # 函数内部的去重是通过相同的数字相邻实现的，如果不排序，相同数字不相邻，去重会失效
        nums.sort()

        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


# n = [1, 1, 2]
n = [3, 3, 0, 3]

s = Solution()
print(s.permuteUnique(n))
