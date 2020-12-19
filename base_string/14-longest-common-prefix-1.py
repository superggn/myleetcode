from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        # min_ls = [索引，长度]
        if not strs:
            return ""
        min_ls = [0, len(strs[0])]
        # 找最短的
        for idx, item in enumerate(strs):
            if len(item) < min_ls[1]:
                min_ls[0] = idx
                min_ls[1] = len(item)
        shortest = strs[min_ls[0]]

        common_prefix = shortest
        for str_item in strs:
            for j in range(len(shortest)):
                if str_item[j] != shortest[j]:
                    if len(common_prefix) > j:
                        common_prefix = shortest[:j]
        return common_prefix


strs = ["flower", "flow", "flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))