"""
    速度最快的范例，先排除边界条件，再分类讨论
    不要多加不必要的类型转换
"""
import collections
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        if k < 0:
            return 0
        if k == 0:
            # 如果k = 0，生成1个counter数组，目的是查看是否有重复的数值，因为多个重复值不统计，所以不计算具体数量，只要有2个及以上即可
            nums_dict = collections.Counter()
            for num in nums:
                nums_dict[num] += 1
            # 列表推导式
            return sum(1 for val in nums_dict.values() if val > 1)
        # 开始遍历是否有目标数组
        # 生成集合
        # 遍历集合，查看目标+k是否存在，存在几个不一样的
        nums_ = set(nums)
        return sum(1 for num in nums_ if num + k in nums_)


nums = [3, 1, 4, 1, 5]
k = 2
s = Solution()
print(s.findPairs(nums, k))

# nums = [1, 2, 3, 4, 5]
# k = 1
# s = Solution()
# print(s.findPairs(nums, k))
#
# nums = [1, 3, 1, 5, 4]
# k = 0
# s = Solution()
# print(s.findPairs(nums, k))
