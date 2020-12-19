"""
    从后向前遍历，用while
    依次比较排序
    不使用额外的控件，因为num1后面是空着的，所以优先从后向前排



"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        size1 = m - 1
        size2 = n - 1
        index = m + n - 1
        # 从后向前遍历
        while size1 >= 0 and size2 >= 0 and index >= 0:
            if nums1[size1] > nums2[size2]:
                nums1[index] = nums1[size1]
                size1 -= 1
                index -= 1
            else:
                nums1[index] = nums2[size2]
                index -= 1
                size2 -= 1
        # 在某一项清空后，把剩下的数组全部放到nums1里

        # num1不必进行放置操作，因为本来就在里面
        # while size1 >= 0:
        #     nums1[index] = nums1[size1]
        #     size1 -= 1
        #     index -= 1

        while size2 >= 0:
            nums1[index] = nums2[size2]
            index -= 1
            size2 -= 1

