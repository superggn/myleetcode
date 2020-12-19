"""
    读题！！！
        从首行开始，从外向内螺旋遍历！
    循环遍历矩阵并在 适当 的位置改变方向
    https://leetcode-cn.com/problems/spiral-matrix/solution/yong-shi-40ms-xiao-hao-137mb-mei-bu-xiang-xi-zhu-s/
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
            边界条件
            初始化变量
            for循环遍历
                存当前元素和路径
                分类讨论(是否超出范围)，更新元素
        """
        if not matrix:
            return []
        # 初始化坐标、结果[]、方向向量的状态、步数变量di
        x = y = 0  # 矩阵元素位置初始化
        res = []  # 初始化，存储遍历后的矩阵元素

        dx = [0, 1, 0, -1]  # 方向：右，下，左，上
        dy = [1, 0, -1, 0]  # 注：与通常平面坐标系 记号 不同
        di = 0  # 初始化方向变量
        visited = set()  # 初始化集合，存储已走过的坐标
        m, n = len(matrix), len(matrix[0])  # 矩阵的行列
        # for循环遍历数组所有元素
        for i in range(m * n):
            # 存储当前位置
            # 存一下路径
            # 看看下一步是否应该换方向，分类讨论，更新坐标
            res.append(matrix[x][y])  # 存储遍历矩阵过的元素

            visited.add((x, y))  # 存储遍历过的坐标
            tx, ty = x + dx[di], y + dy[di]  # 先记录下一步坐标，用于判断下一步怎么走,提前判别是否越界
            if 0 <= tx < m and 0 <= ty < n and (tx, ty) not in visited:  # 判断坐标是否需变向，且没有遍历过
                x, y = tx, ty
            else:
                di = (di + 1) % 4  # 改变方向，右下左上为一圈，防止方向坐标越界
                x, y = x + dx[di], y + dy[di]  # 下一步坐标
        return res


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.spiralOrder(mat))
