class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x , -n)
        elif n % 2:
            return x * self.myPow(x * x, n - 1)
        else:
            return self.myPow(x * x, n // 2)