"""
    通过定义全局变量加速判别，有取巧的嫌疑
"""

# 初始化res列表
res = ['1']

class Solution:
    def countAndSay(self, n: int) -> str:
        len_res = len(res)
        # 边界条件处理
        if len_res > n - 1:
            return res[n - 1]
        for m in range(n - len_res):
            # pre:上一行
            pre = res[-1]
            # num:被描述的数字
            # 初始化被描述的数字，即"m个n"中的n
            num = pre[0]
            # 初始化上一行被描述数字的个数，即"m个n"中的m
            cnt = 0
            # cur:当前行
            cur = ''
            for i in range(len(pre)):
                # 如果下一个不重复，更新当前行
                if pre[i] != num:
                    cur = cur + str(cnt) + num
                    num = pre[i]
                    cnt = 0
                # 上一行遍历到头了
                if i == len(pre) - 1:
                    cnt += 1
                    cur = cur + str(cnt) + num
                    break
                cnt += 1
            res.append(cur)
        return res[n - 1]
