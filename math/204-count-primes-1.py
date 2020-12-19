"""
    埃氏筛法
    https://leetcode-cn.com/problems/count-primes/solution/pythonzui-you-jie-fa-mei-you-zhi-yi-liao-ba-by-bru/

"""


class Solution:
    def countPrimes(self, n):
        """
        求n以内的所有质数个数（纯python代码）
        """
        # 最小的质数是 2
        if n < 2:
            return 0
        # 初始化位置数组，用1标记素数
        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0  # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号n的所有质数的倍数剔除
        # 通过在[2,sqrt(n)+1)区间内的
        # 把不是质数的剔除，剩下的位置肯定全部是质数
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(isPrime)


n = 1000000
s = Solution()
print(s.countPrimes(n))
