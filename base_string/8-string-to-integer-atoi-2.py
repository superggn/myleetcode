"""
    用frank588大佬的C++代码改一下
"""

# C++代码

"""
class Solution {
public:
    int myAtoi(string str) {
        int res = 0;
        int i = 0;
        int flag = 1;
        // 1. 检查空格
        while (str[i] == ' ') { i++; }
        // 2. 检查符号
        if (str[i] == '-') { flag = -1; }
        if (str[i] == '+' || str[i] == '-') { i++; }
        // 3. 计算数字
        while (i < str.size() && isdigit(str[i])) {
            int r = str[i] - '0';
            // ------ 4. 处理溢出，这是关键步骤 ------
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && r > 7)) { 
                return flag > 0 ? INT_MAX : INT_MIN;
            }
            // ------------------------------------
            res = res * 10 + r;
            i++;
        }
        return flag > 0 ? res : -res;
    }
};
 
作者：frank588
链接：https://leetcode-cn.com/problems/string-to-integer-atoi/solution/clean-c-code-by-frank588/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""



class Solution:
    def myAtoi(self, s: str) -> int:
        # 边界值
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31

        res = 0
        i = 0
        flag = 1
        # 边界条件
        if not s:
            return 0
        # 检查空格
        while i < len(s) - 1 and s[i] == ' ':
            i += 1
        # 检查符号
        if s[i] == '-':
            flag = -1
        # 索引向后推一位
        if s[i] == '+' or s[i] == '-':
            i += 1
        # 计算数字
        while i < len(s) and s[i].isdigit():
            # 待压入res的数字
            r = int(s[i])
            # // ------ 4. 处理溢出，这是关键步骤 ------
            # 这里的r是2**31-1 = 2147483647 的最后一位
            if res > int_max // 10 or (res == int_max // 10 and r > 7):
                return int_max if flag > 0 else int_min
            res = res * 10 + r
            i += 1
        return res if flag > 0 else -res


sol = Solution()
# s = "2147483648"
# s = "-91283472332"
# s = "91283472332"
# s = "-12asd"
# s = "asdas-12asd"
# s = ""
# s = " "
s = "   -42"

print(sol.myAtoi(s))
