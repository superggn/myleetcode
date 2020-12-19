"""

    https://leetcode-cn.com/problems/jump-game/solution/pythonji-bai-97kan-bu-dong-ni-chui-wo-by-mo-lan-4/
"""


class Solution:
    def canJump(self, nums):
        """
            初始化
            遍历整个数组，更新最远距离
            判别最远坐标 >= len(nums) - 1
        """
        max_i = 0
        for idx,jump in enumerate(nums):
            if idx <= max_i < idx + jump:
                max_i = idx + jump
        return max_i >= len(nums) - 1


        max_i = 0  # 初始化当前能到达最远的位置
        i = -1
        # 循环的目的是更新最远可以到达的距离
        for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
            if i <= max_i < i + jump:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + jump  # 更新最远能到达位置
        print(max_i, i, sep=" ")
        return max_i >= len(nums) - 1


nums = [4, 0, 0, 0, 0]
s = Solution()
print(s.canJump(nums))
