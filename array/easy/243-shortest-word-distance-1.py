"""
    双指针法
"""

from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
#       先找word1和word2
#       再找word2，更新最小距离
        i = 0
        j = 0
        while words[i] != word1:
            i += 1
        while words[j] != word2:
            j += 1
        min_dis = abs(i-j)
        while True:
            if i > j:
                j += 1
                while j < len(words) and words[j] != word2:
                    j += 1
                if j == len(words):
                    break
                else:
                    min_dis = min(min_dis, abs(i - j))
            else:
                i += 1
                while i < len(words) and words[i] != word1:
                    i += 1
                if i == len(words):
                    break
                else:
                    min_dis = min(min_dis, abs(i - j))
        return min_dis

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
s = Solution()
print(s.shortestDistance(words, word1, word2))
