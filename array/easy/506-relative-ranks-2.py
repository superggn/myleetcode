"""
    hashmap版本
"""
from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        hashmap = {}
        # 相当于还是构造了一个pairs，只不过pairs里面只存储数值，索引单独放在hashmap里
        pairs = []
        for i in range(len(nums)):
            pairs.append(nums[i])
            hashmap[nums[i]] = i
        pairs.sort(reverse=True)
        res = [''] * len(nums)
        for i in range(len(pairs)):
            if i == 0:
                res[hashmap[pairs[i]]] = 'Gold Medal'
            if i == 1:
                res[hashmap[pairs[i]]] = 'Silver Medal'
            if i == 2:
                res[hashmap[pairs[i]]] = 'Bronze Medal'
            if i > 2:
                res[hashmap[pairs[i]]] = str(i + 1)
        return res

        # ans = [0] * len(nums)
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # nums.sort(reverse=True)
        # for i in range(len(nums)):
        #     if i == 0:
        #         ans[hashmap[nums[i]]] = 'Gold Medal'
        #     if i == 1:
        #         ans[hashmap[nums[i]]] = 'Silver Medal'
        #     if i == 2:
        #         ans[hashmap[nums[i]]] = 'Bronze Medal'
        #     if i > 2:
        #         ans[hashmap[nums[i]]] = str(i + 1)
        # return ans


# nums = [4, 5, 3, 2, 1]
nums = [10, 3, 8, 9, 4]

s = Solution()
print(s.findRelativeRanks(nums))
