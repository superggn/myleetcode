"""
    从最后一位开始转换，处理每位
    如果中途没有跳出，意味着后几位全部为9，最后在数组的头部+1
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            digits[i] += 1
            if digits[i] < 10:
                break
            digits[i] = 0
        else:
            return [1] + digits
        return digits

n = [4, 3, 2, 1]
s = Solution()
print(s.plusOne(n))
