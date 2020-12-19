"""
    3次比较
    据说这个是根据概率写的？？？
    奥，在高概率的情况下，过几个数之后，大概率只需要1次比较了

    注意啊，这里小心不要把 >= 和>混为一谈

"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        for item in nums:
            if item > third:
                if item < second:
                    third = item
                elif item > second:
                    if item < first:
                        third = second
                        second = item
                    elif item > first:
                        third = second
                        second = first
                        first = item

        if third == float("-inf"):
            return first
        else:
            return third


nums = [5, 2, 2]
s = Solution()
print(s.thirdMax(nums))


from typing import List
