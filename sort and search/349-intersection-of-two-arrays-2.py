"""
    效率和时间复杂度和集合运算差不多，行数还多，就当多一条路记一下好了


"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        intersection = []
        prev = None
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if nums1[i] != prev:
                    intersection.append(nums1[i])
                    prev = nums1[i]
                i += 1
                j += 1
        return intersection




