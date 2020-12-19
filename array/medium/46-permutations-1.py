"""
    来自李威威大佬
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # nums:输入需要遍历的内容
        # size:len(nums)
        # depth:深度
        # path:途经的选择
        # state:初始为0，深度+1时，则左移一位
        # res:结果数组
        def dfs(nums, size, depth, path, state, res):
            # 如果搜索的深度到达底层：在res中记录经历，退出
            # print(path)
            if depth == size:
                # 注意，这里没有用path[:]是因为在本代码中，后面递归使用的是path + [nums[i]]，相当于每次传入的path参数都是新构造的列表，不是同一个path不断进行append和pop操作
                res.append(path)
                return

            for i in range(size):
                # 判断state从右往左第i位，若为0，则没有遍历过，进入下一层
                # state为最高用到3位的flag变量，标志下一层有没有遍历过
                if ((state >> i) & 1) == 0:
                    # 进入下一层，参数变化：depth + 1,path + [nums[i]],state ^ (1<<i)
                    # state更新为：第i位置1

                    dfs(nums, size, depth + 1, path + [nums[i]], state ^ (1 << i), res)


        size = len(nums)
        # 边界条件
        if size == 0:
            return []

        state = 0
        res = []
        # 使用函数更改res
        dfs(nums, size, 0, [], state, res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
