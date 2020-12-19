"""
作者：larcenciel
链接：https: // leetcode - cn.com / problems / degree - of - an - array / solution / 697 - shu - zu - de - du - san - bu - zou - 100 - by - larcenciel /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1.先找到度，用字典统计，再找最大统计数，即为度
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        du = 0
        for i in dic:
            if du < dic[i]:
                du = dic[i]
        if du == 1:
            return 1

        # 根据度找数，找出所有出现频次与度相等的数
        num = []
        for i in dic:
            if dic[i] == du:
                num.append(i)
        # 根据数找该数最大最小下标，根据下标计算最短连续子数组
        start, end = 0, 0
        num_length = []
        for i in num:
            # 设置flag,记录最小下标（第一次出现的下标）
            flag = 1
            for j in range(len(nums)):
                # 不断更新最大下标
                if nums[j] == i:
                    end = j
                # 记录第一次的下标
                if flag == 1:
                    if nums[j] == i:
                        start = j
                        flag -= 1
            num_length.append(end - start + 1)
        return min(num_length)
