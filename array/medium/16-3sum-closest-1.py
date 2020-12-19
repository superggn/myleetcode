"""
    双指针
    去重思路：先更新数值，如果和上一个一样，跳过此次循环
    来自时间统计中最快的一批

"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = float("inf")
        nums.sort()
        for cur in range(n - 2):
            # 一堆边界条件的处理

            # 相同元素只需要处理一次，去重
            if cur > 0 and nums[cur] == nums[cur - 1]:
                continue

            # 处理target不在[min,max]区间内的情况，这种情况就不需要遍历了
            # 三数之和最大值如果比target还小，此值已经是此轮循环最接近target的值。
            max_sum = nums[cur] + nums[-1] + nums[-2]
            # 三数之和最小值如果比target还大，此值已经是整个循环最接近target的值，因为数组是升序的，而我们已经遍历过左边了，不需要continue，直接break
            min_sum = nums[cur] + nums[cur + 1] + nums[cur + 2]
            if max_sum <= target:
                if abs(max_sum - target) < abs(res - target):
                    res = max_sum
                continue
            if min_sum >= target:
                if abs(min_sum - target) < abs(res - target):
                    res = min_sum
                break

            # 初始化左指针
            left = cur + 1
            # 初始化右指针
            right = n - 1
            # 循环双指针
            while left < right:
                three_sum = nums[cur] + nums[left] + nums[right]
                # 先判定是否更新res
                if abs(three_sum - target) < abs(res - target):
                    res = three_sum
                # 再判定three_sum往哪个方向挪动，挪动完，去重
                if three_sum > target:
                    right -= 1
                    # 注意，这里的去重要在right更新后再进行，否则会发生跳过元素的事情
                    # 去重：和上一个进行比较
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif three_sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    return target
        return res


# nums = [-1, 0, 1, 1, 55]
nums = [-1, 0, 1, 1, 55]
# nums = [0, 5, -1, -2, 4, -1, 0, -3, 4, -5]
t = 3
s = Solution()
print(s.threeSumClosest(nums, t))
