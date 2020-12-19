from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        for i in range(len(s)//2):
            s[i],s[size-i-1] = s[size-i-1],s[i]