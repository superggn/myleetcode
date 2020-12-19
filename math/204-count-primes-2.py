"""
    欧拉筛法
    https://leetcode-cn.com/problems/count-primes/solution/python-ou-la-xian-xing-shai-xiang-xi-jie-shi-by-is/

"""


class Solution:
    # def countPrimes(self, n: int) -> int:
    #    if n < 2:
    #        return 0
    #    #埃氏筛法：
    #    count = 0
    #    list = [True] * n
    #    list[0] = list[1] = False
    #    for i in range(2,n,1):
    #        if list[i]:
    #            count += 1
    #            for j in range(i*i,n,i):
    #                list[j] = False;
    #    return count

    def countPrimes(self, n: int) -> int:
        """
            欧拉法
        """
        if n < 2:
            return 0
        cnt = 0
        list_prime = [1] * n
        prime = []
        # 开始遍历
        for i in range(2, n, 1):
            if list_prime[i]:
                prime.append(i)
                cnt += 1

            # 精髓
            #
            # 循环条件：
            #   j < count: 被筛除的合数的素因子必须是之前已经发现的
            #   i * prime[j] < n: 要被筛除的合数的大小必须小于n
            #
            # 核心判断终止条件：
            #   i % prime[j] == 0: prime[j]是i的质因数
            #   因为如果prime[j]是i的质因数，则i是一个合数
            #   那么i == k * prime[j]，k是一个正整数
            #   那么i * prime[j + 1]形成的合数可以写成：
            #   i * prime[j + 1] = k * prime[j] * prime[j + 1]
            #   又prime列表是严格递增的（显然）
            #   即此合数至少有一个质因子prime[j] < prime[j + 1]
            #   不再满足通过最小质因子筛去合数的原则
            #
            # 举个例子，假设n == 20，当i == 2时，prime == [2]
            # 第一次循环j == 0，则会筛除所有值为2 * 质数表中的质数的合数
            # 也就是只会筛除4，之后j + 1 == 2，大于了已知质数的个数
            # i的循环进下一层，i == 3，prime == [2, 3]
            # 这个时候第一个被筛除的合数是 3 * prime[0] == 6
            # 第二个是3 * prime[1] == 9，之后j + 1 == 3，又大于了已知质数的个数
            # 以此类推，i == 4时，筛去8
            # i == 5时，5会被加入质数表，并筛去10，15
            # i == 6时，筛去6 * 2 == 12
            # i == 7时，7会被加入质数表，筛去7 * 2 == 14
            # i == 8时，筛去8 * 2 == 16
            # i == 9时，筛去9 * 2 == 18
            # i == 10时，不做任何事
            # i == 11时，11加入质数表
            # i == 12时，不做任何事
            # i == 13时，13加入质数表
            # i == 14时，不做任何事
            # i == 15时，不做任何事
            # i == 16时，不做任何事
            # i == 17时，17加入质数表
            # i == 18时，不做任何事
            # i == 19时，19加入质数表
            # i == 20时，不做任何事
            # 最终得到了8个小于20的质数，2，3，5，7，11，13，17，19
            #
            # 究其根本 就是欧拉线性筛不通过i的倍数，而是通过质数的倍数去筛
            # 而根据 算数基本定理 ，一个合数必定可以写成若干个质数之积
            # e.g.  150 = 15 * 10 = 2 * 3 * 5 * 5
            # 那么只要选择使用最小的质因子筛除一个数，就能保证这个数只被删除一次
            # 如上文的150，如果用埃氏筛，那么他会被2、3、5各筛去一次
            # 但如果用线性筛，就只会被筛去一次: 在i == 75时用最小质因子2筛除
            j = 0

            while j < cnt and i * prime[j] < n:
                # 标记找到的合数，flag为0
                list_prime[i * prime[j]] = 0
                # 如果已经找到了i的质因子（如果i是合数）就不再继续
                if i % prime[j] == 0:
                    break
                j += 1

        return cnt


if __name__ == '__main__':
    n = 1000000
    s = Solution()
    print(s.countPrimes(n))
