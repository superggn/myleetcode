"""
    回溯算法
    这里不需要使用used，直接用begin和size在传参的时候对子递归进行限制即可
    https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/

"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            定义dfs函数
            判定是否遍历到底(path遍历中，减到了负数)
                修改res输出
            进入for循环
                判断该点是否遍历过

                进入下一层

            初始化结果
            开始遍历
            输出结果
        """
        def dfs(candidates,begin,size,path,target,res):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
                return
            for i in range(begin,size):
                path.append(candidates[i])
                dfs(candidates,i,size,path,target - candidates[i],res)
                path.pop()
        size = len(candidates)
        if not size:
            return []
        res = []
        dfs(candidates,0,size,[],target,res)
        return res


        # 定义dfs函数
        def dfs(candidates, begin, size, path, res, target):
            # 若已经满足条件或者遍历到树的底层了，即可退出
            # 在for循环里进行dfs遍历

            # print(path)
            # 若输入目标的和已经小于0:退出

            if target < 0:
                return
            # 若此时经历的路径，已经把目标削减到0:返回path
            if target == 0:
                res.append(path)
                return
            for index in range(begin, size):
                # 去重：在进入下一层的时候，仍然会遍历当前位置，直到到达最底层发现不符合要求
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


nums = [2, 3, 6, 7]
target = 7
s = Solution()
print(s.combinationSum(nums, target))
