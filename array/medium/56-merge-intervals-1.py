"""
    题目：
        合并区间
    排序法
    https://leetcode-cn.com/problems/merge-intervals/solution/he-bing-qu-jian-by-leetcode-solution/
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            按照区间左边界排序intervals
            初始化结果数组
            遍历数组，若二者重合，则合并
        """

        # 按序遍历
        intervals.sort(key=lambda x: x[0])
        # 初始化merged
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            # 前一个的最大值后下一个的最小值比较
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
