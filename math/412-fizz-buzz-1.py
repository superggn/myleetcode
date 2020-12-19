from typing import List


class Solution:
    def helper(self, n):
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return str(n)

    def fizzBuzz(self, n: int) -> List[str]:
        nums = list(range(1, n + 1))
        # print(nums)
        for i in range(len(nums)):
            nums[i] = self.helper(nums[i])
        return nums


n = 10
s = Solution()
print(s.fizzBuzz(n))
