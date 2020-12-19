"""
    回溯+剪枝
    李威威大佬
    https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
"""
from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(nums, begin, path, residue):
            """

                边界条件处理，什么时候遍历到叶子节点，处理res
                在for循环里进行下一层的遍历，修改path
            """
            # 边界条件
            size = len(nums)
            if residue == 0:
                res.append(path[:])
                return
            # index在begin到size中循环
            for index in range(begin, size):
                if nums[index] > residue:
                    break

                if index > begin and nums[index - 1] == nums[index]:
                    continue

                path.append(nums[index])
                dfs(nums, index + 1, path, residue - nums[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(candidates, 0, [], target)
        return res


nums = [10, 1, 2, 7, 6, 1, 5]
target = 8

s = Solution()
print(s.combinationSum2(nums, target))
