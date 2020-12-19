"""
    leetcode天大狂徒的code

"""


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M[0])

        N = [[0.5] + item + [0.5] for item in M]
        N = [[0.5] * m] + N + [[0.5] * m]

        for i in range(1, len(N) - 1):
            for j in range(1, len(N[0]) - 1):
                total = [
                    N[i - 1][j - 1], N[i - 1][j], N[i - 1][j + 1],
                    N[i][j - 1], N[i][j], N[i][j + 1],
                    N[i + 1][j - 1], N[i + 1][j], N[i + 1][j + 1],
                ]
                sums = 0
                padding_cnt = 0
                for item in total:
                    if item != 0.5:
                        sums += item
                    else:
                        padding_cnt += 1
                M[i - 1][j - 1] = int(sums / (9 - padding_cnt))
        return M

        # padding
        # 为了防止丢失图像角落信息，对图像周围进行像素填充
        # 在边上加1圈0.5，0.5是用来标注哪些是空格的
        m = len(M[0])
        N = [[0.5] + i + [0.5] for i in M]
        N = [[0.5] * (m + 2)] + N + [[0.5] * (m + 2)]

        # 卷积
        # 求平均
        for i in range(1, len(N) - 1):
            for j in range(1, len(N[0]) - 1):
                total = [N[i - 1][j - 1], N[i][j - 1], N[i + 1][j - 1],
                         N[i - 1][j], N[i][j], N[i + 1][j],
                         N[i - 1][j + 1], N[i][j + 1], N[i + 1][j + 1]]
                sums, k = 0, 0
                for _ in total:
                    if _ != 0.5:
                        sums += _
                    else:
                        k += 1
                M[i - 1][j - 1] = int(sums / (9 - k))
        print("__________________")
        print("__________________")
        return M


nums = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
s = Solution()
print(s.imageSmoother(nums))
