class Solution:
    def smallestFactorization(self, a):
        if a < 10:
            return a
        res = 0
        n = 1
        int_max = pow(2, 31) - 1
        for i in range(9, 1, -1):
            while a%i == 0:
                a /= i
                res += n*i
                n *= 10
                if res > int_max:
                    return 0
        if a!= 1:
            return 0
        return res

print(Solution().smallestFactorization(15))