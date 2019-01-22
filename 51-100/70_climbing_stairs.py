import math
class Solution(object):
    def climbStairs(self, n):
        '''
        count, l = 1, n // 2 #最多的2步个数
        for i in range(1, l + 1): #每种2步个数的不重复排列数
            a = n - 2 * i
            m1 = math.factorial(a + i)
            n1 = math.factorial(i)
            n2 = math.factorial(a)
            count += m1 / (n1 * n2)

        return int(count)
        '''
        # 感觉可以参考91题解法如下 但是是迭代 比上一钟方法慢
        if n == 1:
            return 1
        cnt = [0] * (n)
        cnt[0], cnt[1] = 1, 2
        for i in range(2, n):
            cnt[i] = cnt[i - 1] + cnt[i - 2]
        return cnt[n - 1]



print(Solution().climbStairs(2))