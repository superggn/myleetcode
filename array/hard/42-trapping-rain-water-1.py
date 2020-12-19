"""
    单调栈
    https://leetcode-cn.com/problems/trapping-rain-water/solution/xiong-mao-shua-ti-python3-shi-pin-jiang-jie-dan-di/
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
            初始化+边界条件
            遍历    外层:遍历+更新stack
                   内层:计算+pop
        """
        length = len(height)
        if length < 3:
            return 0
        res, idx = 0, 0
        stack = []
        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                dist = idx - stack[-1] - 1
                h = min(height[stack[-1]], height[idx]) - height[top]
                res += dist * h
            stack.append(idx)
            idx += 1
        return res

        # 边界条件+初始化
        length = len(height)
        if length < 3:
            return 0
        res, idx = 0, 0
        stack = []
        # 从左向右遍历
        # 内层循环负责计算
        # 外层负责遍历，向栈中压入元素
        while idx < length:
            # 判别栈里有货而且当前值比栈顶大，
            # 要么把栈里的货清空，要么进入下一个“凹”字
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                # 当前计算的底边高度
                top = stack.pop()  # index of the last element in the stack
                # 如果
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += (dist * h)
            # 栈中每次都压入当前数值
            stack.append(idx)
            idx += 1
        return res


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
