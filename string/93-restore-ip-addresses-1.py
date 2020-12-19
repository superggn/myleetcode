"""
    递归
    https://leetcode-cn.com/problems/restore-ip-addresses/solution/fu-yuan-ipdi-zhi-by-leetcode-solution/
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 初始化IP地址段总数，ans,segments(类似path，当前遍历的路径)
        # 进入dfs
        # dfs:停止条件：找完了4段seg;遍历完了字符串
        # 进入下一层条件：前导0；

        seg_count = 4
        ans = list()
        segments = [0] * seg_count

        def dfs(seg_idx: int, seg_start: int):
            # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
            # 边界条件：先看有没有遍历到树的底层，再看有没有遍历完字符串
            if seg_idx == seg_count:
                # 看情况，是否满足append条件（刚好遍历完字符串）
                if seg_start == len(s):
                    ip_addr = ".".join(str(seg) for seg in segments)
                    ans.append(ip_addr)
                # 无论如何，到底了，完事
                return

            # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
            if seg_start == len(s):
                return

            # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
            if s[seg_start] == "0":
                segments[seg_idx] = 0
                dfs(seg_idx + 1, seg_start + 1)

            # 一般情况，枚举每一种可能性并递归
            # 初始化addr
            # 遍历：计算addr，根据值，判别是否进入下一层dfs
            addr = 0
            for seg_end in range(seg_start, len(s)):
                # addr: int, segments: List[int]
                addr = addr * 10 + (ord(s[seg_end]) - ord("0"))
                if 0 < addr <= 0xFF:
                    segments[seg_idx] = addr
                    dfs(seg_idx + 1, seg_end + 1)
                else:
                    break

        dfs(0, 0)
        return ans


s = "25525511135"
sol = Solution()
print(sol.restoreIpAddresses(s))
