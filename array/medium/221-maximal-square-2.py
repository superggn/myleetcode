"""
    采用二进制思路的方法
    https://leetcode-cn.com/problems/maximal-square/solution/fen-xiang-yi-ge-bu-yong-dong-tai-gui-hua-cai-yong-/
"""


class Solution:
    def getWidth(self, num):  # 步骤3：求一个数中连续最多的1
        w = 0
        while num > 0:
            num &= num << 1
            w += 1
        return w

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nums = [int(''.join(n), base=2) for n in matrix]  # 步骤1：每一行当作二进制数
        res, n = 0, len(nums)
        for i in range(n):  # 步骤2：枚举所有的组合，temp存储相与的结果
            temp = nums[i]
            for j in range(i, n):
                temp &= nums[j]
                if self.getWidth(temp) < j - i + 1:
                    break
                res = max(res, j - i + 1)
        return res * res
