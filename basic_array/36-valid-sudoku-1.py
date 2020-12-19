"""
    这里如果leetcode出现了json错误，八成是测试用例写错了，人家的list输入不支持换行
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    # dct.get(target,default_value)
                    # 意思是更新字典中的次数值
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    # box_index：第几个大方块
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    # 这三个list[dct[i]]中，存储的是i出现的次数
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True


bd = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
      [".", "4", ".", "3", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", "3", ".", ".", "1"],
      ["8", ".", ".", ".", ".", ".", ".", "2", "."],
      [".", ".", "2", ".", "7", ".", ".", ".", "."],
      [".", "1", "5", ".", ".", ".", ".", ".", "."],
      [".", ".", ".", ".", ".", "2", ".", ".", "."],
      [".", "2", ".", "9", ".", ".", ".", ".", "."],
      [".", ".", "4", ".", ".", ".", ".", ".", "."]]

s = Solution()
print(s.isValidSudoku(bd))
