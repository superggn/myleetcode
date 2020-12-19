"""
    使用pair数组
    https://leetcode-cn.com/problems/relative-ranks/solution/tong-su-yi-dong-python3506-xiang-dui-ming-ci-by-fe/

"""
from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        pairs = []
        # 构造pairs数组
        for i in range(len(nums)):
            pairs.append([nums[i], i])
        # 使用pairs元素0位置，排序
        pairs.sort(key=lambda a: a[0], reverse=True)
        # 遍历pairs,根据pairs里面的索引，填充res
        res = [''] * len(nums)
        for i in range(len(pairs)):
            # print(type(pairs[i][1]), ":", pairs[i][1])
            if i == 0:
                res[pairs[i][1]] = "Gold Medal"
            if i == 1:
                res[pairs[i][1]] = "Silver Medal"
            if i == 2:
                res[pairs[i][1]] = "Bronze Medal"
            if i > 2:
                res[pairs[i][1]] = str(i + 1)
        return res


nums = [4, 5, 3, 2, 1]
s = Solution()
print(s.findRelativeRanks(nums))
