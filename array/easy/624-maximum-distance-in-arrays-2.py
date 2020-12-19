"""
    在空列表里存一下max和min，取出最大最小值，根据索引是否相同，分类讨论
"""
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # 初始化空列表
        min_list = []
        max_list = []
        # 初始化min_max列表
        for arr in arrays:
            min_list.append(arr[0])
            max_list.append(arr[-1])

        max_max = max(max_list)
        min_min = min(min_list)
        # 根据最大最小值数量及处于哪个列表进行分类讨论
        if max_list.count(max_max) > 1 or min_list.count(min_min) >1:
            return max_max - min_min
        else:
            if max_list.index(max_max) != min_list.index(min_min):
                return max_max - min_min
            else:
                # 注意，此处干掉最大最小，意思是这个数组的都不考虑了
                max_list.remove(max_max)
                min_list.remove(min_min)
                max_2 = max(max_list)
                min_2 = min(min_list)
                return max(max_max - min_2, max_2 - min_min)


