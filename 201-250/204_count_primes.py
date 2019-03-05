class Solution:
    def countPrimes(self, n):
        rlt = [True] * n
        rlt[0], rlt[1] = False, False
        for i in range(2, n):
            if rlt[i]:
                for j in range(2, (n - 1)//i + 1):
                    rlt[i * j] = False
        return sum(rlt)

print(Solution().countPrimes(10))