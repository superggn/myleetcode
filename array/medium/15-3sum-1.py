"""
    排序+双指针
    https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
    思路：数组排序后，外层遍历start，内层遍历mid和end，mid和end是从两侧向中间查找的双指针
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not nums or n < 3:
            return []
        nums.sort()
        res = []
        # 在下面的循环中，start_pos是第一个数，mid是第2个，end是第3个（最右边的那个）
        for start in range(n):
            # 全大于0，没用
            if nums[start] > 0:
                return res
            # 若start和上一个遍历过的相等，跳过
            # 过滤掉重复的第1个数
            if start > 0 and nums[start] == nums[start - 1]:
                continue
            # 初始化mid和end
            mid = start + 1
            end = n - 1
            # 开始在[start+1,len(nums)-1]这个区间中，寻找三数和为0的mid和end
            while mid < end:
                if nums[start] + nums[mid] + nums[end] == 0:
                    res.append([nums[start], nums[mid], nums[end]])
                    while mid < end and nums[mid] == nums[mid + 1]:
                        mid = mid + 1
                    while mid < end and nums[end] == nums[end - 1]:
                        end = end - 1
                    mid = mid + 1
                    end = end - 1
                elif nums[start] + nums[mid] + nums[end] > 0:
                    end = end - 1
                else:
                    mid = mid + 1
        return res


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
