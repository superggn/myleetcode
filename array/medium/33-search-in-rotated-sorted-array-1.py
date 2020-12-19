"""
    对一个旋转过的数组进行二分查找
    二分法
    来自官方
    https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/
    专注于有序的部分
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 边界条件
        if not nums:
            return -1
        # 初始化两侧指针
        l, r = 0, len(nums) - 1
        # 开始遍历
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                # 循环唯一出口
                return mid
            # 从这里开始，和普通二分查找不一样
            # 判别mid在两个单调区间中的哪个区域里，哪个区域就是有序的部分，在有序的部分查找
            if nums[0] <= nums[mid]:  # 从整体来看，若mid左侧为有序的区间，则在有序的部分查找
                # 这里注意下，target==mid已经在前面过滤掉了
                if nums[0] <= target < nums[mid]:
                    # 若有序，缩小区间
                    r = mid - 1
                else:
                    # 若不在有序区间内，甩个更新过去，进下个循环，在整个数组里面查
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


s = Solution()
# print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([1], 0))
